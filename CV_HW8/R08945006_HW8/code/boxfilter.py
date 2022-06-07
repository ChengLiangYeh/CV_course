#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def boxfilter(img,kernalsize):
    imgsize = np.shape(img)
    newimg = np.zeros([imgsize[0],imgsize[1]])
    if kernalsize == 3:
        paddingimg = padding(img)
    if kernalsize == 5:
        paddingimg = padding(img)
        paddingimg = padding(paddingimg)  #double padding because of kernal size = 5*5
    for row in range(imgsize[0]):
        for col in range(imgsize[1]):
            if kernalsize == 3:
                temp = (sum(sum(paddingimg[row:row+kernalsize,col:col+kernalsize])))/9
                newimg[row][col] = temp
            if kernalsize == 5:
                temp = (sum(sum(paddingimg[row:row+kernalsize,col:col+kernalsize])))/25
                newimg[row][col] = temp
    newimg = newimg.astype(np.uint8)
    return newimg

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


img = cv2.imread('salt_and_pepper_p0.1_img.bmp',cv2.IMREAD_GRAYSCALE)
afterboxfilterimg = boxfilter(img,5)  #kernal size 可用 3*3 or 5*5


# In[4]:


cv2.imshow('afterboxfilterimg',afterboxfilterimg)
cv2.waitKey(0)


# In[5]:


cv2.imwrite('SP0.1_afterboxfilterimg_kernalsize5.bmp',afterboxfilterimg)


# In[ ]:





# In[ ]:




