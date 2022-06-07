#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def expand_padding(img):
    shape = np.shape(img)
    new_img = np.zeros([shape[0]+2, shape[1]+2])
    for row in range(shape[0]):
        for col in range(shape[1]):
            new_img[row+1][col+1] = img[row][col]
            
    for row in range(shape[0]):
        new_img[row+1][0] = img[row][0]
        new_img[row+1][513] = img[row][511]
    
    for col in range(shape[0]):
        new_img[0][col+1] = img[0][col]
        new_img[513][col+1] = img[511][col]

    new_img[0][0] = img[0][0]
    new_img[0][513] = img[0][511]
    new_img[513][0] = img[511][0]
    new_img[513][513] = img[511][511]
    
    return(new_img)


# In[3]:


def Robinson(paddingimg, threshold):
    shape = np.shape(paddingimg)
    new_img = np.zeros([shape[0]-2,shape[1]-2])
    
    #防止overflow
    paddingimg = paddingimg.astype(np.float64)
    #print(paddingimg)
    
    for row in range(0, shape[0]-2):
        for col in range(0, shape[1]-2):
            
            r0 = (paddingimg[row][col+2] + 2*paddingimg[row+1][col+2] + paddingimg[row+2][col+2]) - (paddingimg[row][col] + 2*paddingimg[row+1][col] + paddingimg[row+2][col])          
            r1 = (2*paddingimg[row][col+2] + paddingimg[row+1][col+2] + paddingimg[row][col+1]) - (paddingimg[row+2][col+1] + paddingimg[row+1][col] + 2*paddingimg[row+2][col])
            r2 = (paddingimg[row][col] + 2*paddingimg[row][col+1] + paddingimg[row][col+2]) - (paddingimg[row+2][col] + 2*paddingimg[row+2][col+1] + paddingimg[row+2][col+2])  
            r3 = (2*paddingimg[row][col] + paddingimg[row][col+1] + paddingimg[row+1][col]) - (paddingimg[row+2][col+1] + paddingimg[row+2][col+1] + 2*paddingimg[row+2][col+2])  
            r4 = (paddingimg[row][col] + 2*paddingimg[row+1][col] + paddingimg[row+2][col]) - (paddingimg[row][col+2] + 2*paddingimg[row+1][col+2] + paddingimg[row+2][col+2])  
            r5 = (paddingimg[row+2][col+1] + paddingimg[row+1][col] + 2*paddingimg[row+2][col]) - (2*paddingimg[row][col+2] + paddingimg[row+1][col+2] + paddingimg[row][col+1]) 
            r6 = (paddingimg[row+2][col] + 2*paddingimg[row+2][col+1] + paddingimg[row+2][col+2]) - (paddingimg[row][col] + 2*paddingimg[row][col+1] + paddingimg[row][col+2]) 
            r7 = (2*paddingimg[row+2][col+2] + paddingimg[row+2][col+1] + paddingimg[row+1][col+2]) - (2*paddingimg[row][col] + paddingimg[row][col+1] + paddingimg[row+1][col]) 
            
            
            
            
            gradientlist = [r0,r1,r2,r3,r4,r5,r6,r7]
            #print(gradientlist)
            gradient = max(gradientlist)
            #print(gradient)
            if gradient > threshold:
                new_img[row][col] = 0
            else:
                new_img[row][col] = 255
            
            
    return new_img


# In[4]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
paddingimg = expand_padding(img)
paddingimg = paddingimg.astype(np.uint8)
new_img = Robinson(paddingimg, 43)


# In[5]:


cv2.imshow('new_img',new_img)
cv2.waitKey(0)


# In[6]:


cv2.imwrite('Robinson_t43.bmp',new_img)


# In[ ]:




