# Automatic End to End Process Labelling SFA 3D Bounding Box Object Detection for KITTI Format using LATTE Bounding Box Tools
**Automatic Process Labelling Deep Learning Super Fast Accurate SFA 3D Object Detection using LATTE Bounding Box Tools**

Process of Automatic Labelling SFA 3D Datasets using LATTE Bounding Box Tools can be seen as below

![alt text]( ./Figure_of_Automatic_Process_Labelling_SFA_3D_using_LATTE_Bounding_Box_Tools/Process_Automatic_Labelling_SFA_3D_Datasets_using_Bounding_Box_Tools_LATTE.drawio%20(1).png)

## Using Bounding Box Tools LATTE

- First Download Bounding Box Tools LATTE on Github Folders. You Can Download Bounding Box Tools LATTE on Github Folder by Command this Command Line.

```
git clone https://github.com/bernwang/latte.git
```

- Install dependencies. By default we use Python3.

```
pip install -r requirements.txt
```

- Download pre-trained COCO weights (mask_rcnn_coco.h5) from the releases page into `app/Mask_RCNN` in the below Link.

https://github.com/matterport/Mask_RCNN/releases

![ alt text ]( ./Figure_of_Automatic_Process_Labelling_SFA_3D_using_LATTE_Bounding_Box_Tools/Screenshot%20from%202023-07-06%2017-36-49.png)

## Using Automatic Process Labelling SFA 3D using LATTE Bounding Box Tools

- Then Download Automatic Labelling SFA 3D  using LATTE Bounding Box Tools on Github. You can Download Automatic Labelling SFA 3D using Latte Bounding Box Tools using Command Command Line below.

```
git clone https://github.com/christofel04/Automatic-Process-Labelling-SFA-3D-using-LATTE-Bounding-Box-Tools.git
```

- Then Download all needed package of Automatic Labelling SFA 3D using LATTE Bounding Box Tools using Python Pip Package. You Can Download all needed package of Automatic Labelling SFA 3D using LATTE Bounding Box Tools using Command Line as below.

```
pip install -r requirements.txt
```

## Using Preprocessing Labelling SFA 3D Dataset

- Then change Folder Name of Se SSD Bag Files Name in Python Script Preprocessing_LiDAR_Point_Cloud_Bag_Files_to_KITTI_Dataset.py into SE SSD Bag Files Name. You Can change Folder Name of SE SSD Bag Files Name into SE SSD Bag Files Name as below.

![ alt text ]( ./Figure_of_Automatic_Process_Labelling_SFA_3D_using_LATTE_Bounding_Box_Tools/Screenshot%20from%202023-07-06%2018-04-44.png)

- Then Use Python Script Preprocessing_LiDAR_Point_Cloud_Bag_Files_to_KITTO_Dataset.py by using this command.

```
sudo python Preprocessing_LiDAR_Point_Cloud_Bag_Files_to_KITTI_Dataset.py
```

- After using Python Script of Preprocessing_LiDAR_Point_Cloud_Bag_Files_to_KITTI_Dataset changes all the Dataset_for_Labelling Folder Result to /latte/app/test_dataset/Dataset_for_Labelling. The folder of /latte/app/test_dataset/Dataset_for_Labelling in LATTE app/test_dataset folder can be seen as below.

![ alt text ]( ./Figure_of_Automatic_Process_Labelling_SFA_3D_using_LATTE_Bounding_Box_Tools/Screenshot%20from%202023-07-06%2019-05-34.png )

## Using Process Labelling SFA 3D Dataset

- Then Change Folder Name of LiDAR Point Cloud SE SSD Data in Python Script ``NAME_FOLDER_LiDAR_POINT_CLOUD_SE_SSD_DATA`` into Name Folder LiDAR Point Cloud Data and change Folder Name of LATTE Labelling Result SE SSD Data in Python Script Process_Labelling_SFA_3D_Dataset.py as below.

![ alt text ]( ./Figure_of_Automatic_Process_Labelling_SFA_3D_using_LATTE_Bounding_Box_Tools/Screenshot%20from%202023-07-06%2019-14-59.png )

-Then Use Python Script Process_Labelling_SFA_3D_Dataset.py by using command Line as below.

```
sudo python Process_Labelling_SFA_3D_Dataset.py
```

- Then Go to Folder Bounding Box Tools LATTE and un the tool, run python app.py in wherever you have your app directory is by using Command as below.

```
sudo python app.py
```

- Open http://127.0.0.1:5000/ on a browser (FireFox has been noted to have compatibility issues). Then Labelling Bounding Box SE SSD Bag Files Dataset by Make Bounding Box in LATTE Bounding Box Tools.

- Process of Labelling Bounding Box SE SSD Dataset using LATTE Bounding Box Tools Can be seen as below.

![ alt text ]( ./Figure_of_Automatic_Process_Labelling_SFA_3D_using_LATTE_Bounding_Box_Tools/Screenshot%20from%202023-07-06%2020-36-54.png )

## Using Process Transforms Result SFA 3D Dataset

- Then We will transform Result SFA 3D Dataset Label by using Python Script Process_Transform_Result_3D_Labelling_Result.py. 
Transform Result SFA 3D Dataset using Python Script Process_Transform_Result_3D_Labelling_Result.py can be use by Command Line as below.

```
sudo python Process_Transform_Result_3D_Labelling_Result.py
```

- Then We Can Have the SFA 3D Dataset Bounding Box KITTI Format as below.

![ alt text ]( ./Figure_of_Automatic_Process_Labelling_SFA_3D_using_LATTE_Bounding_Box_Tools/Screenshot%20from%202023-07-06%2020-56-31.png )





