#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
np.set_printoptions(threshold=np.inf)


# In[2]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float64)
#防止overfitting
afterlaplacian_img = np.zeros([512,512])
afterzerocrossing_img = np.zeros([512,512])


# In[3]:


def laplacian(img, threshold):
    for row in range(1,511):
        for col in range(1,511):
            value = img[row-1][col] + img[row+1][col] + img[row][col-1] + img[row][col+1] + (-4 * img[row][col])
            #overfit
            #print('img[row-1][col]=',img[row-1][col])
            #print('img[row+1][col]=',img[row+1][col])
            #print('img[row][col-1]=',img[row][col-1])
            #print('img[row][col+1]=',img[row][col+1])
            #print('img[row][col]=',img[row][col])
            #print('value=',value)
            
            if value > 0 and value >= threshold:
                afterlaplacian_img[row][col] = 1
                value = 0
            elif value < 0 and value <= threshold:
                afterlaplacian_img[row][col] = -1
                value = 0
            else:
                afterlaplacian_img[row][col] = 0 
                value = 0
    return afterlaplacian_img

def laplacian2(img, threshold):
    for row in range(1,511):
        for col in range(1,511):
            value = img[row-1][col] + img[row-1][col-1] + img[row-1][col+1] + img[row+1][col] + img[row+1][col+1] + img[row+1][col-1] + img[row][col-1] + img[row][col+1] + (-8 * img[row][col])
            value = value / 3
            #overfit
            #print('img[row-1][col]=',img[row-1][col])
            #print('img[row+1][col]=',img[row+1][col])
            #print('img[row][col-1]=',img[row][col-1])
            #print('img[row][col+1]=',img[row][col+1])
            #print('img[row][col]=',img[row][col])
            #print('value=',value)
            
            if value > 0 and value >= threshold:
                afterlaplacian_img[row][col] = 1
                value = 0
            elif value < 0 and value <= threshold:
                afterlaplacian_img[row][col] = -1
                value = 0
            else:
                afterlaplacian_img[row][col] = 0 
                value = 0
    return afterlaplacian_img

def mini_var_laplacian(img, threshold):
    for row in range(1,511):
        for col in range(1,511):
            value = -1*img[row-1][col] + 2*img[row-1][col-1] + 2*img[row-1][col+1] + -1*img[row+1][col] + 2*img[row+1][col+1] + 2*img[row+1][col-1] + -1*img[row][col-1] + -1*img[row][col+1] + (-4 * img[row][col])
            value = value / 3
            #overfit
            #print('img[row-1][col]=',img[row-1][col])
            #print('img[row+1][col]=',img[row+1][col])
            #print('img[row][col-1]=',img[row][col-1])
            #print('img[row][col+1]=',img[row][col+1])
            #print('img[row][col]=',img[row][col])
            #print('value=',value)
            
            if value > 0 and value >= threshold:
                afterlaplacian_img[row][col] = 1
                value = 0
            elif value < 0 and value <= threshold:
                afterlaplacian_img[row][col] = -1
                value = 0
            else:
                afterlaplacian_img[row][col] = 0 
                value = 0
    return afterlaplacian_img

def zerocrossing(afterlaplacian_img):
    for row in range(1,511):
        for col in range(1,511):
            if afterlaplacian_img[row][col] == 1:
                if afterlaplacian_img[row-1,col-1] == -1 or afterlaplacian_img[row-1,col] == -1 or afterlaplacian_img[row-1,col+1] == -1 or afterlaplacian_img[row+1,col-1] == -1 or afterlaplacian_img[row+1,col] == -1 or afterlaplacian_img[row+1,col+1] == -1 or afterlaplacian_img[row][col-1] == -1 or afterlaplacian_img[row][col+1] == -1:
                    afterzerocrossing_img[row][col] = 0
            else:
                afterzerocrossing_img[row][col] = 255
                
    return afterzerocrossing_img


# In[4]:


afterlaplacian_img = mini_var_laplacian(img, 20)
#print(afterlaplacian_img)
final_img = zerocrossing(afterlaplacian_img)


# In[5]:


print(final_img)


# In[6]:


cv2.imshow('final_img',final_img)
cv2.waitKey()


# In[7]:


cv2.imwrite('mini_var_laplacian.bmp',final_img)


# In[ ]:




