#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def expand_padding(img):
    shape = np.shape(img)
    new_img = np.zeros([shape[0]+2, shape[1]+2])
    for row in range(shape[0]):
        for col in range(shape[1]):
            new_img[row+1][col+1] = img[row][col]
            
    for row in range(shape[0]):
        new_img[row+1][0] = img[row][0]
        new_img[row+1][shape[0]+1] = img[row][shape[0]-1]
    
    for col in range(shape[0]):
        new_img[0][col+1] = img[0][col]
        new_img[shape[0]+1][col+1] = img[shape[0]-1][col]

    new_img[0][0] = img[0][0]
    new_img[0][shape[0]+1] = img[0][shape[0]-1]
    new_img[shape[0]+1][0] = img[shape[0]-1][0]
    new_img[shape[0]+1][shape[0]+1] = img[shape[0]-1][shape[0]-1]
    
    return(new_img)


# In[3]:


def Nevatia(paddingimg, threshold):
    shape = np.shape(paddingimg)
    new_img = np.zeros([shape[0]-4,shape[1]-4])
    
    paddingimg = paddingimg.astype(np.float64)
    
    kernal0 = [[100,100,100,100,100],
               [100,100,100,100,100],
               [0,0,0,0,0],
               [-100,-100,-100,-100,-100],
               [-100,-100,-100,-100,-100]]
    kernal0 = np.asarray(kernal0)
    
    kernal30 = [[100,100,100,100,100],
                [100,100,100,78,-32],
                [100,92,0,-92,-100],
                [32,-78,-100,-100,-100],
                [-100,-100,-100,-100,-100]]
    kernal30 = np.asarray(kernal30)
    
    kernal60 = [[100,100,100,32,-100],
                [100,100,92,-78,-100],
                [100,100,0,-100,-100],
                [100,78,-92,-100,-100],
                [100,-32,-100,-100,-100]]
    kernal60 = np.asarray(kernal60)
    
    kernalminus90 = [[-100,-100,0,-100,-100],
                    [-100,-100,0,100,100],
                    [-100,-100,0,100,100],
                    [-100,-100,0,100,100],
                    [-100,-100,0,100,100]]
    kernalminus90 = np.asarray(kernalminus90)
    
    kernalminus60 = [[-100,32,100,100,100],
                    [-100,-78,92,100,100],
                    [-100,-100,0,100,100],
                    [-100,-100,-92,78,100],
                    [-100,-100,-100,-32,100]]
    kernalminus60 = np.asarray(kernalminus60)
    
    kernalminus30 = [[100,100,100,100,100],
                    [-32,78,100,100,100],
                    [-100,-92,0,92,100],
                    [-100,-100,-100,-78,32],
                    [-100,-100,-100,-100,-100]]
    kernalminus30 = np.asarray(kernalminus30)
    
    for row in range(0, shape[0]-4):
        for col in range(0, shape[1]-4):
            
            paddingimg[row:row+5,col:col+5]
            
            N0 = sum(sum(paddingimg[row:row+5,col:col+5] * kernal0))
            N30 = sum(sum(paddingimg[row:row+5,col:col+5] * kernal30))
            N60 = sum(sum(paddingimg[row:row+5,col:col+5] * kernal60))
            Nminus90 = sum(sum(paddingimg[row:row+5,col:col+5] * kernalminus90))
            Nminus60 = sum(sum(paddingimg[row:row+5,col:col+5] * kernalminus60))
            Nminus30 = sum(sum(paddingimg[row:row+5,col:col+5] * kernalminus30))
            
            gradientlist = [N0,N30,N60,Nminus90,Nminus60,Nminus30]
            #print(gradientlist)
            gradient = max(gradientlist)
            #print(gradient)
            if gradient > threshold:
                new_img[row][col] = 0
            else:
                new_img[row][col] = 255
    return new_img


# In[4]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
paddingimg = expand_padding(img)
paddingimg = expand_padding(paddingimg)
paddingimg = paddingimg.astype(np.uint8)
new_img = Nevatia(paddingimg, 12500)


# In[7]:


cv2.imshow('new_img',new_img)
cv2.waitKey(0)


# In[8]:


cv2.imwrite('Nevatia_t12500.bmp',new_img)


# In[ ]:


#之前在作業8時使用的處理方式，是操作row,col，如img[row:row+2,col:col+3]這種方式。缺點:碰到kernal中長的不太規則很痛苦，要一個一個寫。解法如下:
#在作業9，此時使用矩陣方式做處理，直接寫出kernal，用numpy做處理。

