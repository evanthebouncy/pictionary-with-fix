# Describe_Page_01.jpg	Describe_Page_11.jpg	modify_Page_09.jpg
# Describe_Page_02.jpg	Describe_Page_12.jpg	modify_Page_10.jpg
# Describe_Page_03.jpg	modify_Page_01.jpg	modify_Page_11.jpg
# Describe_Page_04.jpg	modify_Page_02.jpg	modify_Page_12.jpg
# Describe_Page_05.jpg	modify_Page_03.jpg	modify_Page_13.jpg
# Describe_Page_06.jpg	modify_Page_04.jpg	modify_Page_14.jpg
# Describe_Page_07.jpg	modify_Page_05.jpg	modify_Page_15.jpg
# Describe_Page_08.jpg	modify_Page_06.jpg	modify_Page_16.jpg
# Describe_Page_09.jpg	modify_Page_07.jpg
# Describe_Page_10.jpg	modify_Page_08.jpg

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# process the describe ones first
modify_files = ['Describe_Page_01.jpg', 'Describe_Page_02.jpg', 'Describe_Page_03.jpg', 'Describe_Page_04.jpg', 'Describe_Page_05.jpg', 'Describe_Page_06.jpg', 'Describe_Page_07.jpg', 'Describe_Page_08.jpg', 'Describe_Page_09.jpg', 'Describe_Page_10.jpg', 'Describe_Page_11.jpg', 'Describe_Page_12.jpg']
# process the modify ones
modify_files = ['modify_Page_01.jpg', 'modify_Page_02.jpg', 'modify_Page_03.jpg', 'modify_Page_04.jpg', 'modify_Page_05.jpg', 'modify_Page_06.jpg', 'modify_Page_07.jpg', 'modify_Page_08.jpg', 'modify_Page_09.jpg', 'modify_Page_10.jpg', 'modify_Page_11.jpg', 'modify_Page_12.jpg', 'modify_Page_13.jpg', 'modify_Page_14.jpg', 'modify_Page_15.jpg', 'modify_Page_16.jpg']

input_path = 'assets/raw/'
for idx, file_name in enumerate(modify_files):
    print(file_name)
    file_path = os.path.join(input_path, file_name)
    img = cv2.imread(file_path)
    # crop out the top 10% and bottom 10% of the image
    height, width, channels = img.shape
    img = img[int(height*0.1):int(height*0.9), 0:width]
    height, width, channels = img.shape

    # split the image into 4 sub-regions, upper-left, upper-right, lower-left, lower-right
    # but give the sub-region some slack, so they can overlap a little bit
    # each sub-region should be 55% of the original image
    img_ul = img[0:int(height*0.55), 0:int(width*0.55)]
    img_ur = img[0:int(height*0.55), int(width*0.45):width]
    img_ll = img[int(height*0.45):height, 0:int(width*0.55)]
    img_lr = img[int(height*0.45):height, int(width*0.45):width]

    # save the sub-regions to /assets/telephone-mod
    # output_path = 'assets/telephone-mod/'
    # cv2.imwrite(os.path.join(output_path, str(idx) + '_describe.jpg'), img_ul)
    # cv2.imwrite(os.path.join(output_path, str(idx) + '_draw1.jpg'), img_ur)
    # cv2.imwrite(os.path.join(output_path, str(idx) + '_modify.jpg'), img_ll)
    # cv2.imwrite(os.path.join(output_path, str(idx) + '_draw2.jpg'), img_lr)

    output_path = 'assets/telephone/'
    # cv2.imwrite(os.path.join(output_path, str(idx) + '_describe.jpg'), img_ul)
    cv2.imwrite(os.path.join(output_path, str(idx) + '_describe.jpg'), img_ur)
    # cv2.imwrite(os.path.join(output_path, str(idx) + '_modify.jpg'), img_ll)
    cv2.imwrite(os.path.join(output_path, str(idx) + '_draw.jpg'), img_lr)


