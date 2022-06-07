#!/usr/bin/env python
# coding: utf-8

# In[153]:


import numpy as np
import cv2


# In[154]:


def Oimgshow():
    img = cv2.imread('lena.bmp')
    cv2.imshow('img',img)
    cv2.waitKey(0)


# In[155]:


#ratio = input('please input your zoom in/out ratio')
#print('your zoom in/out ratio', ratio) 


# In[156]:


img = cv2.imread('lena.bmp')
np.shape(img)

print(img)


# In[157]:


#test
a = np.random.randint(10, size=(8,8,3))
b = np.zeros([4,8,3])
b2 = np.zeros([4,4,3])

for k in range(3):
    for j in range (8):
        for i in range (0,8,2):
            b[round(i/2)][j][k] = round((a[i][j][k]+a[i+1][j][k])/2) 
            
for k in range(3):
    for j in range (4):
        for i in range (0,8,2):
            b2[j][round(i/2)][k] = round((b[j][i][k]+b[j][i+1][k])/2) 
            
print(b2)


# In[158]:


#test end -> 用平均法沒問題啊


# In[159]:


#create a tensor 
new_img = np.zeros([256,512,3])

for k in range(3):
    for j in range (512):
        for i in range (0,512,2):
            new_img[round(i/2)][j][k] = round(((img[i][j][k])/2+(img[i+1][j][k])/2)) 
            #會怪怪的原來是因為影像溢位阿(pixel 灰階值只能是0~255!,所以先相加會超過255,因此選擇先除2在相加)
                                              
print(new_img)
    


# In[160]:


new_img2 = np.zeros([256,256,3])

for k in range(3):
    for j in range (256):
        for i in range (0,512,2):
            new_img2[j][round(i/2)][k] = round((new_img[j][i][k])/2 + (new_img[j][i+1][k])/2 ) 
            #column好像沒有溢位的問題,但還是照做一下吧
print(new_img2)


# In[161]:


cv2.imwrite('shrink_lena_in_half.bmp',new_img2)
img = cv2.imread('shrink_lena_in_half.bmp')
cv2.imshow('shrink_lena_in_half',img)
cv2.waitKey(0)


# In[ ]:




