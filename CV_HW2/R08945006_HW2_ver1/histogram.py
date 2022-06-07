#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt


# In[51]:


img = cv2.imread('lena.bmp')

index = np.zeros([256])

for i in range(512):
    for j in range(512):
        a = img[j][i][0]
        index[a] = index[a] + 1
        
x = np.zeros([256])       # x軸從0~255
for i in range(256):
    x[i] = i
    
y = index

plt.bar(x, y, label = 'bars1')

plt.xlabel("gray value")

plt.ylabel("number")

plt.title("histogram")

plt.show()


# In[ ]:





# In[ ]:




