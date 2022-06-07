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


def Frei(paddingimg, threshold):
    shape = np.shape(paddingimg)
    new_img = np.zeros([shape[0]-2,shape[1]-2])
    
    for row in range(0, shape[0]-2):
        for col in range(0, shape[1]-2):
            
            f1 = (paddingimg[row+2][col] + ((2**(0.5))*paddingimg[row+2][col+1]) + paddingimg[row+2][col+2]) - (paddingimg[row][col] + ((2**(0.5))*paddingimg[row][col+1]) + paddingimg[row][col+2])
            
            f2 = (paddingimg[row][col+2] + ((2**(0.5))*paddingimg[row+1][col+2]) + paddingimg[row+2][col+2]) - (paddingimg[row][col] + ((2**(0.5))*paddingimg[row+1][col]) + paddingimg[row+2][col])
            
            
            gradient = ((f1**(2)) + (f2**(2)))**(0.5)
            
            if gradient > threshold:
                new_img[row][col] = 0
            else:
                new_img[row][col] = 255
            
            
    return new_img


# In[4]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
paddingimg = expand_padding(img)
paddingimg = paddingimg.astype(np.uint8)
new_img = Frei(paddingimg, 30)


# In[5]:


cv2.imshow('new_img',new_img)
cv2.waitKey(0)


# In[6]:


cv2.imwrite('Frei_t30.bmp',new_img)


# In[ ]:





# In[ ]:




