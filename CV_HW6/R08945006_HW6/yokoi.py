#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


'''
img = cv2.imread('binarylena.bmp',cv2.IMREAD_GRAYSCALE)

#using 8x8 blocks as a unit,  take the topmost-left pixel as the down-sampled data, Down-sample Lena from 512x512 to 64x64
imgADS = np.zeros([64,64])
img_row = list(range(0,512,8))
img_col = list(range(0,512,8))
imgADS_row = list(range(0,64))
imgADS_col = list(range(0,64))

for img_row, imgADS_row in zip(img_row, imgADS_row):
    img_col = list(range(0,512,8))
    imgADS_col = list(range(0,64))
    for img_col, imgADS_col in zip(img_col, imgADS_col):
        imgADS[imgADS_row][imgADS_col] = img[img_row][img_col]
#手動疊代此block跳過
'''


# In[3]:


imgADS = cv2.imread('iteration6.bmp',cv2.IMREAD_GRAYSCALE) #手動疊代 EX:newiteration(X).bmp
#print(imgADS)
#cv2.imwrite('DSlena.bmp',imgADS)  #手動疊代時不用!，第一次做yokoi用的
#cv2.imshow('imgADS',imgADS)
#cv2.waitKey()


# In[4]:


#padding 
blankimg = np.zeros([66,66])

for row in range(64):
    for col in range(64):
        blankimg[row+1][col+1] = imgADS[row][col]
#print(blankimg)
#print(np.shape(blankimg))
#cv2.imshow('blankimg',blankimg)
#cv2.waitKey()


# In[5]:


#Yokoi
def h(b,c,d,e):
    if b==c:
        if d!=b or e!=b:
            return 'q'
        else:
            return 'r'
    else:
        return 's'
    
totala1 = np.zeros([64,64])
#a1(b,c,d,e)
for row in range(64):
    for col in range(64):
        if blankimg[row+1][col+1] == 255:
            b=blankimg[row+1][col+1]
            c=blankimg[row+1][col+2]
            d=blankimg[row][col+2]
            e=blankimg[row][col+1]

            a1 = h(b,c,d,e)
            if a1 == 'q':
                totala1[row][col]=1
            elif a1 == 'r':
                totala1[row][col]=2
            else:
                totala1[row][col]=3

totala2 = np.zeros([64,64])
#a2(b,c,d,e)
for row in range(64):
    for col in range(64):
        if blankimg[row+1][col+1] == 255:
            b=blankimg[row+1][col+1]
            c=blankimg[row][col+1]
            d=blankimg[row][col]
            e=blankimg[row+1][col]

            a2 = h(b,c,d,e)
            if a2 == 'q':
                totala2[row][col]=1
            elif a2 == 'r':
                totala2[row][col]=2
            else:
                totala2[row][col]=3

totala3 = np.zeros([64,64])
#a3(b,c,d,e)
for row in range(64):
    for col in range(64):
        if blankimg[row+1][col+1] == 255:
            b=blankimg[row+1][col+1]
            c=blankimg[row+1][col]
            d=blankimg[row+2][col]
            e=blankimg[row+2][col+1]

            a3 = h(b,c,d,e)
            if a3 == 'q':
                totala3[row][col]=1
            elif a3 == 'r':
                totala3[row][col]=2
            else:
                totala3[row][col]=3

totala4 = np.zeros([64,64])
#a4(b,c,d,e)
for row in range(64):
    for col in range(64):
        if blankimg[row+1][col+1] == 255:
            b=blankimg[row+1][col+1]
            c=blankimg[row+2][col+1]
            d=blankimg[row+2][col+2]
            e=blankimg[row+1][col+2]

            a4 = h(b,c,d,e)
            if a4 == 'q':
                totala4[row][col]=1
            elif a4 == 'r':
                totala4[row][col]=2
            else:
                totala4[row][col]=3
            

            
        


# In[6]:


finalimg = np.zeros([64,64])
for row in range(64):
    for col in range(64):
        
        q=0
        r=0
        s=0
        
        if totala1[row][col]== 1:
            q = q + 1
        elif totala1[row][col]== 2:
            r = r + 1
        else:
            s = s + 1
            
        if totala2[row][col]== 1:
            q = q + 1
        elif totala2[row][col]== 2:
            r = r + 1
        else:
            s = s + 1
        
        if totala3[row][col]== 1:
            q = q + 1
        elif totala3[row][col]== 2:
            r = r + 1
        else:
            s = s + 1
            
        if totala4[row][col]== 1:
            q = q + 1
        elif totala4[row][col]== 2:
            r = r + 1
        else:
            s = s + 1
            
        #print('a1,a2,a3,a4=',totala1[row][col],totala2[row][col],totala3[row][col],totala4[row][col])
        #print('numbers of q,r,s=',q,r,s)
        
        if q == 1 :
            finalimg[row][col] = 1
        elif q == 2 :
            finalimg[row][col] = 2
        elif q == 3 :
            finalimg[row][col] = 3
        elif q == 4 :
            finalimg[row][col] = 4
        elif r == 4 :
            finalimg[row][col] = 5
        else:
            finalimg[row][col] = 0
        #print('finalimg=',finalimg[row][col])


# In[7]:


np.set_printoptions(threshold=np.inf)
#print(finalimg)


# In[8]:


for row in range(64):
    for col in range(64):
        finalimg[row][col] = int(finalimg[row][col])
np.savetxt('afteriteration6.txt',finalimg)  #疊代手動改名字 EX:afteriteration(X).txt


# In[9]:


'''
#手動疊代不用跑這個block
for row in range(64):
    for col in range(64):
        print(int(finalimg[row][col]), end=' ')
'''


# In[10]:


yokoi = np.loadtxt('matrix.txt')
for row in range(64):
    for col in range(64):
        print(int(yokoi[row][col]), end=' ')


# In[ ]:





# In[ ]:





# In[ ]:




