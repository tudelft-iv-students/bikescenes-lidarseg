# OpenBike LiDAR Segmentation Dataset

[![OpenBike Dataset GIF](assets/openbike.gif)](assets/openbike.gif)


## Overview

The OpenBike LiDAR Segmentation Dataset provides 3D semantic segmentation data from a bicycle's perspective, collected around the TU Delft campus. It is designed to facilitate research into cyclist-centric perception. For detailed information on data collection, processing, and baseline model performance, please refer to our accompanying paper:

* **[link to paper]**

Authors: Denniz Goren, Holger Caesar. 

## The SenseBike

<div style="display: flex; align-items: center; justify-content: space-between; gap: 0px;">

<div style="flex: 1;">
<p>
This dataset was recorded using the SenseBike, which is based on the Holoscene X by <a href="https://www.borealbikes.com">Boreal Bikes</a>, with additions and modifications by members and students of the Intelligent Vehicles group of the TU Delft. 

Key sensors on the SenseBike relevant to this dataset include a front-mounted RoboSense M1 Plus LiDAR, a SparkFun ICM-20948 IMU, an ArduSimple simpleRTK2B GPS, and an ArduCam IMX477 camera. Further details about the sensor setup and calibration can be found in our paper.

</p>
</div>

<div style="flex: 1; text-align: right;">
<a href="assets/sensebike.png">
<img src="assets/sensebike.png" alt="SenseBike Platform Image" style="max-width: 100%; height: auto;">
</a>
</div>

</div>

## Dataset Contents & File Structure
<div style="display: flex; align-items: center; justify-content: space-between; gap: 20px;">

<div style="flex: 1;">
<p>
The OpenBike Segmentation dataset is provided in two main directories: <code>entire_sequence</code> and <code>subsequences</code>.
</p>

<p>
The <code>entire_sequence</code> directory contains the full, uninterrupted recording, along with associated images and poses for each scan. In <code>subsequences</code>, we provide the same core data, but split into sequential segments (e.g., <code>00</code>, <code>01</code>, etc.) designed for train/test splits to reproduce the results in our paper.
</p>

<p>
The data within <code>subsequences</code> is structured to be compatible with the SemanticKITTI format, including the <code>velodyne</code> (for LiDAR point clouds) and <code>labels</code> folder structure, to allow for easy integration with existing data loaders and models. The folder structure is as follows:
</p>

<pre>
<code>
openbike/
├── entire_sequence/      
│   ├── velodyne/          
│   │   ├── 1739357499107089281.bin
│   │   └── ...
│   ├── labels/             
│   │   ├── 1739357499107089281.label
│   │   └── ...
│   ├── images/             
│   │   ├── 1739357499107089281.png
│   │   └── ...
│   ├── calib.txt           
│   └── poses.txt          
│
├── subsequences/           
│   ├── 00/                
│   │   └── ...
│   ├── 01/                 
│   │   └── ...
│   ├── ...                 
│   ├── 08/                 
│   │   └── ...
</code>
</pre>

</div>

<div style="flex: 1; text-align: right;">
<a href="assets/subsequences.png">
<img src="assets/subsequences.png" alt="Subsequences Overview" style="max-width: 100%; height: auto;">
</a>
<p style="text-align: center; margin-top: 10px;">Locations of subsequences</p>
</div>

</div>

## Labeling Scheme

We utilize the 28 semantic classes from the SemanticKITTI dataset, with the addition of a distinct `bike-path` class. The labeling was performed manually using the SemanticKITTI labelling tool. 


[![Class Distribution Figure](assets/class_distribution.png)](assets/class_distribution.png)



## Acknowledgements
We gratefully acknowledge the following projects and contributors, whose work and support were instrumental in the development of our dataset and paper:

- [SemanticKITTI](http://www.semantic-kitti.org/)
- [SemanticKITTI API](https://github.com/PRBonn/semantic-kitti-api)
- [Point Labeler](https://github.com/jbehley/point_labeler)
- [FRNet](https://github.com/Xiangxu-0103/FRNet)
- [GLIM](https://github.com/koide3/GLIM) 
- [Boreal Bikes](https://www.borealbikes.com)