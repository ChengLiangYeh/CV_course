#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


img = cv2.imread('lena.bmp')

#List = ['img_r','img_g','img_b']

img_r = np.zeros([512,512,1])

for j in range(512):
    for k in range(512):
        img_r[k][j][0] = img[k][j][0]
        
img_g = np.zeros([512,512,1])

for j in range(512):
    for k in range(512):
        img_g[k][j][0] = img[k][j][1]

img_b = np.zeros([512,512,1])

for j in range(512):
    for k in range(512):
        img_b[k][j][0] = img[k][j][2]


# In[3]:


h = 512
w = 512
center = (h/2,w/2)
angle = 315
scale = 0.7


M = cv2.getRotationMatrix2D(center, angle, scale)
rotated45_r = cv2.warpAffine(img_r, M, (w, h))

M = cv2.getRotationMatrix2D(center, angle, scale)
rotated45_g = cv2.warpAffine(img_g, M, (w, h))

M = cv2.getRotationMatrix2D(center, angle, scale)
rotated45_b = cv2.warpAffine(img_b, M, (w, h))

threechannel = np.zeros([512,512,3])

rotated45_r = np.expand_dims(rotated45_r, axis=2)

rotated45_g = np.expand_dims(rotated45_r, axis=2)

rotated45_b = np.expand_dims(rotated45_r, axis=2)

for i in range(512):
    for j in range(512):
        threechannel[i][j][0] = rotated45_r[i][j][0]

for i in range(512):
    for j in range(512):
        threechannel[i][j][1] = rotated45_g[i][j][0]
        
for i in range(512):
    for j in range(512):
        threechannel[i][j][2] = rotated45_b[i][j][0]


# In[4]:


cv2.imwrite('img_rotated45.bmp',threechannel)
img_rotated45 = cv2.imread('img_rotated45.bmp')
cv2.imshow('img_rotated45',img_rotated45)
cv2.waitKey(0)


# In[9]:


#非常粗糙的寫法
#回去看看有沒有可能把r g b 寫成for迴圈, 或是試試看可不可以直接rotate3D,不然先轉成rgb再一張一張旋轉很麻煩,之後還要拼回去成3D...
#旋轉那邊scale也是很粗糙,為了怕切到而調整,但是不是剛好切齊...


# In[ ]:




