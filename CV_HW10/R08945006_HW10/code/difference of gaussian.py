#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
np.set_printoptions(threshold=np.inf)


# In[2]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float64)
#防止overfitting
afterDOG_img = np.zeros([512,512])
afterzerocrossing_img = np.zeros([512,512])


# In[3]:


def DOG(img,threshold):
    kernal = [[-1,-3,-4,-6,-7,-8,-7,-6,-4,-3,-1],
              [-3,-5,-8,-11,-13,-13,-13,-11,-8,-5,-3],
              [-4,-8,-12,-16,-17,-17,-17,-16,-12,-8,-4],
              [-6,-11,-16,-16,0,15,0,-16,-16,-11,-6],
              [-7,-13,-17,0,85,160,85,0,-17,-13,-8],
              [-8,-13,-17,15,160,283,160,15,-17,-13,-8],
              [-7,-13,-17,0,85,160,85,0,-17,-13,-8],
              [-6,-11,-16,-16,0,15,0,-16,-16,-11,-6],
              [-4,-8,-12,-16,-17,-17,-17,-16,-12,-8,-4],
              [-3,-5,-8,-11,-13,-13,-13,-11,-8,-5,-3],
              [-1,-3,-4,-6,-7,-8,-7,-6,-4,-3,-1],
             ]
    
    for row in range(5,507):
        for col in range(5,507):
            matrix = img[row-5:row+6,col-5:col+6]
            temp = matrix * kernal
            #print(matrix)
            #print(kernal)
            #print(temp)
            value = sum(sum(temp))
            #print(value)
            
            if value > 0 and value >= threshold:
                afterDOG_img[row][col] = 1
                value = 0
            elif value < 0 and value <= threshold:
                afterDOG_img[row][col] = -1
                value = 0
            else:
                afterDOG_img[row][col] = 0 
                value = 0
                
    return afterDOG_img         

def zerocrossing(afterDOG_img):
    for row in range(5,507):
        for col in range(5,507):
            if afterDOG_img[row][col] == 1:
                temp_matrix = afterDOG_img[row-5:row+6,col-5:col+6]
                finded = False
                for i in range(11):
                    for j in range(11):
                        if temp_matrix[i][j] == -1:
                            finded = True
                            break
                if finded == True:            
                    afterzerocrossing_img[row][col] = 0
                else:
                    afterzerocrossing_img[row][col] = 255
            else:
                afterzerocrossing_img[row][col] = 255
                
    return afterzerocrossing_img


# In[4]:


afterDOG_img = DOG(img,1)
#print(afterDOG_img)

final_img = zerocrossing(afterDOG_img)
cv2.imshow('final_img',final_img)
cv2.waitKey()


# In[5]:


cv2.imwrite('difference_of_gaussian.bmp',final_img)


# In[ ]:





# In[ ]:




