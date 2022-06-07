#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def Robert(img, threshold):
    shape = np.shape(img)
    new_img = np.zeros([shape[0],shape[1]])
    
    for row in range(shape[0]-1):
        for col in range(shape[1]-1):
            r1 = -1*(img[row][col]) + (img[row+1][col+1])
            
            #print('img[row][col]=',img[row][col])
            #print('-(img[row][col])=',-(img[row][col]))
            #抓到BUG -> 不可以直接這樣寫負號
            
            r2 = -1*(img[row][col+1]) + (img[row+1][col])
            gradient = ((r1**(2)) + (r2**(2)))**(0.5)
            if gradient > threshold:
                new_img[row][col] = 0
            else:
                new_img[row][col] = 255
    return new_img
                


# In[3]:


img = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
new_img = Robert(img, 30)


# In[4]:


cv2.imshow('new_img',new_img)
cv2.waitKey(0)


# In[5]:


cv2.imwrite('Robert_t30_img.bmp',new_img)


# In[ ]:


#講義給的結果是threshold=30的，但是他的threshold打12...

