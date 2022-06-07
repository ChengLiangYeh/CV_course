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
        new_img[row+1][513] = img[row][511]
    
    for col in range(shape[0]):
        new_img[0][col+1] = img[0][col]
        new_img[513][col+1] = img[511][col]

    new_img[0][0] = img[0][0]
    new_img[0][513] = img[0][511]
    new_img[513][0] = img[511][0]
    new_img[513][513] = img[511][511]
    
    return(new_img)

#往外padding一層，值為內層拓展出去


# In[3]:


def Prewitt(paddingimg, threshold):
    shape = np.shape(paddingimg)
    new_img = np.zeros([shape[0]-2,shape[1]-2])
    #print(np.shape(new_img))
    
    for row in range(0, shape[0]-2):
        for col in range(0, shape[1]-2):
            #print('row=',row)
            #print('col=',col)
            p1 = (sum(paddingimg[row+2,col:col+3])) - (sum(paddingimg[row,col:col+3]))
            #print('paddingimg[row+2,col:col+3]=',paddingimg[row+2,col:col+3])
            #print('sum=',sum(paddingimg[row+2,col:col+3]))
            #print('paddingimg[row,col:col+3]=',paddingimg[row,col:col+3])
            #print('sum=',sum(paddingimg[row,col:col+3]))
            #print('p1=',p1)
            
            p2 = (sum(paddingimg[row:row+3,col+2])) - (sum(paddingimg[row:row+3,col]))
            #print('paddingimg[row:row+3,col+2]=',paddingimg[row:row+3,col+2])
            #print('sum=',sum(paddingimg[row:row+3,col+2]))
            #print('paddingimg[row:row+3,col]',paddingimg[row:row+3,col])
            #print('sum=',sum(paddingimg[row:row+3,col]))
            #print('p2=',p2)
            
            gradient = ((p1**(2)) + (p2**(2)))**(0.5)
            #print('gradient=',gradient)
            
            if gradient > threshold:
                new_img[row][col] = 0
            else:
                new_img[row][col] = 255
            #print(new_img[row][col])
            
    return new_img


# In[4]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
paddingimg = expand_padding(img)
paddingimg = paddingimg.astype(np.uint8)
new_img = Prewitt(paddingimg, 24)


# In[5]:


cv2.imshow('new_img',new_img)
cv2.waitKey(0)


# In[7]:


cv2.imwrite('Prewitt_t24.bmp',new_img)
#講義結果圖有錯!


# In[ ]:




