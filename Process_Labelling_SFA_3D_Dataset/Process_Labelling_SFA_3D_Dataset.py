import os

NAME_FOLDER_LiDAR_POINT_CLOUD_SE_SSD_DATA = "/home/ofel04/Preprocessing_Labelling_SFA_3D_Dataset/Dataset_for_Labelling/bin_data/"

NAME_FOLDER_LATTE_LABELLING_RESULT_SE_SSD_DATA = "/home/ofel04/latte/app/output/Dataset_for_Labelling/"#/home/ofel04/latte/app/output/7_drive_0080_sync/"

import json

for File_Labelling_Output_SE_SSD_Data in sorted( os.listdir( NAME_FOLDER_LiDAR_POINT_CLOUD_SE_SSD_DATA )) :
    
    if File_Labelling_Output_SE_SSD_Data.find( ".bin" ) != -1 :
        
        File_Labelling_Output_SE_SSD_Data_With_SE_SSD_Cars = json.load( open( "01178.json" , "r+" ) )
        
        New_File_Labelling_Output_SE_SSD_Data_With_SE_SSD_Cars = File_Labelling_Output_SE_SSD_Data_With_SE_SSD_Cars
        
        New_File_Labelling_Output_SE_SSD_Data_With_SE_SSD_Cars[ "frame" ][ "fname" ] = "Dataset_for_Labelling" + "/" + File_Labelling_Output_SE_SSD_Data.replace( ".bin" , "" )
        
        # Save File Labelling Output SE SSD Data With SE SSD Cars 
        
        print( "Save File Labelling Output SE SSD Data with SE SSD Cars : " + File_Labelling_Output_SE_SSD_Data )
        
        
        export = json.dump( New_File_Labelling_Output_SE_SSD_Data_With_SE_SSD_Cars , open( NAME_FOLDER_LATTE_LABELLING_RESULT_SE_SSD_DATA + File_Labelling_Output_SE_SSD_Data.replace( ".bin" , ".json" ) , "w+" ) )
        
        
        