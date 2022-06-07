#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)


# In[3]:


index = np.zeros([256])

for row in range(512):
    for column in range(512):
        value = img[row][column]
        index[value] = index[value] + 1


# In[5]:


x = np.zeros([256])     
for i in range(256):
    x[i] = i
    
y = index

plt.bar(x, y, label = 'bars1')

plt.xlabel("gray value")

plt.ylabel("number")

plt.title("histogram")

plt.savefig('Origin_img_Histogram.png')

plt.show()



# In[ ]:




