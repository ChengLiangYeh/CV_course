#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread('intensity_divided3_img.bmp',cv2.IMREAD_GRAYSCALE)
cv2.imshow('intensity_divided3_img',img)
cv2.waitKey(0)
#print(img)


# In[3]:


index = np.zeros([256])
for row in range(512):
    for column in range(512):
        grayvalue = img[row][column]
        index[grayvalue] = index[grayvalue] + 1
#print(index)

cdf = np.zeros([256])
for i in range(256):
    if i == 0:
        cdf[i] = index[i]
        tem = index[i]
    else:
        tem = tem + index[i] 
        cdf[i] = tem
          


# In[4]:


index_2 = np.zeros([256]) #轉換表: index是o~255 灰階 , value是指轉換後的灰階值

for i in range(256):
     index_2[i] = int(round(((cdf[i] - 1) / 262143) * 255))
print(index_2)


# In[5]:


print(img)

for i in range(512):
    for j in range(512):
        value = img[i][j]
        img[i][j] = index_2[value]
print(img)


# In[6]:


cv2.imwrite('equal_img.bmp', img)
equal_img = cv2.imread('equal_img.bmp')
cv2.imshow('equal_img',equal_img)
cv2.waitKey(0)


# In[7]:


index = np.zeros([256])

for row in range(512):
    for column in range(512):
        value = equal_img[row][column]
        index[value] = index[value] + 1
        
        
x = np.zeros([256])     
for i in range(256):
    x[i] = i
    
y = index

plt.bar(x, y, label = 'bars1')

plt.xlabel("gray value")

plt.ylabel("number")

plt.title("histogram")

plt.savefig('equal_img_Histogram.png')

plt.show()



# In[ ]:




