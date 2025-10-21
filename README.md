# <img src="assets/logo_small.png" height="46px" style="vertical-align: middle" /> BikeScenes-lidarseg dataset

[![BikeScenes Dataset GIF](assets/bikescenes_map.png)](assets/bikescenes_map.png)


## Overview

The BikeScenes-lidarseg dataset provides semantically annotated 3D LiDAR data from a bicycle's perspective, collected around the TU Delft campus. It is created to facilitate research into cyclist-centric perception. For detailed information on data collection, processing, and baseline model performance, please refer to our accompanying paper:

* **[link to paper]**

Authors: Denniz Goren, Holger Caesar 

## The SenseBike

<table>
  <tr>
    <td>
      <p>
        This dataset was recorded using the SenseBike, which is based on the Holoscene X by <a href="https://www.borealbikes.com">Boreal Bikes</a>, with additions and modifications by members and students of the Intelligent Vehicles group of the TU Delft.
      </p>
      <p>
        Key sensors on the SenseBike relevant to this dataset include a front-mounted RoboSense M1 Plus LiDAR, a SparkFun ICM-20948 IMU, an ArduSimple simpleRTK2B GPS, and an ArduCam IMX477 camera. Further details about the sensor setup and calibration can be found in our paper.
      </p>
    </td>
    <td align="right" valign="top">
      <a href="assets/sensebike.png">
        <img src="assets/sensebike.png" alt="SenseBike Platform Image" width="1500">
      </a>
    </td>
  </tr>
</table>

## Dataset Contents & File Structure
<table>
  <tr>
    <td>
      <p>
         Each LiDAR scan <code>.bin</code> file in <code>robosense_m1p/</code> has matching labels and images in <code>labels/</code> and <code>images/</code>, along with calibration and pose metadata used for multi-scan labeling.
      </p>
      <p>
        The training and evaluation splits used in our paper are provided via <code>subsequences.json</code>, which maps contiguous frame ranges (e.g., <code>00</code>, <code>01</code>, etc.) onto the full trajectory. The folder structure is as follows:
      </p>
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
   ├── poses.txt
   └── subsequences.json 
</code></pre>
    </td>
    <td align="right" valign="top">
      <a href="assets/subsequences.png">
        <img src="assets/subsequences.png" alt="Subsequences Overview" width="1500">
      </a>
      <p>Locations of subsequences</p>
    </td>
  </tr>
</table>

## Labeling Scheme

We utilize the 28 semantic classes from the SemanticKITTI dataset, with the addition of a distinct `bike-path` class. The labeling was performed manually using the [SemanticKITTI labeling tool](https://github.com/jbehley/point_labeler). 


[![Class Distribution Figure](assets/class_distribution.png)](assets/class_distribution.png)


## Acknowledgements
We gratefully acknowledge the following projects and contributors, whose work and support were instrumental in the development of our dataset and paper:

- [SemanticKITTI](http://www.semantic-kitti.org/)
- [SemanticKITTI API](https://github.com/PRBonn/semantic-kitti-api)
- [Point Labeler](https://github.com/jbehley/point_labeler)
- [FRNet](https://github.com/Xiangxu-0103/FRNet)
- [GLIM](https://github.com/koide3/GLIM) 
- [Boreal Bikes](https://www.borealbikes.com)

## Citation
