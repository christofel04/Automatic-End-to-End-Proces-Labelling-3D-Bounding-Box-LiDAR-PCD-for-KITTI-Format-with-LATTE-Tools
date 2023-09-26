#####################################################
# Preprocessing Files to Make LiDAR Dataset Bag Files into LiDAR KITTI Dataset
# For Preprocessing Files LiDAR Dataset Bag Files into LiDAR Dataset Labelling by LiDAR 3D Bounding Box Labelling Tool LATTE
# By : Christofel Rio Goenawan
#       Master of AI & Robotics at Korea Advanced Institute of Technology
# If there is Advice and Help or you want To Chit Chat Me kindly call me on christofel.goenawan@kaist.ac.kr

import os

# Convert all LiDAR Point Cloud Data to LiDAR Bin Datas

NAME_FOLDER_DATASET_FOR_LABELLING = "/home/ofel04/data_from_bag_For_Hyundai_Race_New_Data/"#"/media/ofel04/eb36cbe5-b485-4b41-a943-aa0452f90da3/home/ofel04/data_from_bag_For_Hyundai_Race_New_Data/"#"/media/ofel04/T7/data_from_bag_For_Hyundai_Race_6/"

NAME_FOLDER_LIDAR_BIN_DATA = NAME_FOLDER_DATASET_FOR_LABELLING + "bin_data/"# "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_6/bin_data/"

NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD = NAME_FOLDER_DATASET_FOR_LABELLING + "ground_removed/" #"/media/ofel04/T7/data_from_bag_For_Hyundai_Race_6/ground_removed/"

NAME_FOLDER_LiDAR_IMAGE_DATA_FOR_LiDAR_KITTI_DATASET = NAME_FOLDER_DATASET_FOR_LABELLING + "image/"# "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_6/image/"

NAME_FOLDER_LiDAR_CALIBRATION_FILES_FOR_KITTI_DATASET = NAME_FOLDER_DATASET_FOR_LABELLING + "oxts/"# "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_6/oxts/"

NAME_FOLDER_SE_SSD_DATASET_BAG_FILES = "/media/ofel04/eb36cbe5-b485-4b41-a943-aa0452f90da3/home/ofel04/data_from_bag_For_Hyundai_Race_New_Data/"#"/home/ofel04/data_from_bag_For_Hyundai_Race_New_Data/"#"/home/ofel04/data_from_bag_For_Hyundai_Race_6/"#/home/ofel04/data_from_bag_For_Hyundai_Race_1/"

# Check if Folder LiDAR Bin Data there or not

if os.path.exists( NAME_FOLDER_DATASET_FOR_LABELLING ) == False :
    
    os.mkdir( NAME_FOLDER_DATASET_FOR_LABELLING )

if os.path.exists( NAME_FOLDER_LIDAR_BIN_DATA ) == False :
    
    os.mkdir( NAME_FOLDER_LIDAR_BIN_DATA )



print( "Change LiDAR Point Cloud Data into LiDAR Bin Data...")


    
os.system( "python pcd2bin-master/pcd2bin.py --pcd_path={} --bin_path={}".format( NAME_FOLDER_SE_SSD_DATASET_BAG_FILES + "os1-128/",
NAME_FOLDER_LIDAR_BIN_DATA ))

# Change All LiDAR Bin Data into LiDAR Bin Data Format


for LiDAR_Bin_Data_in_LiDAR_Data_Folder in sorted( os.listdir( NAME_FOLDER_LIDAR_BIN_DATA ) ):
    
    if LiDAR_Bin_Data_in_LiDAR_Data_Folder.find( ".bin" ) != -1 :
        
        os.system( "mv {} {}".format( NAME_FOLDER_LIDAR_BIN_DATA + LiDAR_Bin_Data_in_LiDAR_Data_Folder ,
                                     NAME_FOLDER_LIDAR_BIN_DATA + str(int( LiDAR_Bin_Data_in_LiDAR_Data_Folder.replace( "file_name_" , "" ).replace( ".bin" , "" ))).zfill( 6 ) + ".bin" ) )
        

# Change All LiDAR Point Cloud Data into LiDAR Point Cloud Data Without Groud Point Cloud

if os.path.exists( NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD ) == False :
    
    os.mkdir( NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD  )

print( "Change LiDAR Point Cloud Data into LiDAR Point Cloud without Ground Point Cloud Data..." )

os.system( "python export_pointcloud_without_ground_nuscenes.py {} {}".format( NAME_FOLDER_SE_SSD_DATASET_BAG_FILES + "os1-128/" ,
                                                                              NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD ) )


os.system( "python pcd2bin-master/pcd2bin.py --pcd_path={} --bin_path={}".format( NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD ,
NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD ))

for LiDAR_Bin_Data_in_LiDAR_Data_Folder in sorted( os.listdir( NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD ) ):
    
    if LiDAR_Bin_Data_in_LiDAR_Data_Folder.find( ".bin" ) != -1 :
        
        os.system( "mv {} {}".format( NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD + LiDAR_Bin_Data_in_LiDAR_Data_Folder ,
                                     NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD + str(int( LiDAR_Bin_Data_in_LiDAR_Data_Folder.replace( "file_name_" , "" ).replace( ".bin" , "" ))).zfill( 6 ) + ".bin" ) )
        

os.system( "rm {}*.pcd".format( NAME_FOLDER_LiDAR_BIN_DATA_WITHOUT_GROUND_POINTCLOUD ) )

# Change All LiDAR Images Data into LiDAR Images Data KITTI Dataset

print( "Change LiDAR Images Data into LiDAR Images Data KITTI Dataset..." )

if os.path.exists( NAME_FOLDER_LiDAR_IMAGE_DATA_FOR_LiDAR_KITTI_DATASET ) == False :
    
    os.mkdir( NAME_FOLDER_LiDAR_IMAGE_DATA_FOR_LiDAR_KITTI_DATASET )

try :
    
    for LiDAR_Image_Data_in_LiDAR_Image_Data_Files in sorted( os.listdir(  NAME_FOLDER_SE_SSD_DATASET_BAG_FILES + "cam-front/" )) :
        
        if LiDAR_Image_Data_in_LiDAR_Image_Data_Files.find( ".png" ) != -1 :
            
            if ( int( LiDAR_Image_Data_in_LiDAR_Image_Data_Files.replace( "cam-front_" , "" ).replace( ".png" , "")) + 1 ) % 3 == 0 :
            
                os.system( "cp {} {}".format( NAME_FOLDER_SE_SSD_DATASET_BAG_FILES + "cam-front/" + LiDAR_Image_Data_in_LiDAR_Image_Data_Files ,
                                        NAME_FOLDER_LiDAR_IMAGE_DATA_FOR_LiDAR_KITTI_DATASET + str( int( LiDAR_Image_Data_in_LiDAR_Image_Data_Files.replace( "cam-front_" , "" ).replace( ".png" , "" ))).zfill( 6 ) + ".png" ) )
                
except :

    for LiDAR_Image_Data_in_LiDAR_Image_Data_Files in sorted( os.listdir(  NAME_FOLDER_LIDAR_BIN_DATA )) :
        
        if LiDAR_Image_Data_in_LiDAR_Image_Data_Files.find( ".bin" ) != -1 :
            
            os.system( "cp {} {}".format( "000000.png" ,
            NAME_FOLDER_LiDAR_IMAGE_DATA_FOR_LiDAR_KITTI_DATASET + LiDAR_Image_Data_in_LiDAR_Image_Data_Files.replace( ".bin" , ".png" ) ) )

# Change All LiDAR Calibration Files into LiDAR Calibration File

if os.path.exists( NAME_FOLDER_LiDAR_CALIBRATION_FILES_FOR_KITTI_DATASET ) == False :
    
    os.mkdir( NAME_FOLDER_LiDAR_CALIBRATION_FILES_FOR_KITTI_DATASET )
    
print( "Change All LiDAR Calibration Files into LiDAR Calibration Files for KITTI Dataset..." )
 
for LiDAR_Calibration_Files_in_LiDAR_Calibration_Files in sorted( os.listdir( NAME_FOLDER_LIDAR_BIN_DATA ) ):
    
    os.system( "cp {} {}".format( "00000.txt" , NAME_FOLDER_LiDAR_CALIBRATION_FILES_FOR_KITTI_DATASET + LiDAR_Calibration_Files_in_LiDAR_Calibration_Files.replace( ".bin" , ".txt" ) ) )
    

