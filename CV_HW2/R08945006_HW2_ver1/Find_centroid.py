#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.set_printoptions(threshold=np.inf)
import cv2


# In[2]:


img_aftercc = np.load('aftercc_matrix.npy')
#print(img_aftercc)


# In[3]:


#centroid座標如下:
# row' = bounding box中所有 row * row 中 pixel個數(不含背景) / 總面積
# column' = boundind box中所有 column * column 中 pixel個數(不含背景) / 總面積

#boundind box由左至右算 1-5
#b1: [399,0],[511,31]         107770
#b2: [0,0],[511,87]           1
#b3: [237,89],[287,139]       66809
#b4: [94,118],[237,157]       26099
#b5: [0,127],[511,511]        73

#面積是有該區域元素的pixel才算,不是bounding box的
#  1  ,  73  ,  26099  ,66809  , 107770                 (區域)
#18362  ,  106045  ,  2048  ,  644  ,  1490             (面積)


# In[4]:


#bounding box 1 中所有 row * row 中 pixel個數(不含背景)

store_list = np.zeros([114])
for i in range(399,512):
    for j in range(0,32):
        if img_aftercc[i][j] == 107770:
            store_list[i-399] = store_list[i-399] + 1
print(store_list)

for i in range(114):
    store_list[i] = store_list[i] * (i+1)
print(store_list)

s = sum(store_list) 

print(s)

b1_c_row = s / 1490
b1_c_row = round(b1_c_row) #四捨五入取整 ! 
print(b1_c_row)

#------------------------------------------------------------------------------------------------------

#bounding box 1 中所有 col * col 中 pixel個數(不含背景)

store_list = np.zeros([32-0+1])
for j in range(0,32):
    for i in range(399,512):
        if img_aftercc[i][j] == 107770:
            store_list[j] = store_list[j] + 1
print(store_list)
for j in range(32):
    store_list[j] = store_list[j] * (j+1)
print(store_list)
s = sum(store_list) 
print(s)
b1_c_col = s / 1490
b1_c_col = round(b1_c_col)
print(b1_c_col)

#boundbox1的centroid座標 = (b1_c_row,b1_c_col)


# In[5]:


#畫centroid
#cv.circle(img, (160, 160), 60, (0, 0, 255), 0)
#               圓心座標    半徑  顏色       厚度


# In[6]:


final_img = cv2.imread('final_img.bmp')
final_img3 = cv2.circle(final_img, (0+19, 399+60), 5, (0, 0, 255), 0)
                            #千萬千萬注意!! 算出來的centroid座標是以該boundingbox左上角為基準,且畫圓形的座標(col,row)!! 不是(row,col)


# In[7]:


#爽啦~~~~~~~~~~~~~~成功了~~~~~~~~~~~~~~~~~~


# In[8]:


#bounding box 2 中所有 row * row 中 pixel個數(不含背景)
#b2: [0,0],[511,87]           1
store_list = np.zeros([511-0+1])
for i in range(0,512):
    for j in range(0,88):
        if img_aftercc[i][j] == 1:
            store_list[i-0] = store_list[i-0] + 1
print(store_list)

for i in range(512):
    store_list[i] = store_list[i] * (i+1)
print(store_list)

s = sum(store_list) 

print(s)

b2_c_row = s / 18362
b2_c_row = round(b2_c_row) #四捨五入取整 ! 
print(b2_c_row)

#bounding box 2 中所有 col * col 中 pixel個數(不含背景)

store_list = np.zeros([87-0+1])
for j in range(0,88):
    for i in range(0,512):
        if img_aftercc[i][j] == 1:
            store_list[j] = store_list[j] + 1
print(store_list)
for j in range(88):
    store_list[j] = store_list[j] * (j+1)
print(store_list)
s = sum(store_list) 
print(s)
b2_c_col = s / 18362
b2_c_col = round(b2_c_col)
print(b2_c_col)

final_img3 = cv2.circle(final_img3, (0+43, 0+230), 5, (0, 0, 255), 0)
                        #千萬千萬注意!! 算出來的centroid座標是以該boundingbox左上角為基準,且畫圓形的座標(col,row)!! 不是(row,col)


# In[9]:


#bounding box 3中所有 row * row 中 pixel個數(不含背景)
#b3: [237,89],[287,139]       66809    644

store_list = np.zeros([287-237+1])
for i in range(237,288):
    for j in range(89,140):
        if img_aftercc[i][j] == 66809:
            store_list[i-237] = store_list[i-237] + 1
print(store_list)

for i in range(51):
    store_list[i] = store_list[i] * (i+1)
print(store_list)

s = sum(store_list) 

print(s)

b3_c_row = s / 644
b3_c_row = int(round(b3_c_row)) #四捨五入取整 ! 
print(b3_c_row)

#bounding box 2 中所有 col * col 中 pixel個數(不含背景)

store_list = np.zeros([139-89+1])
for j in range(89,140):
    for i in range(237,288):
        if img_aftercc[i][j] == 66809:
            store_list[j-89] = store_list[j-89] + 1
print(store_list)
for j in range(51):
    store_list[j] = store_list[j] * (j+1)
print(store_list)
s = sum(store_list) 
print(s)
b3_c_col = s / 644
b3_c_col = int(round(b3_c_col))
print(b3_c_col)

final_img3 = cv2.circle(final_img3, (89+b3_c_col, 237+b3_c_row), 5, (0, 0, 255), 0)


# In[10]:


#b4: [94,118],[237,157] , pixel_index = 26099 , area = 2048

store_list = np.zeros([237-94+1])
for i in range(94,238):
    for j in range(118,158):
        if img_aftercc[i][j] == 26099:
            store_list[i-94] = store_list[i-94] + 1
            
for i in range(237-94+1):
    store_list[i] = store_list[i] * (i+1)
s = sum(store_list) 

b4_c_row = s / 2048
b4_c_row = int(round(b4_c_row))

store_list = np.zeros([157-118+1])
for j in range(118,158):
    for i in range(94,238):
        if img_aftercc[i][j] == 26099:
            store_list[j-118] = store_list[j-118] + 1

for j in range(157-118+1):
    store_list[j] = store_list[j] * (j+1)
s = sum(store_list) 
b4_c_col = s / 2048
b4_c_col = int(round(b4_c_col))

final_img3 = cv2.circle(final_img3, (118+b4_c_col, 94+b4_c_row), 5, (0, 0, 255), 0)


# In[11]:


#b5: [0,127],[511,511]        73      106045

store_list = np.zeros([511-0+1])
for i in range(0,512):
    for j in range(127,512):
        if img_aftercc[i][j] == 73:
            store_list[i-0] = store_list[i-0] + 1
            
for i in range(511-0+1):
    store_list[i] = store_list[i] * (i+1)
s = sum(store_list) 

b5_c_row = s / 106045
b5_c_row = int(round(b5_c_row))

store_list = np.zeros([511-127+1])
for j in range(127,512):
    for i in range(0,512):
        if img_aftercc[i][j] == 73:
            store_list[j-127] = store_list[j-127] + 1

for j in range(511-127+1):
    store_list[j] = store_list[j] * (j+1)
s = sum(store_list) 
b5_c_col = s / 106045
b5_c_col = int(round(b5_c_col))

final_img3 = cv2.circle(final_img3, (127+b5_c_col, 0+b5_c_row), 5, (0, 0, 255), 0)





cv2.imwrite('final_img3.bmp',final_img3)
final_img3 = cv2.imread('final_img3.bmp')
cv2.imshow('final_img3',final_img3)
cv2.waitKey(0)


# In[ ]:




