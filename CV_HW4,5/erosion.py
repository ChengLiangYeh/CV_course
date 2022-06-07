import numpy as np
import cv2

img = cv2.imread('binarylena.bmp',cv2.IMREAD_GRAYSCALE)

erosionimg = img
for row in range(2):
    for col in range(512):
        erosionimg[row][col] = 0
for row in range(510,512):
    for col in range(512):
        erosionimg[row][col] = 0
for col in range(2):
    for row in range(512):
        erosionimg[row][col] = 0
for col in range(510,512):
    for row in range(512):
        erosionimg[row][col] = 0

def erosion():
    list1 = [-1,0,1]
    list2 = [-2,-1,0,1,2]
    error = 0

    for row in range(2,510):
        for col in range(2,510):
            if img[row][col] == 255:
                for item in list1:
                    if img[row-2][col+item] != 255:  
                        error = 1
                    if img[row+2][col+item] != 255:
                        error = 1
                for item in list2:
                    if img[row-1][col+item] !=255:
                        erroe = 1 
                    if img[row][col+item] !=255:
                        error = 1
                    if img[row+1][col+item] !=255:
                        error = 1
                if error == 1: 
                    erosionimg[row][col] = 0
                    error = 0

    cv2.imshow('erosionimg',erosionimg)
    cv2.waitKey()
                        

erosion()
                    
                
                