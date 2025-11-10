# <img src="assets/logo_small.png" height="46px" style="vertical-align: middle" /> BikeScenes-lidarseg dataset
[![arXiv](https://img.shields.io/badge/arXiv-10.48550%2FarXiv.2510.25901-b31b1b.svg)](https://doi.org/10.48550/arXiv.2510.25901)
[![Zenodo](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.17508644-1f70c1.svg)](https://doi.org/10.5281/zenodo.17508644)
[![BikeScenes Dataset](assets/bikescenes_map.png)](assets/bikescenes_map.png)

## Overview

The BikeScenes-lidarseg dataset provides semantically annotated 3D LiDAR data from a bicycle's perspective, collected around the TU Delft campus. It is created to facilitate research into cyclist-centric perception. For detailed information on data collection, processing, and baseline model performance, please refer to our accompanying paper:

* [BikeScenes: Online LiDAR Semantic Segmentation for Bicycles](https://arxiv.org/abs/2510.25901)

Authors: Denniz Goren, Holger Caesar 

## The SenseBike
<p align="center"><a href="assets/sensebike.png"><img src="assets/sensebike.png" alt="The SenseBike" width="500"></a></p>

This dataset was recorded using the SenseBike, which is based on the Holoscene X by <a href="https://www.borealbikes.com">Boreal Bikes</a>, with additions and modifications by members and students of the Intelligent Vehicles group of the TU Delft.
    
Key sensors on the SenseBike relevant to this dataset include a front-mounted RoboSense M1 Plus LiDAR, a SparkFun ICM-20948 IMU, an ArduSimple simpleRTK2B GPS, and an ArduCam IMX477 camera. Further details about the sensor setup and calibration can be found in our paper.
 
## Dataset Contents & File Structure
[![Overview Subsequences](assets/subsequences.jpeg)](assets/subsequences.jpeg)
Each LiDAR scan <code>.bin</code> file in <code>robosense_m1p/</code> has matching labels and images in <code>labels/</code> and <code>images/</code>, along with calibration and pose metadata used for multi-scan labeling.

The training and evaluation splits used in our paper are provided via <code>subsequences.json</code>, which maps contiguous frame ranges (e.g., <code>00</code>, <code>01</code>, etc.) onto the full trajectory. The folder structure is as follows:

<pre><code>bikescenes_lidarseg/
   ├── robosense_m1p/
   │   ├── 000000.bin
   │   └── ...
   ├── labels/
   │   ├── 000000.label
   │   └── ...
   ├── images/
   │   ├── 000000.png
   │   └── ...
   ├── calib.txt
   ├── classes.yaml
   ├── poses.txt
   └── subsequences.json 
</code></pre>

## Labeling Scheme
We utilize the 28 semantic classes from the SemanticKITTI dataset, with the addition of a distinct `bike-path` class. The labeling was performed manually using the [SemanticKITTI labeling tool](https://github.com/jbehley/point_labeler). 

[![Class Distribution Figure](assets/class_distribution.png)](assets/class_distribution.png)

## Downloading the Dataset
The dataset can be downloaded as a single .zip file from the following link:
- [Download the BikeScenes-lidarseg dataset](https://zenodo.org/records/17508644)

## Acknowledgements
We gratefully acknowledge the following projects and contributors, whose work and support were instrumental in the development of our dataset and paper:

- [SemanticKITTI](http://www.semantic-kitti.org/)
- [SemanticKITTI API](https://github.com/PRBonn/semantic-kitti-api)
- [Point Labeler](https://github.com/jbehley/point_labeler)
- [FRNet](https://github.com/Xiangxu-0103/FRNet)
- [GLIM](https://github.com/koide3/GLIM) 
- [Boreal Bikes](https://www.borealbikes.com)

## Citation
If you use this work in your research, please cite:

```bibtex
@misc{goren2025bikescenesonlinelidarsemantic,
      title={BikeScenes: Online LiDAR Semantic Segmentation for Bicycles}, 
      author={Denniz Goren and Holger Caesar},
      year={2025},
      eprint={2510.25901},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2510.25901}, 
}