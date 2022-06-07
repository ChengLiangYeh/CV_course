#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)

for row in range(512):
    for column in range(512):
        value = img[row][column]
        value = int(round(value/3))
        img[row][column] = value
        
cv2.imwrite('intensity_divided3_img.bmp', img)
intensity_divided3_img = cv2.imread('intensity_divided3_img.bmp')
cv2.imshow('intensity_divided3_img',intensity_divided3_img)
cv2.waitKey(0)


#histogram
index = np.zeros([256])

for row in range(512):
    for column in range(512):
        value = intensity_divided3_img[row][column]
        index[value] = index[value] + 1


x = np.zeros([256])     #x軸
for i in range(256):
    x[i] = i
    
y = index

plt.bar(x, y, label = 'bars1')

plt.xlabel("gray value")

plt.ylabel("number")

plt.title("histogram")

plt.savefig('intensity_divided3_img_histogram.png')

plt.show()

        


# In[5]:





# In[ ]:





# In[ ]:





# In[ ]:




