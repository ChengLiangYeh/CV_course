#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


#擇一: 做closing會用到。
#img = cv2.imread('binarylena.bmp',cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('dilationimg.bmp',cv2.IMREAD_GRAYSCALE)

erosionimg = np.zeros([512,512])
print(erosionimg)


# In[3]:


list1 = [-1,0,1]      #kernal位置
list2 = [-2,-1,0,1,2]
correct = 0           #統計是否kernal中所有位置都正確填入。


# In[4]:


#逐個pixel進行判定直到掃完整張影像。

for row in range(2,510):        #參考kernal位置
    for col in range(2,510):
        if img[row][col] == 255:
            for item in list1:
                if img[row-2][col+item] == 255:  
                    correct = correct + 1
                if img[row+2][col+item] == 255:
                    correct = correct + 1
            for item in list2:
                if img[row-1][col+item] == 255:
                    correct = correct + 1
                if img[row][col+item] == 255:
                    correct = correct + 1
                if img[row+1][col+item] == 255:
                    correct = correct + 1
            if correct == 21:                      #成功填入則保留
                erosionimg[row][col] = 255
                correct = 0
            else:                                  #失敗則侵蝕掉
                erosionimg[row][col] = 0        
                correct = 0
          


# In[5]:


np.set_printoptions(threshold=np.inf)
print(erosionimg)
cv2.imshow('erosionimg',erosionimg)
cv2.waitKey()


# In[6]:


#cv2.imwrite('erosionimg.bmp',erosionimg)
#cv2.imwrite('closing.bmp',erosionimg)

