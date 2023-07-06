import os

import json

import math

def Change_Angle_Label_SE_SSD_To_Rotation_Y_Label_SE_SSD( Angle_Lable_SE_SSD ):
    
    while abs(Angle_Lable_SE_SSD) > 2*math.pi :
        
        if Angle_Lable_SE_SSD >0 :
            
            Angle_Lable_SE_SSD = Angle_Lable_SE_SSD - math.pi
        
        elif Angle_Lable_SE_SSD < 0 :
            
            Angle_Lable_SE_SSD = Angle_Lable_SE_SSD + math.pi
            
    if abs( Angle_Lable_SE_SSD ) > math.pi :

        if Angle_Lable_SE_SSD > 0 :        
        
            Angle_Lable_SE_SSD = Angle_Lable_SE_SSD - 2*math.pi
            
        elif Angle_Lable_SE_SSD <= 0 :
            
            Angle_Lable_SE_SSD = Angle_Lable_SE_SSD + 2*math.pi
            
    if Angle_Lable_SE_SSD > 0 :
        
        Angle_Lable_SE_SSD = 1* math.pi - Angle_Lable_SE_SSD
        
    elif Angle_Lable_SE_SSD <= 0 :
        
        Angle_Lable_SE_SSD = -1*( math.pi - ( ( -1 )* Angle_Lable_SE_SSD))
            
    return Angle_Lable_SE_SSD

def change_Label_Bounding_Box_Width_Heigh_Upper_Cars( Label_Bounding_Box , Height_New_Label_Length , Height_New_Width ):
    
    Bounding_Box_Back_Edge = ( Label_Bounding_Box[ 'center' ]['x'] - math.cos( 2* math.pi - Label_Bounding_Box[ 'angle' ])*Label_Bounding_Box[ 'length' ]* 0.5 ,
                              Label_Bounding_Box[ 'center' ]['y'] - math.sin( 2* math.pi - Label_Bounding_Box[ 'angle' ])*Label_Bounding_Box[ 'length' ]* 0.5 )
    
    Label_Bounding_Box[ 'length' ] = Height_New_Label_Length 
    
    Label_Bounding_Box_After_Transformation = ( Bounding_Box_Back_Edge[ 0 ] + math.cos( 2* math.pi - Label_Bounding_Box[ 'angle' ])*Label_Bounding_Box[ 'length' ]* 0.5 ,
                            Bounding_Box_Back_Edge[ 1 ] + math.sin( 2* math.pi - Label_Bounding_Box[ 'angle' ])*Label_Bounding_Box[ 'length' ]* 0.5 )
    

    return Label_Bounding_Box_After_Transformation

def change_Label_Bounding_Box_Width_Heigh_Below_Cars( Label_Bounding_Box , Height_New_Label_Length , Height_New_Width ):
    
    Bounding_Box_Back_Edge = ( Label_Bounding_Box[ 'center' ]['x'] + math.cos( 2* math.pi - Label_Bounding_Box[ 'angle' ])*Label_Bounding_Box[ 'length' ]* 0.5 ,
                              Label_Bounding_Box[ 'center' ]['y'] + math.sin( 2* math.pi - Label_Bounding_Box[ 'angle' ])*Label_Bounding_Box[ 'length' ]* 0.5 )
    
    Label_Bounding_Box[ 'length' ] = Height_New_Label_Length 
    
    Label_Bounding_Box_After_Transformation = ( Bounding_Box_Back_Edge[ 0 ] - math.cos( 2* math.pi - Label_Bounding_Box[ 'angle' ])*Label_Bounding_Box[ 'length' ]* 0.5 ,
                            Bounding_Box_Back_Edge[ 1 ] - math.sin( 2* math.pi - Label_Bounding_Box[ 'angle' ])*Label_Bounding_Box[ 'length' ]* 0.5 )
    

    return Label_Bounding_Box_After_Transformation


NAME_OF_3D_LABELLING_RESULT_RESULT = "./7_drive_0080_sync/"

NAME_OF_3D_LABELLING_RESULT_OUTPUT = "./3D_Labelling_Result/"

if os.path.exists( NAME_OF_3D_LABELLING_RESULT_OUTPUT )== False :
    
    os.mkdir( NAME_OF_3D_LABELLING_RESULT_OUTPUT )

for Result_of_3D_Labelling in sorted( os.listdir( NAME_OF_3D_LABELLING_RESULT_RESULT ) ) :
    
    if Result_of_3D_Labelling.find( ".json" ) != -1 :
        
        # Opening JSON file
        f = open( os.path.join( NAME_OF_3D_LABELLING_RESULT_RESULT , Result_of_3D_Labelling ) )#'data.json')
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        data = list( data[ "frame" ][ "bounding_boxes" ] )
    
        f.close()
        
        f = open( os.path.join( NAME_OF_3D_LABELLING_RESULT_OUTPUT , str("0") + Result_of_3D_Labelling.replace( ".json" , ".txt" ) ) , "w+" )
        
        for Result_3D_Labelling_Bounding_Box_Result in data :
            
            Number_of_Bounding_Box = 0 
            
            if Result_3D_Labelling_Bounding_Box_Result[ "box_id" ] <= 100 or Result_3D_Labelling_Bounding_Box_Result[ "box_id" ] >= 0 :
                
                Number_of_Bounding_Box = Number_of_Bounding_Box + 1 
                
                if Result_3D_Labelling_Bounding_Box_Result[ "length" ] > 2 :
                    
                    Result_3D_Labelling_Bounding_Box_Result[ "length" ] = 2
                    
                if Result_3D_Labelling_Bounding_Box_Result[ "width" ] > 5 :
                    
                    Result_3D_Labelling_Bounding_Box_Result[ "width" ] = 5
                    
                #Result_3D_Labelling_Bounding_Box_Result[ "length" ] = 4
                
                #Result_3D_Labelling_Bounding_Box_Result[ "width" ] = 2
                
                '''
                if Number_of_Bounding_Box <= 2 :
                
                    ( Result_3D_Labelling_Bounding_Box_Result[ 'center' ][ 'x' ] , Result_3D_Labelling_Bounding_Box_Result[ 'center' ][ 'y' ] ) = change_Label_Bounding_Box_Width_Heigh_Upper_Cars( Result_3D_Labelling_Bounding_Box_Result , 4 , 2 )
                
                elif Number_of_Bounding_Box >= 3 :
                    
                    ( Result_3D_Labelling_Bounding_Box_Result[ 'center' ][ 'x' ] , Result_3D_Labelling_Bounding_Box_Result[ 'center' ][ 'y' ] ) = change_Label_Bounding_Box_Width_Heigh_Below_Cars( Result_3D_Labelling_Bounding_Box_Result , 4 , 2 )
                '''
                 
                   
                f.write( "Car 0.0 0 0"  + " -100 -100 -100 -100 " + "2 " + str( Result_3D_Labelling_Bounding_Box_Result[ "length" ] ) + " " + str( Result_3D_Labelling_Bounding_Box_Result[ "width" ] ) + " " + str( -1* Result_3D_Labelling_Bounding_Box_Result[ "center" ][ "y" ]) + " " + "1.7" + " " + str( Result_3D_Labelling_Bounding_Box_Result[ "center" ][ "x" ] ) + " "  + str( Change_Angle_Label_SE_SSD_To_Rotation_Y_Label_SE_SSD(  float( Result_3D_Labelling_Bounding_Box_Result[ "angle" ] ) + 0.5* math.pi ) ) + "\n" )
                
        f.close()
        
        print( "Print Result Output 3D Labelling Result " + str( Result_of_3D_Labelling ) )
        
        

