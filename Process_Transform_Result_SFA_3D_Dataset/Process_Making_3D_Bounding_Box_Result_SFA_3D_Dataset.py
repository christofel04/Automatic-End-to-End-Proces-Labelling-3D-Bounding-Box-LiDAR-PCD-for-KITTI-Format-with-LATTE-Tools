import os

NAME_FOLDER_3D_Labelling_Result = "/home/ofel04/Automatic-End-to-End-Proces-Labelling-3D-Bounding-Box-LiDAR-PCD-for-KITTI-Format-with-LATTE-Tools/Process_Transform_Result_SFA_3D_Dataset/3D_Labelling_Result/"

NAME_FOLDER_3D_Labelling_Image_Velodyne_Calibration = "/home/ofel04/latte/app/test_dataset/8_drive_0000_sync/"

NAME_FOLDER_3D_Labelling_Result_Data_From_Bag = "./3D_Labelling_Result_from_Bag_Files/"

NAME_FOLDER_3D_Labelling_Result_Image_Sets = "./3D_Labelling_Result_from_Bag_Files/ImageSets/"

NAME_FOLDER_3D_Labelling_Result_Training_Folder = "./3D_Labelling_Result_from_Bag_Files/training/"

NAME_FOLDER_3D_Labelling_Result_Testing_Folder = "./3D_Labelling_Result_from_Bag_Files/testing/"

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



            


            