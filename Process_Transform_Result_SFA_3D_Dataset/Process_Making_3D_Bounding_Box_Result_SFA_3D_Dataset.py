import os

NAME_FOLDER_3D_Labelling_Result = "/home/ofel04/Automatic-End-to-End-Proces-Labelling-3D-Bounding-Box-LiDAR-PCD-for-KITTI-Format-with-LATTE-Tools/Process_Transform_Result_SFA_3D_Dataset/3D_Labelling_Result/"

NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration = "/home/ofel04/latte/app/test_dataset/8_drive_0000_sync/"


NAME_FOLDER_3D_Labelling_Result_Data_From_Bag = "/media/ofel04/T7/3D_Labelling_Result_from_Bag_Files_All_Rosbag_Data/"

NAME_FOLDER_3D_Labelling_Result_Image_Sets = "/media/ofel04/T7/3D_Labelling_Result_from_Bag_Files_All_Rosbag_Data/ImageSets/"

NAME_FOLDER_3D_Labelling_Result_Training_Folder = "/media/ofel04/T7/3D_Labelling_Result_from_Bag_Files_All_Rosbag_Data/training/"

NAME_FOLDER_3D_Labelling_Result_Testing_Folder = "/media/ofel04/T7/3D_Labelling_Result_from_Bag_Files_All_Rosbag_Data/testing/"

NAME_OF_LIST_3D_LABELLING_RESULT_RESULT = [ "/home/ofel04/latte/app/test_dataset/8_drive_0000_sync/output/",
                                           "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_0/output/" ,
                                           "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_1/output/" ,
                                           "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_2/output/" ,
                                           "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_3/output/" ,
                                           "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_4/output/" ,
                                           "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_5/output/" ,
                                           "/media/ofel04/T7/data_from_bag_For_Hyundai_Race_6/output/" ,
                                           ]

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Data_From_Bag )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Image_Sets )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" )


os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "velodyne/" )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "image_2/" )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "calib/" )

os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "label_2/" )


Number_of_Labelling_Result_Rosbag_Data = 0

Number_of_Labelling_Result_3D_Bounding_Box_Transformed = 0

if NAME_OF_LIST_3D_LABELLING_RESULT_RESULT != [] :

    for Name_of_Folder_3D_Labelling_Result_Result in NAME_OF_LIST_3D_LABELLING_RESULT_RESULT :

        NAME_FOLDER_3D_Labelling_Result = Name_of_Folder_3D_Labelling_Result_Result.replace( "/output/" , "") + "/3D_Labelling_Result/"

        NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration = Name_of_Folder_3D_Labelling_Result_Result.replace( "/output/" , "/" )

        #NAME_FOLDER_3D_Labelling_Result_Data_From_Bag = Name_of_Folder_3D_Labelling_Result_Result.replace( "/output/" , "" ) + "/Result_of_Labelling_Rosbag_Hyundai/"

        #NAME_FOLDER_3D_Labelling_Result_Image_Sets = NAME_FOLDER_3D_Labelling_Result_Data_From_Bag + "ImageSets/"

        #NAME_FOLDER_3D_Labelling_Result_Training_Folder = NAME_FOLDER_3D_Labelling_Result_Data_From_Bag + "training/"

        #NAME_FOLDER_3D_Labelling_Result_Testing_Folder = NAME_FOLDER_3D_Labelling_Result_Data_From_Bag + 'testing/'

        print( 'Making SFA 3D Dataset Bounding Box Labelling for 3D Bounding Box Labelling Rosbag : ' + str( Name_of_Folder_3D_Labelling_Result_Result ) )


        #os.system( "sudo rm -r {}/*".format( NAME_FOLDER_3D_Labelling_Result_Data_From_Bag ))
        #try :
        #    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Data_From_Bag )
        #except :
        #    print( 'Didnt Make Labelling Result 3D Bounding Box Rosbag Hyundai Dataset' )

        """

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Image_Sets )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "velodyne/" )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "image_2/" )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "calib/" )

        os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "label_2/" )

        """

        #Number_of_Labelling_Result_3D_Bounding_Box_Transformed = 0

        for Data_Labelling_Result_3D_Bounding_Box_SFA_3D in sorted( os.listdir( NAME_FOLDER_3D_Labelling_Result )) :

            if int( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) ) >= 2500 :

                continue

            #Data_Labelling_Result_3D_Bounding_Box_SFA_3D = Data_Labelling_Result_3D_Bounding_Box_SFA_3D[ 1 : ]

            if Data_Labelling_Result_3D_Bounding_Box_SFA_3D.find( ".txt" ) != -1 :

                Number_of_Data_Labelling_Result_3D_Bounding_Box_SFA_3D = len( open( NAME_FOLDER_3D_Labelling_Result + Data_Labelling_Result_3D_Bounding_Box_SFA_3D ).readlines() )

                if Number_of_Data_Labelling_Result_3D_Bounding_Box_SFA_3D <= 0 and Number_of_Data_Labelling_Result_3D_Bounding_Box_SFA_3D <= 0 :

                    continue

                    # Make 3D Labelling Result SFA 3D into Folder Testing 3D Labelling Result SFA 3D

                    if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" ) == False :

                        os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" )

                    f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" , "a+" )

                    f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                    f.close()

                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                                                    NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "velodyne/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" )) ) )

                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                                                    NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "image_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" )) ) )
                    
                    os.system( "sudo cp {} {}".format( "000000.txt" ,
                                                    NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "calib/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ) ) )
                    
                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                                                    NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "label_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".txt" )) ) )
                    
                    print( "Making Labelling Result 3D Bounding Box SFA 3D Dataset : " + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ))

                else :

                    Number_of_Labelling_Result_3D_Bounding_Box_Transformed = Number_of_Labelling_Result_3D_Bounding_Box_Transformed + 1


                    if Number_of_Labelling_Result_3D_Bounding_Box_Transformed % 5 <= 3 :

                        # Make 3D Labelling Result SFA 3D into Folder Training 3D Labelling Result SFA 3D

                        if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "train.txt" ) == False :

                            os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "train.txt" )

                        f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "train.txt" , "a+" )

                        #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                        f.writelines( str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + "\n" )

                        f.close()

                        if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" ) == False :

                            os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" )

                        f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" , "a+" )

                        #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                        f.writelines( str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed).zfill( 6 ) + "\n" )

                        f.close()

                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                        #                                NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" )) ) )

                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                                                        NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" + ( str( ( Number_of_Labelling_Result_3D_Bounding_Box_Transformed)).zfill( 6 ) + ".bin").replace( ".txt" , ".bin" )) ) 
                        
                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                        #                                NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" )) ) )
                        
                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                                                        NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" + (str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed).zfill( 6 ) + ".png").replace( ".txt" , ".png" )) ) 
                        
                        #os.system( "sudo cp {} {}".format( "000000.txt" ,
                        #                                NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ) ) )
                        
                        os.system( "sudo cp {} {}".format( "000000.txt" ,
                                                        NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" + str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + ".txt" ) ) 
                        
                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                        #                                NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".txt" )) ) )
                        
                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                                                        NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" + str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + ".txt"))
                        
                        print( "Making Labelling Result 3D Bounding Box SFA 3D Dataset : " + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ))

                    elif Number_of_Labelling_Result_3D_Bounding_Box_Transformed % 5 >= 4 :

                        if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" ) == False :

                            os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" )

                        f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" , "a+" )

                        #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                        f.writelines( str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + "\n" )

                        f.close()

                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                        #                                NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "velodyne/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" )) ) )

                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                                                        NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "velodyne/" + ( str( ( Number_of_Labelling_Result_3D_Bounding_Box_Transformed)).zfill( 6 ) + ".bin").replace( ".txt" , ".bin" )) ) 
                        

                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                        #                                NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "image_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" )) ) )
                        
                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                                                        NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "image_2/" + (str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed).zfill( 6 ) + ".png").replace( ".txt" , ".png" )) ) 
                        
                        #os.system( "sudo cp {} {}".format( "000000.txt" ,
                        #                                NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "calib/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ) ) )
                        
                        os.system( "sudo cp {} {}".format( "000000.txt" ,
                                                        NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "calib/" + str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + ".txt" ) ) 

                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                        #                                NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "label_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".txt" )) ) )
                        
                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                                                        NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "label_2/" + str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + ".txt"))

                        print( "Making Labelling Result 3D Bounding Box SFA 3D Dataset : " + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ))
                        

                        # Make 3D Labelling Result SFA 3D into Folder Validation 3D Labelling Result SFA 3D

                        if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "val.txt" ) == False :

                            os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "val.txt" )

                        f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "val.txt" , "a+" )

                        #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                        f.writelines( str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + "\n" )

                        f.close()

                        #if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" ) == False :

                        #    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" )

                        f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" , "a+" )

                        #f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                        f.writelines( str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + "\n" )

                        f.close()

                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                        #                                NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" )) ) )

                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                                                        NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" + ( str( ( Number_of_Labelling_Result_3D_Bounding_Box_Transformed)).zfill( 6 ) + ".bin").replace( ".txt" , ".bin" )) ) 

                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                        #                                NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" )) ) )
                        
                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                                                        NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" + (str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed).zfill( 6 ) + ".png").replace( ".txt" , ".png" )) ) 

                        #os.system( "sudo cp {} {}".format( "000000.txt" ,
                        #                                NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ) ) )
                        
                        os.system( "sudo cp {} {}".format( "000000.txt" ,
                                                        NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" + str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + ".txt" ) ) 

                        #os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                        #                                NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".txt" )) ) )
                        
                        os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                                                        NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" + str( Number_of_Labelling_Result_3D_Bounding_Box_Transformed ).zfill( 6 ) + ".txt"))
                        print( "Making Labelling Result 3D Bounding Box SFA 3D Dataset : " + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ))


else :
        
    os.system( "sudo rm -r {}/*".format( NAME_FOLDER_3D_Labelling_Result_Data_From_Bag ))

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Image_Sets )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "velodyne/" )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "image_2/" )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "calib/" )

    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "label_2/" )



    Number_of_Labelling_Result_3D_Bounding_Box_Transformed = 0

    for Data_Labelling_Result_3D_Bounding_Box_SFA_3D in sorted( os.listdir( NAME_FOLDER_3D_Labelling_Result )) :

        if int( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) ) >= 1201 :

            continue

        #Data_Labelling_Result_3D_Bounding_Box_SFA_3D = Data_Labelling_Result_3D_Bounding_Box_SFA_3D[ 1 : ]

        if Data_Labelling_Result_3D_Bounding_Box_SFA_3D.find( ".txt" ) != -1 :

            Number_of_Data_Labelling_Result_3D_Bounding_Box_SFA_3D = len( open( NAME_FOLDER_3D_Labelling_Result + Data_Labelling_Result_3D_Bounding_Box_SFA_3D ).readlines() )

            if Number_of_Data_Labelling_Result_3D_Bounding_Box_SFA_3D <= 2 and Number_of_Data_Labelling_Result_3D_Bounding_Box_SFA_3D <= 2 :

                continue

                # Make 3D Labelling Result SFA 3D into Folder Testing 3D Labelling Result SFA 3D

                if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" ) == False :

                    os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" )

                f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" , "a+" )

                f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                f.close()

                os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                                                NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "velodyne/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" )) ) )

                os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                                                NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "image_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" )) ) )
                
                os.system( "sudo cp {} {}".format( "000000.txt" ,
                                                NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "calib/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ) ) )
                
                os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                                                NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "label_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".txt" )) ) )
                
                print( "Making Labelling Result 3D Bounding Box SFA 3D Dataset : " + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ))

            else :

                Number_of_Labelling_Result_3D_Bounding_Box_Transformed = Number_of_Labelling_Result_3D_Bounding_Box_Transformed + 1

                if Number_of_Labelling_Result_3D_Bounding_Box_Transformed % 5 <= 3 :

                    # Make 3D Labelling Result SFA 3D into Folder Training 3D Labelling Result SFA 3D

                    if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "train.txt" ) == False :

                        os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "train.txt" )

                    f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "train.txt" , "a+" )

                    f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                    f.close()

                    if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" ) == False :

                        os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" )

                    f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" , "a+" )

                    f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                    f.close()

                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                                                    NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" )) ) )

                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                                                    NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" )) ) )
                    
                    os.system( "sudo cp {} {}".format( "000000.txt" ,
                                                    NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ) ) )
                    
                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                                                    NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".txt" )) ) )
                    
                    print( "Making Labelling Result 3D Bounding Box SFA 3D Dataset : " + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ))

                elif Number_of_Labelling_Result_3D_Bounding_Box_Transformed % 5 >= 4 :

                    if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" ) == False :

                        os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" )

                    f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "test.txt" , "a+" )

                    f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                    f.close()

                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                                                    NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "velodyne/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" )) ) )

                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                                                    NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "image_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" )) ) )
                    
                    os.system( "sudo cp {} {}".format( "000000.txt" ,
                                                    NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "calib/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ) ) )
                    
                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                                                    NAME_FOLDER_3D_Labelling_Result_Testing_Folder + "label_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".txt" )) ) )
                    
                    print( "Making Labelling Result 3D Bounding Box SFA 3D Dataset : " + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ))
                    

                    # Make 3D Labelling Result SFA 3D into Folder Validation 3D Labelling Result SFA 3D

                    if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "val.txt" ) == False :

                        os.system( "sudo touch " + NAME_FOLDER_3D_Labelling_Result_Image_Sets + "val.txt" )

                    f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "val.txt" , "a+" )

                    f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                    f.close()

                    #if os.path.exists( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" ) == False :

                    #    os.mkdir( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" )

                    f = open( NAME_FOLDER_3D_Labelling_Result_Image_Sets + "trainval.txt" , "a+" )

                    f.writelines( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , "" ) + "\n" )

                    f.close()

                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "bin_data/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" ) ),
                                                    NAME_FOLDER_3D_Labelling_Result_Training_Folder + "velodyne/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".bin" )) ) )

                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration + "image/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" ) ),
                                                    NAME_FOLDER_3D_Labelling_Result_Training_Folder + "image_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".png" )) ) )
                    
                    os.system( "sudo cp {} {}".format( "000000.txt" ,
                                                    NAME_FOLDER_3D_Labelling_Result_Training_Folder + "calib/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ) ) )
                    
                    os.system( "sudo cp {} {}".format( NAME_FOLDER_3D_Labelling_Result + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D),
                                                    NAME_FOLDER_3D_Labelling_Result_Training_Folder + "label_2/" + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D.replace( ".txt" , ".txt" )) ) )
                    
                    print( "Making Labelling Result 3D Bounding Box SFA 3D Dataset : " + str( Data_Labelling_Result_3D_Bounding_Box_SFA_3D ))



            


            