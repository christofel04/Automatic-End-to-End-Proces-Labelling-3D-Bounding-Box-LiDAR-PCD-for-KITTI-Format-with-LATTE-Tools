import os

NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA = "/home/ofel04/3D_Labelling_Result_from_Bag_Files_All_Rosbag_Data/"

NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_ImageSets_Folder = NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA + "ImageSets/"

NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Training_Folder = NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA + "training/"

NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Testing_Folder = NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA + "testing/"

NAME_FOLDER_3D_LABELLING_RESULT_NEW_DATA_ADDED = "/media/ofel04/Backup/KITTI_Dataset/kitti/testing/label_2/"#"/home/ofel04/3D_Labelling_Result_Hyundai_New_Racing/"

NAME_FOLDER_3D_LABELLING_RESULT_LiDAR_DATA_ADDED = "/media/ofel04/Backup/KITTI_Dataset/kitti/testing/"#"/home/ofel04/latte/app/test_dataset/11_drive_0000_sync/"

Maximum_Number_of_3D_Labelling_Result_All_Rosbag_Data = max( [ int( str( i ).replace( ".bin" , "" ) ) for i in os.listdir( NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Training_Folder + "velodyne/" ) ] )

i = Maximum_Number_of_3D_Labelling_Result_All_Rosbag_Data + 1

for Name_3D_Labelling_Result_New_Data in sorted( os.listdir( NAME_FOLDER_3D_LABELLING_RESULT_NEW_DATA_ADDED ) ) :

    # Put 3D Labelling Result Rosbag Hyundai Data into 3D Labelling Result All Rosbag Hyundai Data Training Data

    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_LABELLING_RESULT_LiDAR_DATA_ADDED + "image_2/" + str( Name_3D_Labelling_Result_New_Data ).replace( ".txt" , "") + ".png" ,
                                      NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Training_Folder + "image_2/" + str( i ).zfill( 6 ) + ".png" ) )
    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_LABELLING_RESULT_NEW_DATA_ADDED + "/" + Name_3D_Labelling_Result_New_Data  ,
                                      NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Training_Folder + "label_2/" + str( i ).zfill( 6 ) + ".txt" ) )
    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_LABELLING_RESULT_LiDAR_DATA_ADDED + "velodyne/" + str( Name_3D_Labelling_Result_New_Data ).replace( ".txt" , "") + ".bin" ,
                                      NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Training_Folder + "velodyne/" + str( i ).zfill( 6 ) + ".bin" ) )
    os.system( "sudo cp {} {}".format( "000000.txt" ,
                                      NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Training_Folder + "calib/" + str( i ).zfill( 6 ) + ".txt" ) )
    
    f = open( NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_ImageSets_Folder + "train.txt" , "a+" )

    #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

    f.writelines( str( i  ).zfill( 6 ) + "\n" )

    f.close()

    f = open( NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_ImageSets_Folder + "trainval.txt" , "a+" )

    #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

    f.writelines( str(  i ).zfill( 6 ) + "\n" )

    f.close()

    if ( ( ( i - Maximum_Number_of_3D_Labelling_Result_All_Rosbag_Data ) % 10 >= 6 ) & ( ( i - Maximum_Number_of_3D_Labelling_Result_All_Rosbag_Data ) % 10 <= 7 ) ) :

        f = open( NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_ImageSets_Folder + "val.txt" , "a+" )

        #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

        f.writelines( str(  i ).zfill( 6 ) + "\n" )

    if ( ( ( i - Maximum_Number_of_3D_Labelling_Result_All_Rosbag_Data ) % 10 >= 8 ) & ( ( i - Maximum_Number_of_3D_Labelling_Result_All_Rosbag_Data ) % 10 ) <= 9 ) :

        # Put 3D Labelling Result Rosbag Hyundai Data into 3D Labelling Result All Rosbag Hyundai Data Validation Data
    
        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_LABELLING_RESULT_LiDAR_DATA_ADDED + "image_2/" + str( Name_3D_Labelling_Result_New_Data ).replace( ".txt" , "") + ".png" ,
                                      NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Testing_Folder + "image_2/" + str( i ).zfill( 6 ) + ".png" ) )
        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_LABELLING_RESULT_NEW_DATA_ADDED + "/" + Name_3D_Labelling_Result_New_Data  ,
                                            NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Testing_Folder + "calib/" + str( i ).zfill( 6 ) + ".txt" ) )
        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_LABELLING_RESULT_LiDAR_DATA_ADDED + "velodyne/" + str( Name_3D_Labelling_Result_New_Data ).replace( ".txt" , "") + ".bin" ,
                                            NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Testing_Folder + "velodyne/" + str( i ).zfill( 6 ) + ".bin" ) )
        os.system( "sudo cp {} {}".format( "000000.txt" ,
                                            NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_Testing_Folder + "calib/" + str( i ).zfill( 6 ) + ".txt" ) )

        f = open( NAME_FOLDER_3D_LABELLING_RESULT_ALL_ROSBAG_DATA_ImageSets_Folder + "test.txt" , "a+" )

        #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

        f.writelines( str( i  ).zfill( 6 ) + "\n" )

        f.close()

    print( "Success Adding New Data " + str( Name_3D_Labelling_Result_New_Data ) + "...." )

    i = i + 1

    

        
    


