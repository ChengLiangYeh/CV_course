#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import cv2


# In[29]:


img = cv2.imread('lena.bmp')
cv2.imshow('lena',img)
cv2.waitKey(0)


# In[30]:


#轉 90度


# In[31]:


st = np.zeros([512,512,3])


for i in range(3):
    for k in range(512):
        for j in range(512):
            st[k][abs(j-511)][i] = img[j][k][i]
        


# In[32]:


cv2.imwrite('new_img.bmp',st)
new_img = cv2.imread('new_img.bmp')
cv2.imshow('new_img',new_img)
cv2.waitKey(0)


# In[33]:


#上下顛倒 


# In[34]:


st2 = np.zeros([512,512,3])

for a in range(3):
    for b in range(512):
        for c in range(512):
            st2[c][b][a] = st[abs(c-511)][b][a]
            


# In[35]:


cv2.imwrite('new_img2.bmp',st2)
new_img2 = cv2.imread('new_img2.bmp')
cv2.imshow('new_img2', new_img2)
cv2.waitKey(0)


# In[ ]:




