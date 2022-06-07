#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def get_imgsize(img):
    shape = np.shape(img)
    return shape            
            
def padding(img):
    shape = get_imgsize(img) 
    paddingimg = np.zeros([shape[0]+2,shape[1]+2]) 
    for row in range(shape[0]):
        for col in range(shape[1]):
            paddingimg[row+1][col+1] = img[row][col]
    return paddingimg

def medianfilter(img,kernalsize):
    imgsize = np.shape(img)
    newimg = np.zeros([imgsize[0],imgsize[1]])
    if kernalsize == 3:
        paddingimg = padding(img)
    if kernalsize == 5:
        paddingimg = padding(img)
        paddingimg = padding(paddingimg)  #double padding because of kernal size = 5*5
    for row in range(imgsize[0]):
        for col in range(imgsize[1]):
            if kernalsize == 3:
                temp = np.zeros([3,3])
                temp[0:3,0:3] = (paddingimg[row:row+kernalsize,col:col+kernalsize])
                templist = np.zeros(9)
                for i in range(3):
                    for j in range(3):
                        if i == 0:
                            templist[j] = temp[i][j]
                        elif i == 1:
                            templist[j+3] = temp[i][j]
                        else:
                            templist[j+6] = temp[i][j]
                templist = np.sort(templist)
                #print('median number=', templist[4])
                newimg[row][col] = templist[4]
                
            if kernalsize == 5:
                temp = np.zeros([5,5])
                temp[0:5,0:5] = (paddingimg[row:row+kernalsize,col:col+kernalsize])
                templist = np.zeros(25)
                for i in range(5):
                    for j in range(5):
                        if i == 0:
                            templist[j] = temp[i][j]
                        elif i == 1:
                            templist[j+5] = temp[i][j]
                        elif i == 2:
                            templist[j+10] = temp[i][j]
                        elif i == 3:
                            templist[j+15] = temp[i][j]
                        else:
                            templist[j+20] = temp[i][j]
                templist = np.sort(templist)
                newimg[row][col] = templist[12]
    newimg = newimg.astype(np.uint8)
    return newimg


# In[3]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
aftermedianfilterimg = medianfilter(img,5)  #kernal size 可用 3*3 or 5*5


# In[4]:


cv2.imshow('aftermedianfilterimg',aftermedianfilterimg)
cv2.waitKey(0)


# In[5]:


cv2.imwrite('after5medianfilterlena.bmp',aftermedianfilterimg)


# In[ ]:





# In[ ]:





# In[6]:


'''
#test
img = np.zeros([5,5])
img[0][0] = 1
img[1][1] = 2
img[2][2] = 3
img[3][3] = 4 
img[4][4] = 5
img[0][2] = 7
img[1][2] = 10
print(img)
img = padding(img)
print(img)
print('--------------------------')
for row in range(5):
    for col in range(5):
        temp = np.zeros([3,3])
        temp[0:3,0:3] = img[row:row+3,col:col+3]
        templist = np.zeros(9)
        print(temp)
        print('--------------------------')
        for i in range(3):
            for j in range(3):
                if i == 0:
                    templist[j] = temp[i][j]
                elif i == 1:
                    templist[j+3] = temp[i][j]
                else:
                    templist[j+6] = temp[i][j]
        print(templist)
        templist = np.sort(templist)
        print(templist)
        print('median number=', templist[4])
        
        
        #print(temp)
        #print('-------------')
        #print(np.sort(temp))
        #print('-------------')
        #print(np.sort(np.sort(temp),axis = 0))
#這樣排完max在右下角，靠北不是找最大值阿，是找中位數...
'''

