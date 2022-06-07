#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


def loadimageingrayscale():
    
    #擇1 -> opening 也會用到。
    
    #img = cv2.imread('binarylena.bmp',cv2.IMREAD_GRAYSCALE)
    #img = cv2.imread('erosionimg.bmp',cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img',img)
    cv2.waitKey()
    cv2.destroyAllWindows() 
    return img


# In[3]:


img  = loadimageingrayscale()


# In[4]:


list1 = [-1,0,1]          #kernal中最上面和最下面3-3位置
list2 = [-2,-1,0,1,2]     #kernal中5-5-5位置
dilationimg = np.zeros([512,512])  

#由於kernal是3-5-5-5-3，kernal中心在正中間，所以可以不考慮影像上下左右各兩排pixel
for row in range(2):        
    for col in range(512):
        dilationimg[row][col] = img[row][col]
for row in range(510,512):
    for col in range(512):
        dilationimg[row][col] = img[row][col]
for col in range(2):
    for row in range(512):
        dilationimg[row][col] = img[row][col]
for col in range(510,512):
    for row in range(512):
        dilationimg[row][col] = img[row][col]
print(dilationimg)


# In[5]:


#採取逐個pixel取代

for row in range(2,510):      #參考kernal位置相對於整個image位置
    for col in range(2,510):
        if img[row][col] == 255:  
            for item in list1:
                dilationimg[row-2][col+item] = 255
            for item in list2:
                dilationimg[row-1][col+item] = 255
                dilationimg[row][col+item] = 255
                dilationimg[row+1][col+item] = 255
            for item in list1:
                dilationimg[row+2][col+item] = 255


# In[6]:


cv2.imshow('dilationimg',dilationimg)
cv2.waitKey()
cv2.destroyAllWindows() 


# In[7]:


#2擇1
#cv2.imwrite('dilationimg.bmp',dilationimg)
#cv2.imwrite('opening.bmp',dilationimg)


# In[ ]:




