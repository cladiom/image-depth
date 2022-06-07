import os
import sys
import numpy as np
import cv2
import pyrgbd

def sum_column(matrix, column):
    total = 0
    for row in range(len(matrix)):
        total += abs(matrix[row][column])
    return total

def calculate(image):
    depth_image = cv2.imread(image, -1)  # 16bit short
    #depth_image = cv2.bitwise_not(depth_image)
    #cv2.imshow("window", depth_image);
    #cv2.waitKey(0);

    fx, fy, cx, cy = 500, 500, 300, 300 # initial camera parameters

    point_cloud = pyrgbd.my_depth2pc(depth_image, fx, fy, cx, cy)

    #Export 3D representation
    #pyrgbd.util.write_pc_ply_txt("{}.ply".format(image), point_cloud)

    z_values_sum = sum_column(point_cloud, 2)
    #print("{}".format(image), z_values_sum)

    return z_values_sum 

if __name__ == '__main__':
	print("Starting Volume Calculation...")

	#calculate_2('Z25777766_Depth.png', 'Z25777766Leer_Depth.png')
	
	volume_depth_1 = calculate('Z25777766_Depth.png')
	volume_depth_leer_1 = calculate('Z25777766Leer_Depth.png')
	volume_1 = volume_depth_1 - volume_depth_leer_1
	print("Calculated Volume of Object 1 is", volume_1)

	volume_depth_1_inverted = calculate('Z25777766_Depth_inverted.png')
	volume_depth_leer_1_inverted = calculate('Z25777766Leer_Depth_inverted.png')
	volume_1_inverted = volume_depth_1_inverted - volume_depth_leer_1_inverted
	print("Calculated Volume of Object 1 inverted is", volume_1_inverted)

	volume_depth_2 = calculate('Z25777783_Depth.png')
	volume_depth_leer_2 = calculate('Z25777783Leer_Depth.png')
	volume_2 = volume_depth_2 - volume_depth_leer_2
	print("Calculated Volume of Object 2 is", volume_2)

	volume_depth_2_inverted = calculate('Z25777783_Depth_inverted.png')
	volume_depth_leer_2_inverted = calculate('Z25777783Leer_Depth_inverted.png')
	volume_2_inverted = volume_depth_2_inverted - volume_depth_leer_2_inverted
	print("Calculated Volume of Object 2 inverted is", volume_2_inverted)

	volume_depth_3 = calculate('Z25777796_Depth.png')
	volume_depth_leer_3 = calculate('Z25777796Leer_Depth.png')
	volume_3 = volume_depth_3 - volume_depth_leer_3
	print("Calculated Volume of Object 3 is", volume_3)

	volume_depth_3_inverted = calculate('Z25777796_Depth_inverted.png')
	volume_depth_leer_3_inverted = calculate('Z25777796Leer_Depth_inverted.png')
	volume_3_inverted = volume_depth_3_inverted - volume_depth_leer_3_inverted
	print("Calculated Volume of Object 3 inverted is", volume_3_inverted)

	print("Question: What are their ratios?")
	print("Ratio between Z25777783 and Z25777766:", volume_depth_2_inverted/volume_depth_1_inverted)
	print("Ratio between Z25777796 and Z25777766:", volume_depth_3_inverted/volume_depth_1_inverted)
	print("Ratio between Z25777796 and Z25777783:", volume_depth_3_inverted/volume_depth_2_inverted)
