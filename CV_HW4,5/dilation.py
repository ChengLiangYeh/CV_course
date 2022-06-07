import cv2
import numpy as np 

img = cv2.imread('binarylena.bmp',cv2.IMREAD_GRAYSCALE)
print(img.shape)

newimg = np.zeros([512,512])
print(newimg.shape)

kernal = np.zeros((5,5))
#print(kernal)
kernal[0][0] = 2
kernal[0][4] = 2 
kernal[4][0] = 2
kernal[4][4] = 2
print(kernal) #真正在做不管2的位置，應該是空集合

for row in range(len(img)):
    

