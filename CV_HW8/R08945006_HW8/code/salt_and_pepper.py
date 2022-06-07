#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import random


# In[2]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
shape = np.shape(img)


# In[3]:


def salt_and_pepper(img, probability):
    for row in range(shape[0]):
        for col in range(shape[1]):
            temp = random.uniform(0,1)
            if temp < probability:
                img[row][col] = 0
            elif temp > 1 - probability:
                img[row][col] = 255
            else:
                img[row][col] = img[row][col]
    return img


# In[4]:


salt_and_pepper_img = salt_and_pepper(img, 0.05)
cv2.imshow('salt_and_pepper_img',salt_and_pepper_img)
cv2.waitKey()


# In[5]:


cv2.imwrite('salt_and_pepper_p0.05_img.bmp', salt_and_pepper_img)


# In[ ]:




