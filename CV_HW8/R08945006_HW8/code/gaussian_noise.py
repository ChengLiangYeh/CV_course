#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import random


# In[2]:


def get_imgsize(img):
    shape = np.shape(img)
    return shape

def padding(img):
    shape = get_imgsize(img) 
    paddingimg = np.zeros([shape[0]+2,shape[1]+2]) 
    for row in range(shape[0]):
        for col in range(shape[1]):
            paddingimg[row+1][col+1] = img[row][col]
    return paddingimg


# In[3]:


def gaussian_noise(img, amp):
    noiseimg = np.zeros([512,512])
    for row in range(len(img)):
        for col in range(len(img)):
            tem = 0
            tem = img[row][col] + amp * random.gauss(0, 1)
            if tem > 255:
                tem = 255
            elif tem < 0:
                tem = 0
            noiseimg[row][col] = tem
    return noiseimg
    


# In[4]:


img = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
noiseimg = gaussian_noise(img,10)
noiseimg = noiseimg.astype(np.uint8)


# In[5]:


cv2.imshow('noiseimg',noiseimg)
cv2.waitKey()


# In[6]:


cv2.imwrite('gaussian_noise_10.bmp',noiseimg)


# In[ ]:





# In[ ]:





# In[ ]:




