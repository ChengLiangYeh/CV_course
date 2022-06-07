import numpy as np
np.set_printoptions(threshold=np.inf)
import cv2

def loadimageingrayscale():
    img = cv2.imread('binarylena.bmp',cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img',img)
    cv2.waitKey()
    cv2.destroyAllWindows() 
    return img


img  = loadimageingrayscale()
#print(np.shape(img))
print(img)

#kernal
kernal = np.ones([5,5])
kernal[0][0]=0
kernal[0][4]=0
kernal[4][0]=0
kernal[4][4]=0
print(kernal)


list1 = [-1,0,1]
list2 = [-2,-1,0,1,2]
#dilation
for row in range(2,510):
    for col in range(2,510):
        if img[row][col] == 255:
            for item in list1:
                img[row-2][col+item] = 255
            for item in list2:
                img[row-1][col+item] = 255
                img[row][col+item] = 255
                img[row+1][col+item] = 255
            for item in list1:
                img[row+2][col+item] = 255
                
#cv2.imshow('img',img)
#cv2.waitKey()
#cv2.destroyAllWindows() 

print(img)
