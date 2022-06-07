#!/usr/bin/env python
# coding: utf-8

# In[1]:


#thining operator


# In[2]:


import numpy as np
import cv2
np.set_printoptions(threshold=np.inf)


# In[3]:


yokoi = np.loadtxt('afteriteration6.txt')   #疊代需要改 EX:afteriteration(X).txt
for row in range(64):
    for col in range(64):
        print(int(yokoi[row][col]), end=' ')
#print(np.shape(yokoi))
        
img = cv2.imread('iteration6.bmp',cv2.IMREAD_GRAYSCALE)   #疊代需要改 EX:newiteration(X).bmp
#print(np.shape(img))


# In[4]:


#pair relationship operator

#先把yokoi做padding:
paddingyokoi = np.zeros([66,66])
for row in range(64):
    for col in range(64):
        paddingyokoi[row+1][col+1] = yokoi[row][col]
#print(np.shape(paddingyokoi))
#print('paddingyokoi=',paddingyokoi)


# In[5]:


#區分原本是零與經過h(a)後成為零的值，因此先把原本值為零改成10
for row in range(66):
    for col in range(66):
        if paddingyokoi[row][col] == 0 :
            paddingyokoi[row][col] = 10

#新開一張
markedimg = np.zeros([66,66])
for row in range(66):
    for col in range(66):
        markedimg[row][col] = paddingyokoi[row][col]

#h()
for row in range(66):
    for col in range(66):
        if paddingyokoi[row][col] == 1:
            markedimg[row][col] = 1
        elif paddingyokoi[row][col] == 10:
            markedimg [row][col] = 10
        else:
            markedimg[row][col] = 0

#開設一張markedimg2存markedimg的data, 把markedimg中10的位置改回0，以便等等判斷
markedimg2 = np.zeros([66,66])
for row in range(66):
    for col in range(66):
        markedimg2[row][col] = markedimg[row][col]
        if markedimg[row][col] == 10:
            markedimg[row][col] = 0

#print('paddingyokoi=',paddingyokoi)
#print('markedimg2=',markedimg2)
#需標記位置個數:
sum=0
for row in range(66):
    for col in range(66):
        if markedimg2[row][col] == 0 or markedimg2[row][col] == 1:
            sum = sum + 1
#print('number of marked=',sum)
#print('markedimg=',markedimg) #only 0 and 1


# In[6]:


#pair_output
sum = 0
finalmarkedimg = np.zeros([66,66]) #一樣有padding
for row in range(64):
    for col in range(64):
        if markedimg2[row+1][col+1] == 0 or markedimg2[row+1][col+1] == 1: #10的位置，也就是原本=0的位置不用判斷。
            sum = markedimg[row+1][col+2] + markedimg[row][col+1] + markedimg[row+1][col] + markedimg[row+2][col+1]
            #print('markedimg2[row+1][col+1]=',markedimg2[row+1][col+1])
            #print('sum=',sum)
            
            if sum < 1 or markedimg2[row+1][col+1] != 1:
                finalmarkedimg[row+1][col+1] = 9 # 設q = 9
                sum = 0
            elif sum >= 1 and markedimg2[row+1][col+1] == 1:
                finalmarkedimg[row+1][col+1] = 6 # 設p = 6
                sum = 0
            else:
                print('error')
                sum = 0
            #print('finalmarkedimg[row+1][col+1]=',finalmarkedimg[row+1][col+1])
            
#print(markedimg)
#print(markedimg2)
numberofmarked = 0
for row in range(66):
    for col in range(66):
        if finalmarkedimg[row][col] == 9 or finalmarkedimg[row][col] == 6:
            numberofmarked = numberofmarked + 1
#print('numberofmarked=',numberofmarked)
#print(finalmarkedimg)

                
                


# In[7]:


print(np.shape(img))
print(np.shape(finalmarkedimg))
#padding img
paddingimg = np.zeros([66,66])
for row in range(64):
    for col in range(64):
        paddingimg[row+1][col+1] = img[row][col]
print(np.shape(paddingimg))
#cv2.imshow('paddingimg',paddingimg)
#cv2.waitKey()


# In[8]:


#11/18,19:25p.m. check以上都OK

#so,現在有padding後原圖(paddingimg)和標記q,p後的圖(finalmarkedimg)
#針對標記p(6)的位置判斷 connected shrink operator(以原圖數值判斷(0,255)):

#開a1,a2,a3,a4空間，都先填5，這樣等等填0,1，5 之後加總才知道位置在哪，不然會搞混0
a1 = np.zeros([64,64])
a2 = np.zeros([64,64])
a3 = np.zeros([64,64])
a4 = np.zeros([64,64])
for row in range(64):
    for col in range(64):
        a1[row][col]=5
        a2[row][col]=5
        a3[row][col]=5
        a4[row][col]=5


# In[9]:


#def h(b,c,d,e):
def h(b,c,d,e):
    if b == c and (b!=d or b!=e):
        return 1
    else:
        return 0

sum = 0
for row in range(64):
    for col in range(64):
        if finalmarkedimg[row+1][col+1] == 6:  #證明了是針對p
            #a1 = h(x0,x1,x6,x2)
            #a2 = h(x0,x2,x7,x3)
            #a3 = h(x0,x3,x8,x4)
            #a4 = h(x0,x4,x5,x1)
            #h(b,c,d,e) = 1 if b=c and (b!=d or b!=e)
            
            
            a1[row][col] = h(paddingimg[row+1][col+1],paddingimg[row+1][col+2],paddingimg[row][col+2],paddingimg[row][col+1])
            #print('b=',paddingimg[row+1][col+1],'c=',paddingimg[row+1][col+2],'d=',paddingimg[row][col+2],'e=',paddingimg[row][col+1])
            #print('a1=',a1[row][col])
            a2[row][col] = h(paddingimg[row+1][col+1],paddingimg[row][col+1],paddingimg[row][col],paddingimg[row+1][col])
            #print('b=',paddingimg[row+1][col+1],'c=',paddingimg[row][col+1],'d=',paddingimg[row][col],'e=',paddingimg[row+1][col])
            #print('a2=',a2[row][col])
            a3[row][col] = h(paddingimg[row+1][col+1],paddingimg[row+1][col],paddingimg[row+2][col],paddingimg[row+2][col+1])
            #print('b=',paddingimg[row+1][col+1],'c=',paddingimg[row+1][col],'d=',paddingimg[row+2][col],'e=',paddingimg[row+2][col+1])
            #print('a3=',a3[row][col])
            a4[row][col] = h(paddingimg[row+1][col+1],paddingimg[row+2][col+1],paddingimg[row+2][col+2],paddingimg[row+1][col+2])
            #print('b=',paddingimg[row+1][col+1],'c=',paddingimg[row+2][col+1],'d=',paddingimg[row+2][col+2],'e=',paddingimg[row+1][col+2])
            #print('a4=',a4[row][col])
            
            #加總各個位置
            sum = a1[row][col] + a2[row][col] + a3[row][col] + a4[row][col]
            #print('sum=',sum)
            #把sum = 1 的位置，在原圖上刪除(改成0)
            if sum == 1:
                finalmarkedimg[row+1][col+1] = 0
                paddingimg[row+1][col+1] = 0
                img[row][col] = 0
                sum = 0
            else:
                sum = 0


# In[10]:


#cv2.imshow('finalpaddingimg',paddingimg)
#cv2.waitKey()
cv2.imwrite('iteration7.bmp',img)   #疊代需要改 EX: newiteration(x).bmp


# In[11]:


#11/18 19:45插入:可能成功了在try幾次。

#改輸入與輸出的image即可，疊代多次
#有地方寫錯了，要疊代很多次，注意圖片右邊都沒有改變...
#抓到bug->因為做完一次thinning之後，要再重做一次yokoi阿阿阿阿
#需要把程式做打包成function，不然這樣要手動一直改很麻煩
#先手動try一次看看
#11/18 14:30 完成手動12次疊代，發現結果有點不同，會有斷點，可能有寫錯。


# In[ ]:





# In[ ]:




