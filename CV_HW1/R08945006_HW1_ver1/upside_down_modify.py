#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


img = cv2.imread('lena.bmp')
cv2.imshow('lena.bmp',img)
cv2.waitKey(0)


# In[3]:


st = np.zeros([512,512,3])


# In[4]:


for j in range(3):
    for i in range(512):
        for k in range(512):
            st[i][k][j] = img[abs(i-512+1)][k][j]


# In[5]:


cv2.imwrite('new_image.bmp', st)

new_image = cv2.imread('new_image.bmp')

cv2.imshow('new_image',new_image)

cv2.waitKey(0)


# In[ ]:




