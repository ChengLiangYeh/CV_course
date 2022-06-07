#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.set_printoptions(threshold=np.inf)
import cv2


# In[2]:


img = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE) 


# In[3]:


#img 是 2D


# In[4]:


#print(img) #row -> 橫的 column -> 直的


# In[5]:


#binary 
for i in range(512):
    for j in range(512):
        if img[j][i] < 128:
            img[j][i] = 0
        else:
            img[j][i] = 1            


# In[6]:


#找出0有幾個,安排數字,然後把0依序(row column)換成2345678910 ps.跟一區別,從二開始 


# In[7]:


#智障ㄚㄚㄚㄚㄚㄚ~ 反了啦...... 0是要當作背景,1才是要做connected components的啦~~~~~~~~~~~~~~~~~~~~~~~~~~~


# In[8]:


number = np.sum( img == 1 )
print(number)


# In[9]:


img.dtype


# In[10]:


#轉換資料型態 -> 解決溢位!!
img_int32 = img.astype(int)
img_int32.dtype


# In[11]:


k = 0 #從2開始 ~128185 #智障 趕快改 ~133960

for row in range(512):
    for column in range(512):
        if img_int32[row][column] == 1:
            k = k + 1
            img_int32[row][column] = k
            


# In[12]:


print(img_int32) # row 是橫的


# In[13]:


#幹勒,會溢位啦 -> 已解決


# In[14]:


#要把0的位置切出來喔喔喔~~不是1喔喔喔 ~~~~  #幹你的智障 反了啦


# In[15]:


#下一步「由左而右，由上而下」依序掃瞄各個像素點，將相鄰且不為0之像素以最小值取代。


# In[16]:


#做疊代 
if_iteration = 0


# In[17]:


while if_iteration < 200:   #跑 X 次疊代
    
    for row in range(512):
        for column in range(511):
            if img_int32[row][column] != 0 and img_int32[row][column + 1] != 0:
                if img_int32[row][column] < img_int32[row][column + 1]: 
                    img_int32[row][column + 1] = img_int32[row][column]
                    
                elif img_int32[row][column] > img_int32[row][column + 1]:
                    img_int32[row][column] = img_int32[row][column + 1]
                    
                else:
                    img_int32[row][column] = img_int32[row][column]
                    img_int32[row][column + 1] = img_int32[row][column + 1]
                    
                    
    for column in range(512):
        for row in range(511):
            if img_int32[row][column] != 0 and img_int32[row + 1][column] != 0:
                if img_int32[row][column] < img_int32[row + 1][column]:    
                    img_int32[row + 1][column] = img_int32[row][column]
                    
                elif img_int32[row][column] > img_int32[row + 1][column]:
                    img_int32[row][column] = img_int32[row + 1][column]
                    
                else:
                    img_int32[row][column] = img_int32[row][column]
                    img_int32[row + 1][column] = img_int32[row + 1][column]
                    
                    
    for row in range(512):
        for column in range(511):
            if img_int32[abs(row-511)][column] != 0 and img_int32[abs(row-511)][column + 1] != 0:
                if img_int32[abs(row-511)][column] < img_int32[abs(row-511)][column + 1]:
                    img_int32[abs(row-511)][column + 1] = img_int32[abs(row-511)][column]
                    
                elif img_int32[abs(row-511)][column] > img_int32[abs(row-511)][column + 1]:
                    img_int32[abs(row-511)][column] = img_int32[abs(row-511)][column + 1]
                    
                else:
                    img_int32[abs(row-511)][column] = img_int32[abs(row-511)][column]
                    img_int32[abs(row-511)][column + 1] = img_int32[abs(row-511)][column + 1]
                    
                    
    for column in range(512):
        for row in range(511):
            if img_int32[abs(row-511)][column] != 0 and img_int32[abs(row-510)][column] != 0:
                if img_int32[abs(row-511)][column] < img_int32[abs(row-510)][column]:
                    img_int32[abs(row-510)][column] = img_int32[abs(row-511)][column]
                    
                elif img_int32[abs(row-511)][column] > img_int32[abs(row-510)][column]:
                    img_int32[abs(row-511)][column] = img_int32[abs(row-510)][column]
                    
                else:
                    img_int32[abs(row-511)][column] = img_int32[abs(row-511)][column]
                    img_int32[abs(row-510)][column] = img_int32[abs(row-510)][column]
    
    if_iteration = if_iteration + 1


# In[18]:


print(img_int32)


# In[19]:


#儲存做完connected components的矩陣
#np.save('my_array', x)
#np.load('my_array.npy')

np.save('aftercc_matrix',img_int32)


# In[20]:


img_int32_removedubble = np.unique(img_int32)
print(img_int32_removedubble)
length = len(img_int32_removedubble)
print(length) # 影像總共分984區

store_number = np.zeros(984) #創造一個LIST存每一區的pixel個數


# In[21]:


#test 算出第一排row的個數跟對應的灰階都沒問題!
for k in range(984):
    a = img_int32_removedubble[k]
    for i in range(512):
        for j in range(512):
            if img_int32[i][j] == a:
                store_number[k] = store_number[k] + 1
                
#查看每區的pixel有幾個
print(store_number)


# In[22]:


#找出是哪些灰階的區域
for q in range(984):
    if store_number[q] >500:
        print(img_int32_removedubble[q])


# In[23]:


#0925 08:31 放棄... -> 發現是做反了,重做一次發現是五個區域有符合>500,但是其中一個是0也就是背景...,可能錯了...也可能是疊代次數不夠多?
# -> 不太可能 ,疊代越多次只會讓區域越變越少...(應該) -> 0925 21:11 放棄 -> wowowowowowowowwo -> check it out -> 發現是828沒改成984
#找到connected components的五個區域啦~~~~~~~~~~~~~~~~~~~~~~~what!!!!!!!!!!!!!


# In[24]:


#找到 1 73 26099 66809 107770 的最 上下左右 位置  #0926 02:10 失敗...框起來位置怪怪的,不知道是connected component錯還是框的問題...
#重新疊代一次...(18362,106045,2048,644,1490 -> 五個區域的pixel數)


# In[25]:


index_1 = np.argwhere(img_int32 == 1)
np.shape(index_1)
print(index_1)

#for i in range(18362):
#    List_row[i] = index_1[i][0] 
#print(List_row)
#
#for i in range(18362):
#    List_column[i] = index_1[i][1] 
#print(List_column)
#List_column.sort()
#print(List_column)
#[0,0] , [511,87]


# In[26]:


index_73 = np.argwhere(img_int32 == 73)
np.shape(index_73)
print(index_73)

#print(np.min(index_73,axis=0))
#print(np.min(index_73,axis=1))
#[0,127]
#print(np.max(index_73,axis=0))
#print(np.max(index_73,axis=1))
#[511,511]
#print(index_73)


# In[27]:


index_26099 = np.argwhere(img_int32 == 26099)
np.shape(index_26099)
print(index_26099)
#for i in range(2048):
#    List_row[i] = index_26099[i][0] 
#print(List_row)
#
#for i in range(2048):
#    List_column[i] = index_26099[i][1] 
#print(List_column)
#List_column.sort()
#print(List_column)

#print(np.min(index_26099,axis=0))
#print(np.min(index_26099,axis=1))
#print(np.max(index_1,axis=0))
#print(np.max(index_1,axis=1))
#[94,118] ,[237,157]


# In[28]:


index_66809 = np.argwhere(img_int32 == 66809)
np.shape(index_66809)
print(index_6680)
#for i in range(644):
#    List_row[i] = index_66809[i][0] 
#print(List_row)

#for i in range(644):
#    List_column[i] = index_66809[i][1] 
#print(List_column)
#List_column.sort()
#print(List_column)

#print(np.min(index_66809,axis=0))
#print(np.min(index_66809,axis=1))
#print(np.max(index_66809,axis=0))
#print(np.max(index_66809,axis=1))
#[237,89] ,[287,139]


# In[29]:


#List_row = np.zeros(1490)
#List_column = np.zeros(1490)

index_107770 = np.argwhere(img_int32 == 107770)
np.shape(index_107770)

#for i in range(1490):
#    List_row[i] = index_107770[i][0] 
#print(List_row)

#for i in range(1490):
#    List_column[i] = index_107770[i][1] 
#print(List_column)
#List_column.sort()
#print(List_column)


#print(np.min(index_107770,axis=0))
#print(np.min(index_107770,axis=1))
#print(np.max(index_107770,axis=0))
#print(np.max(index_107770,axis=1))
#[399,0] ,[511,31]

#使用150次疊代沒問題阿~


# In[31]:


#畫 bounding box
#输入参数分别为图像、左上角坐标、右下角坐标、颜色数组、粗细
#cv2.rectangle(img, (x,y), (x+w,y+h), (B,G,R), Thickness)
img_binary = cv2.imread('binarylena.bmp')

final_img2 = cv2.rectangle(img_binary, (0 , 0), (87 , 511), (255, 0, 0), 1)
final_img2 = cv2.rectangle(final_img2, (127 , 0), (511 , 511), (255, 0, 0), 1) 
final_img2 = cv2.rectangle(final_img2, (118 , 94), (157 , 237), (255, 0, 0), 1)
final_img2 = cv2.rectangle(final_img2, (89 , 237), (139 , 287), (255, 0, 0), 1)
final_img2 = cv2.rectangle(final_img2, (0 , 399), (31 , 511), (255, 0, 0), 1)

#注意座標的row,column是相反的


# In[32]:


cv2.imwrite('final_img2.bmp',final_img2)
final_img2 = cv2.imread('final_img2.bmp')
cv2.imshow('final_img2',final_img2)
cv2.waitKey(0)


# In[ ]:


#-------------------------------------------------------------------------------------------------------------------------------


# In[ ]:


#有做疊代,以下就不跑了!(0925 18:11)


# In[54]:


for row in range(512):
    for column in range(511):
        if img_int32[row][column] != 1 and img_int32[row][column + 1] != 1:
            if img_int32[row][column] < img_int32[row][column + 1]: 
                img_int32[row][column + 1] = img_int32[row][column]
            elif img_int32[row][column] > img_int32[row][column + 1]:
                img_int32[row][column] = img_int32[row][column + 1]
            else:
                img_int32[row][column] = img_int32[row][column]
                img_int32[row][column + 1] = img_int32[row][column + 1]
#由上往下的row (check ok at 0925 16:32)
#print(img_int32)


# In[55]:


#由上往下的column
for column in range(512):
    for row in range(511):
        if img_int32[row][column] != 1 and img_int32[row + 1][column] != 1:
            if img_int32[row][column] < img_int32[row + 1][column]:    
                img_int32[row + 1][column] = img_int32[row][column]
            elif img_int32[row][column] > img_int32[row + 1][column]:
                img_int32[row][column] = img_int32[row + 1][column]
            else:
                img_int32[row][column] = img_int32[row][column]
                img_int32[row + 1][column] = img_int32[row + 1][column]
#(check ok at 0925 17:45)


# In[56]:


#最後一步「由左而右，由下而上」依序掃瞄各個像素點，將相鄰且不為0之像素以最小值取代。
#由下往上的row 

for row in range(512):
    for column in range(511):
        if img_int32[abs(row-511)][column] != 1 and img_int32[abs(row-511)][column + 1] != 1:
            if img_int32[abs(row-511)][column] < img_int32[abs(row-511)][column + 1]:
                img_int32[abs(row-511)][column + 1] = img_int32[abs(row-511)][column]
            elif img_int32[abs(row-511)][column] > img_int32[abs(row-511)][column + 1]:
                img_int32[abs(row-511)][column] = img_int32[abs(row-511)][column + 1]
            else:
                img_int32[abs(row-511)][column] = img_int32[abs(row-511)][column]
                img_int32[abs(row-511)][column + 1] = img_int32[abs(row-511)][column + 1]
#(check ok at 0925 17:50)          


# In[57]:


#由下往上的column #這邊有問題,不確定是code錯還是算法錯 -> 更新算法,比較最小值並且增加疊代
for column in range(512):
    for row in range(511):
        if img_int32[abs(row-511)][column] != 1 and img_int32[abs(row-510)][column] != 1:
            if img_int32[abs(row-511)][column] < img_int32[abs(row-510)][column]:
                img_int32[abs(row-510)][column] = img_int32[abs(row-511)][column]
            elif img_int32[abs(row-511)][column] > img_int32[abs(row-510)][column]:
                img_int32[abs(row-511)][column] = img_int32[abs(row-510)][column]
            else:
                img_int32[abs(row-511)][column] = img_int32[abs(row-511)][column]
                img_int32[abs(row-510)][column] = img_int32[abs(row-510)][column]
# 算法是OK的,差疊代(0925 18:00)

