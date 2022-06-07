#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import cv2
np.set_printoptions(threshold=np.inf)


# In[20]:


#img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
#opening
img = cv2.imread('gray-scale-erosion.bmp',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)
cv2.waitKey()
print(np.shape(img))
print(img)
print(type(img[0][0]))


# In[21]:


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


# In[22]:


#找出Kernal中最大值取代kernal center
comparekernal = np.zeros([5,5])
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
        
        #找出最大值
        [x,y] = np.where(comparekernal==np.max(comparekernal))
        x = x.astype('uint8')
        y = y.astype('uint8')
        dilationimg[row][col] = comparekernal[x[0]][y[0]]
        dilationimg = dilationimg.astype('uint8')
        
        
#print('row,col',row,col)
#print(comparekernal)


# In[23]:


print(dilationimg)
#print(np.shape(dilationimg))
print(type(dilationimg))
cv2.imshow('dilationimg',dilationimg)
cv2.waitKey()


# In[24]:


#cv2.imwrite('gray-scale-dilation.bmp',dilationimg)
#opening
cv2.imwrite('gray-scale-opening.bmp',dilationimg)


# In[ ]:


#以下為test，不用跑


# In[12]:


#data type要轉換
[x,y] = np.where(comparekernal==np.max(comparekernal))
print(type(x[0]))
x = x.astype('uint8')
print(type(x[0]))
print(type(comparekernal[0][0])) #抓!


# In[6]:


#where 出來是矩陣形式，因為可能同時有多個最大值，但我們這邊找一個最大即可
[x,y] = np.where(comparekernal==np.max(comparekernal))
print(comparekernal[x[0]][y[0]])


# In[7]:


#雙變數迴圈
revisecol = list(range(508))
col = list(range(2,510))
for col, revisecol in zip(col, revisecol):
    print(revisecol, col)
    


# In[8]:


#zip 怪洨問題，看上面星號
reviserow = list(range(508))
row = list(range(2,510))
for row, reviserow  in zip(row, reviserow ):
    print(row, reviserow)
    reviserow = list(range(508))
    row = list(range(2,510))
    for row, reviserow  in zip(row, reviserow ):
        print(row, reviserow)
    


# In[ ]:




