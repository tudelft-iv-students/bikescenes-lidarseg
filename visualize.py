import numpy as np
import rerun as rr
import rerun.blueprint as rrb
import yaml
import argparse
from pathlib import Path

def load_class_metadata(root: Path):
    classes_path = root / "classes.yml"
    with open(classes_path, "r") as f:
        config = yaml.safe_load(f)
    colors = {int(k): (v[2], v[1], v[0]) for k, v in config.get("color_map", {}).items()}
    labels = {int(k): str(v) for k, v in config.get("labels", {}).items()}
    return labels, colors

def main():
    parser = argparse.ArgumentParser(description="LiDAR On-Demand Loader")
    parser.add_argument("root", type=str, help="Dataset root")
    rr.script_add_args(parser)
    args = parser.parse_args()
    
    root = Path(args.root)
    rr.script_setup(args, "Bikescenes_Loader")

    rr.log("world", rr.ViewCoordinates.RIGHT_HAND_Z_UP, static=True)

    extrinsic = np.array([
        [0.09150204, -0.99493988, -0.04149717, 1.09618485],
        [-0.06610063, 0.03551153, -0.99718084, 3.79028606],
        [0.99360862, 0.09398708, -0.06251678, 14.18161562],
        [0.0, 0.0, 0.0, 1.0],
    ])
    rotation = extrinsic[:3, :3]
    translation = extrinsic[:3, 3]
    eye = (-rotation.T @ translation).tolist()
    forward = (rotation.T @ np.array([0.0, 0.0, 1.0])).tolist()
    up = (rotation.T @ np.array([0.0, -1.0, 0.0])).tolist()
    look_target = (np.array(eye) + np.array(forward)).tolist()

    rr.send_blueprint(
        rr.blueprint.Blueprint(
            rrb.Horizontal(
                rrb.Spatial3DView(
                    origin="world",
                    contents="world/lidar/**",
                    eye_controls=rr.blueprint.EyeControls3D(
                        position=eye,
                        look_target=look_target,
                        eye_up=up,
                    ),
                ),
                rrb.Spatial2DView(
                    origin="world/camera",
                ),
            )
        )
    )

    labels_dict, color_map = load_class_metadata(root)
    bin_dir, img_dir, lbl_dir = root / "robosense_m1p", root / "images", root / "labels"
    bin_files = sorted(bin_dir.glob("*.bin"))

    print(f"✅ Ready. Processing {len(bin_files)} frames...")

    for i, bin_path in enumerate(bin_files):
        stem = bin_path.stem
        rr.set_time(timeline="frame_idx", sequence=i)

        raw_data = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
        points = raw_data[:, :3]
        
        label_path = lbl_dir / f"{stem}.label"
        if label_path.exists():
            sem = np.fromfile(label_path, dtype=np.uint32) & 0xFFFF
            point_colors = np.array([color_map.get(s, (128, 128, 128)) for s in sem], dtype=np.uint8)
            point_labels = [labels_dict.get(s, f"ID_{s}") for s in sem]
            rr.log("world/lidar", rr.Points3D(points, colors=point_colors, labels=point_labels, radii=0.03))
        else:
            rr.log("world/lidar", rr.Points3D(points, radii=0.03))

        img_path = img_dir / f"{stem}.png"
        if img_path.exists():
            rr.log("world/camera/image", rr.EncodedImage(path=img_path))

        if i % 500 == 0:
            print(f"Indexed {i}/{len(bin_files)}...")

    rr.script_teardown(args)

if __name__ == "__main__":
    main()