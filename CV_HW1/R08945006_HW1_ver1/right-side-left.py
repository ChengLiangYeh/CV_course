#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


img = cv2.imread('lena.bmp')
cv2.imshow('lena.bmp',img)
cv2.waitKey(0)

np.shape(img)


# In[3]:


#create a storage tensor
st = np.zeros([512,512,3])
np.shape(st)


# In[4]:


for i in range(3):                               #channel
    for j in range(512):                         #row
        for k in range(512):                     #column
            st[j][k][i] = img[j][abs(k-512+1)][i]

cv2.imwrite('new_img.bmp',st)
new_img = cv2.imread('new_img.bmp')
cv2.imshow('new_img',new_img)
cv2.waitKey(0)


# In[ ]:




