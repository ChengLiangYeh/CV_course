#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.set_printoptions(threshold=np.inf)
import cv2


# In[2]:


img = cv2.imread('binarylena.bmp',cv2.IMREAD_GRAYSCALE)

#img反白 = imgc
imgc = np.zeros([512,512])

for row in range(512):
    for col in range(512):
        if img[row][col] == 0:
            imgc[row][col] = 255
        else:
            imgc[row][col] = 0
            
cv2.imshow('imgc',imgc)
cv2.waitKey()
cv2.imwrite('imgc.bmp',imgc)


# In[3]:


#A erosion J
erosionimg = np.zeros([512,512])
correct = 0

for row in range(0,511):               
    for col in range(1,512):
        if img[row][col] == 255:
            if img[row][col-1] == 255:
                correct = correct + 1
            if img[row+1][col] == 255:
                correct = correct + 1
                
        if correct == 2: 
            erosionimg[row][col] = 255
            correct = 0
        else:
            erosionimg[row][col] = 0
            correct = 0        
            
cv2.imshow('erosionimg',erosionimg)
cv2.waitKey()


# In[4]:


#Ac erosion K 
#沒有全對的話去掉，有全對的話補上
#kernal中心不包含，要注意!

erosionimgc = np.zeros([512,512])
correct = 0

for row in range(1,512):
    for col in range(0,511):
        if imgc[row][col+1] == 255:
            correct = correct + 1
        if imgc[row-1][col] == 255:
            correct = correct + 1
        if imgc[row-1][col+1] == 255:
            correct = correct + 1
        if correct == 3: 
            erosionimgc[row][col] = 255
            correct = 0
        else:
            erosionimgc[row][col] = 0
            correct = 0          
cv2.imshow('erosionimgc',erosionimgc)
cv2.waitKey()


# In[5]:


#A erosion J和Ac erosion K 兩個結果做交集
#erosionimg 
#erosionimgc
intersection = np.zeros([512,512])

for row in range(512):
    for col in range(512):
        if erosionimg[row][col] == erosionimgc[row][col]:
            intersection[row][col] = erosionimg[row][col]
            


# In[7]:


cv2.imshow('intersection',intersection)
cv2.waitKey()
cv2.imwrite('hitandmiss.bmp',intersection)


# In[ ]:




