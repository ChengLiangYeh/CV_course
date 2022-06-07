#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import math


# In[2]:


def normalize(img):
    newimg = np.zeros([len(img),len(img)])
    for row in range(len(img)):
        for col in range(len(img)):
            newimg[row][col] = (img[row][col])/255
            #img = img.astype(np.uint8)
    return newimg
#check ok


# In[3]:


def us(img):
    sum = 0
    for row in range(len(img)):
        for col in range(len(img)):
            sum = sum + (img[row][col])
            us = sum / ((len(img))**(2))
    return us


# In[4]:


def VS(img, us):
    sum = 0
    for row in range(len(img)):
        for col in range(len(img)):
            sum = sum + (img[row][col] - us)**2
            vs = sum / ((len(img))**(2))
    return vs


# In[5]:


def un(noiseimg,img):
    sum = 0
    for row in range(len(img)):
        for col in range(len(img)):
            sum = sum + (noiseimg[row][col] - img[row][col])
            un = sum / ((len(img))**(2))
    return un


# In[6]:


def VN(noiseimg,img,un):
    sum = 0
    for row in range(len(img)):
        for col in range(len(img)):
            sum = sum + ((noiseimg[row][col] - img[row][col] - un)**(2))
            vn = sum / ((len(img))**(2))
    return vn


# In[7]:


def SNR(vs,vn):
    SNR = 0
    temp = ((vs)**0.5) / ((vn)**0.5)
    temp = math.log(temp,10)
    SNR = temp * 20
    return SNR


# In[8]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
noiseimg = cv2.imread('SP0.1_aftermedianfilterimg_kernalsize5.bmp',cv2.IMREAD_GRAYSCALE)
normalize_img = normalize(img)
normalize_noiseimg = normalize(noiseimg)


us = us(normalize_img)
vs = VS(normalize_img,us)
un = un(normalize_noiseimg,normalize_img)
vn = VN(normalize_noiseimg,normalize_img,un)
SNR = SNR(vs,vn)


# In[9]:


print(SNR) #答對啦~~~~~~~~~~~~~~~~~~~~~~~~~~~
SNR = str(SNR)


# In[10]:


# 開啟檔案
file = open("SNR.txt", "a")
# 寫入 This is a testing! 到檔案
file.write("SP0.1_aftermedianfilterimg_kernalsize5_SNR=")
file.write(SNR)
file.write('\n')
# 關閉檔案
file.close()


# In[ ]:





# In[ ]:




