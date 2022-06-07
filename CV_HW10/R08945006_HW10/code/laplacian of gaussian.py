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
afterLOG_img = np.zeros([512,512])
afterzerocrossing_img = np.zeros([512,512])


# In[3]:


def LOG(img,threshold):
    kernal = [[0,0,0,-1,-1,-2,-1,-1,0,0,0],
              [0,0,-2,-4,-8,-9,-8,-4,-2,0,0],
              [0,-2,-7,-15,-22,-23,-22,-15,-7,-2,0],
              [-1,-4,-15,-24,-14,-1,-14,-24,-15,-4,-1],
              [-1,-8,-22,-14,52,103,52,-14,-22,-8,-1],
              [-2,-9,-23,-1,103,178,103,-1,-23,-9,-2],
              [-1,-8,-22,-14,52,103,52,-14,-22,-8,-1],
              [-1,-4,-15,-24,-14,-1,-14,-24,-15,-4,-1],
              [0,-2,-7,-15,-22,-23,-22,-15,-7,-2,0],
              [0,0,-2,-4,-8,-9,-8,-4,-2,0,0],
              [0,0,0,-1,-1,-2,-1,-1,0,0,0]
             ]
    
    for row in range(5,507):
        for col in range(5,507):
            matrix = img[row-5:row+6,col-5:col+6]
            temp = matrix * kernal
            value = sum(sum(temp))
            
            if value > 0 and value >= threshold:
                afterLOG_img[row][col] = 1
                value = 0
            elif value < 0 and value <= threshold:
                afterLOG_img[row][col] = -1
                value = 0
            else:
                afterLOG_img[row][col] = 0 
                value = 0
                
    return afterLOG_img         

def zerocrossing(afterLOG_img):
    for row in range(5,507):
        for col in range(5,507):
            if afterLOG_img[row][col] == 1:
                temp_matrix = afterLOG_img[row-5:row+6,col-5:col+6]
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
                
    return afterzerocrossing_img


# In[4]:


afterLOG_img = LOG(img,3000)


# In[5]:


final_img = zerocrossing(afterLOG_img)


# In[6]:


cv2.imshow('final_img',final_img)
cv2.waitKey()


# In[7]:


cv2.imwrite('laplacian_of_gaussian.bmp',final_img)


# In[ ]:




