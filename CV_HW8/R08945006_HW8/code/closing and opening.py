#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


#dilation
img = cv2.imread('gaussian_noise_30.bmp',cv2.IMREAD_GRAYSCALE)

list1 = [-1,0,1]          
list2 = [-2,-1,0,1,2]     
dilationimg = np.zeros([512,512]) 

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

comparekernal = np.zeros([5,5])
revisecol = list(range(508))
col = list(range(2,510))
reviserow = list(range(508))
row = list(range(2,510))

for row, reviserow in zip(row, reviserow):     
    revisecol = list(range(508))  
    col = list(range(2,510))      
    for revisecol, col in zip(revisecol, col):
        for item in list1:
            comparekernal[row-2-reviserow][col+item-revisecol] = img[row-2][col+item]
        for item in list2:
            comparekernal[row-1-reviserow][col+item-revisecol] = img[row-1][col+item]
            comparekernal[row-reviserow][col+item-revisecol] = img[row][col+item]
            comparekernal[row+1-reviserow][col+item-revisecol] = img[row+1][col+item]
        for item in list1:
            comparekernal[row+2-reviserow][col+item-revisecol] = img[row+2][col+item]
        
        [x,y] = np.where(comparekernal==np.max(comparekernal))
        x = x.astype('uint8')
        y = y.astype('uint8')
        dilationimg[row][col] = comparekernal[x[0]][y[0]]
        dilationimg = dilationimg.astype('uint8')

#Erosion
img = dilationimg

list1 = [-1,0,1]          
list2 = [-2,-1,0,1,2]     
erosionimg = np.zeros([512,512]) 

for row in range(2):        
    for col in range(512):
        erosionimg[row][col] = img[row][col]
for row in range(510,512):
    for col in range(512):
        erosionimg[row][col] = img[row][col]
for col in range(2):
    for row in range(512):
        erosionimg[row][col] = img[row][col]
for col in range(510,512):
    for row in range(512):
        erosionimg[row][col] = img[row][col]

comparekernal = np.zeros([5,5])
for i in range(5):
    for j in range(5):
        comparekernal[i][j] = 255
revisecol = list(range(508))
col = list(range(2,510))
reviserow = list(range(508))
row = list(range(2,510))

for row, reviserow in zip(row, reviserow):      
    revisecol = list(range(508))  
    col = list(range(2,510))      
    for revisecol, col in zip(revisecol, col):
        for item in list1:
            comparekernal[row-2-reviserow][col+item-revisecol] = img[row-2][col+item]
        for item in list2:
            comparekernal[row-1-reviserow][col+item-revisecol] = img[row-1][col+item]
            comparekernal[row-reviserow][col+item-revisecol] = img[row][col+item]
            comparekernal[row+1-reviserow][col+item-revisecol] = img[row+1][col+item]
        for item in list1:
            comparekernal[row+2-reviserow][col+item-revisecol] = img[row+2][col+item]
            
        [x,y] = np.where(comparekernal==np.min(comparekernal))
        erosionimg[row][col] = comparekernal[x[0]][y[0]]
        erosionimg = erosionimg.astype('uint8')


# In[3]:


#Erosion
img = erosionimg
list1 = [-1,0,1]          
list2 = [-2,-1,0,1,2]     
erosionimg = np.zeros([512,512]) 

for row in range(2):        
    for col in range(512):
        erosionimg[row][col] = img[row][col]
for row in range(510,512):
    for col in range(512):
        erosionimg[row][col] = img[row][col]
for col in range(2):
    for row in range(512):
        erosionimg[row][col] = img[row][col]
for col in range(510,512):
    for row in range(512):
        erosionimg[row][col] = img[row][col]

comparekernal = np.zeros([5,5])
for i in range(5):
    for j in range(5):
        comparekernal[i][j] = 255
revisecol = list(range(508))
col = list(range(2,510))
reviserow = list(range(508))
row = list(range(2,510))

for row, reviserow in zip(row, reviserow):      
    revisecol = list(range(508))  
    col = list(range(2,510))      
    for revisecol, col in zip(revisecol, col):
        for item in list1:
            comparekernal[row-2-reviserow][col+item-revisecol] = img[row-2][col+item]
        for item in list2:
            comparekernal[row-1-reviserow][col+item-revisecol] = img[row-1][col+item]
            comparekernal[row-reviserow][col+item-revisecol] = img[row][col+item]
            comparekernal[row+1-reviserow][col+item-revisecol] = img[row+1][col+item]
        for item in list1:
            comparekernal[row+2-reviserow][col+item-revisecol] = img[row+2][col+item]
            
        [x,y] = np.where(comparekernal==np.min(comparekernal))
        erosionimg[row][col] = comparekernal[x[0]][y[0]]
        erosionimg = erosionimg.astype('uint8')

#dilation
img = erosionimg

list1 = [-1,0,1]          
list2 = [-2,-1,0,1,2]     
dilationimg = np.zeros([512,512]) 

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

comparekernal = np.zeros([5,5])
revisecol = list(range(508))
col = list(range(2,510))
reviserow = list(range(508))
row = list(range(2,510))

for row, reviserow in zip(row, reviserow):     
    revisecol = list(range(508))  
    col = list(range(2,510))      
    for revisecol, col in zip(revisecol, col):
        for item in list1:
            comparekernal[row-2-reviserow][col+item-revisecol] = img[row-2][col+item]
        for item in list2:
            comparekernal[row-1-reviserow][col+item-revisecol] = img[row-1][col+item]
            comparekernal[row-reviserow][col+item-revisecol] = img[row][col+item]
            comparekernal[row+1-reviserow][col+item-revisecol] = img[row+1][col+item]
        for item in list1:
            comparekernal[row+2-reviserow][col+item-revisecol] = img[row+2][col+item]
        
        [x,y] = np.where(comparekernal==np.max(comparekernal))
        x = x.astype('uint8')
        y = y.astype('uint8')
        dilationimg[row][col] = comparekernal[x[0]][y[0]]
        dilationimg = dilationimg.astype('uint8')
        
cv2.imshow('after closing and opening img',dilationimg)
cv2.waitKey()


# In[4]:


cv2.imwrite('G30_after_closing_and_opening_img.bmp',dilationimg)

