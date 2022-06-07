#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import cv2
np.set_printoptions(threshold=np.inf)


# In[8]:


#img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
#closing
img = cv2.imread('gray-scale-dilation.bmp',cv2.IMREAD_GRAYSCALE)


# In[9]:


list1 = [-1,0,1]          #kernal中最上面和最下面3-3位置
list2 = [-2,-1,0,1,2]     #kernal中5-5-5位置
erosionimg = np.zeros([512,512]) 
#由於kernal是3-5-5-5-3，kernal中心在正中間，所以可以不考慮影像上下左右各兩排pixel
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
print(erosionimg)


# In[10]:


comparekernal = np.zeros([5,5])
#erosion是找最小值!，kernal不能有0的位置，那就設255
for i in range(5):
    for j in range(5):
        comparekernal[i][j] = 255
revisecol = list(range(508))
col = list(range(2,510))
reviserow = list(range(508))
row = list(range(2,510))

for row, reviserow in zip(row, reviserow):      #參考kernal位置相對於整個image位置
    #print("row, reviserow",row, reviserow)
    revisecol = list(range(508))  #*
    col = list(range(2,510))      #*
    for revisecol, col in zip(revisecol, col):
        #print("col,revisecol",col,revisecol)
        
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

    


# In[11]:


cv2.imshow('erosionimg',erosionimg)
cv2.waitKey()


# In[12]:


#cv2.imwrite('gray-scale-erosion.bmp',erosionimg)
cv2.imwrite('gray-scale-closing.bmp',erosionimg)


# In[ ]:




