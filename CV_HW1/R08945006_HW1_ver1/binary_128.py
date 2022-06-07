#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import cv2


# In[3]:


img = cv2.imread('lena.bmp')


# In[4]:


threshold = 128 

for i in range(3):
    for j in range(512):
        for k in range(512):
            if img[k][j][i] < threshold:
                img[k][j][i] = 0
            else:
                img[k][j][i] = 255
                


# In[6]:


cv2.imshow('lena',img)
cv2.waitKey(0)

cv2.imwrite('binarylena.bmp',img)


# In[ ]:




