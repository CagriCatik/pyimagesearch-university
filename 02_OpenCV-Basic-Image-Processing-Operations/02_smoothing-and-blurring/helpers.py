# import the necessary packages
import os, shutil
import numpy as np
import cv2 

def createFolder(process_folder):

    os.chdir(process_folder)

    path = "./images_solution"

    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

    print("Existence check or remove the existing solution folder")

    os.mkdir(path)


def get_concat_v(im1, im2):
    concatenate_horizontal = np.concatenate((im1, im2), axis=0) 
    return concatenate_horizontal

def get_concat_h(im1, im2, im3, im4):
    concatenate_vertical = np.concatenate((im1,im2,im3, im4), axis=1) 
    return concatenate_vertical

