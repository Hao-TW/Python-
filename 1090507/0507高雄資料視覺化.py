#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


x = np.linspace(-10,10,100)
y = np.sin(x)
plt.plot(x , y)


# In[9]:


x = np.linspace(0, 10, 200)
y = np.sin(5*x) / (1+x**2)
plt.plot(x,y,'y')


# In[13]:


x = np.linspace(-10,10,200)
y = np.cos(x)

plt.plot(x,y,'r:')


# In[18]:


plt.plot(x,y, c='r', lw=2 , ls =':')


# In[19]:


x = range(20)
y = np.random.randn(20)
plt.plot(x, y, marker='o')


# In[20]:


plt.plot(x, y, c='#6b8fb4', lw=5, marker='o', mfc='#fffa7c', mec="#084c61", mew=3, ms=20)


# In[26]:


plt.plot([1,2,3,4] , [1,4,9,16],'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')


# In[27]:


plt.bar(range(1,6), np.random.randint(1,30,5))


# In[28]:


import numpy as np
from matplotlib import pyplot as plt

#100個學生的分數
data = [73, 71, 34, 85, 80, 100, 57, 78, 88, 98, 
        46, 34, 74, 86, 41, 54, 80, 40, 71, 46, 
        43, 51, 58, 61, 71, 70, 65, 39, 28, 62, 
        49, 89, 73, 38, 41, 51, 45, 64, 51, 34, 
        42, 58, 67, 56, 71, 45, 32, 42, 59, 98, 
        33, 64, 55, 67, 50, 45, 64, 63, 85, 39, 
        48, 62, 34, 67, 100, 58, 68, 34, 38, 70, 
        64, 74, 62, 73, 45, 17, 68, 26, 69, 56, 
        76, 59, 45, 95, 78, 77, 70, 59, 91, 79, 
        53, 78, 61, 84, 56, 96, 68, 64, 46, 70]
data = np.array(data) # 將分數串列轉換為np陣列
#以等差級數決定方盒的數量，為20
bins = np.linspace(np.ceil(min(data)), np.floor(max(data)), 20)
#繪出直方圖，顏色為橘色，透明度為0.5
plt.hist(data, bins, color='orange', alpha=0.5)
#設定X軸刻度
plt.xlim([0, 100])
#設定X軸名稱
plt.xlabel('Score', size=14)
#設定Y軸名稱
plt.ylabel('Quantity', size=14)
#設定圖標題
plt.title('Student Scores Distribution', size=20)
#顯示圖
plt.show()


# In[29]:


x = np.arange(1,6)
plt.bar(x - 0.4, [3, 10, 8, 12, 6], width=0.4, ec='none', fc='#e63946')
plt.bar(x, [6, 3, 12, 5, 8], width=0.4, ec='none', fc='#7fb069')


# In[30]:


data = [5, 20, 15, 25, 10]

plt.bar(range(len(data)), data, color='rgb') # or `color=['r', 'g', 'b']`
plt.show()


# In[31]:


data = [5, 20, 15, 25, 10]

plt.bar(range(len(data)), data, ec='r', ls='--', lw=2)#ec=edgecolor
plt.show()


# In[33]:


data = [5, 20, 15, 25, 10]

plt.bar(range(len(data)), data, ec='k', lw=1, hatch='/')#hatch关键字可用来设置填充样式，可取值为：/, \, |, -, +, x, o, O, ., *
plt.show()


# In[34]:


data = [5, 20, 15, 25, 10]
labels = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']

plt.bar(range(len(data)), data, tick_label=labels)#tick_label可設置字串在X軸
plt.show()


# In[35]:


#通过bottom参数，可以绘制堆叠柱状图。例如：

import numpy as np
import matplotlib.pyplot as plt

size = 5
x = np.arange(size)
a = np.random.random(size)
b = np.random.random(size)

plt.bar(x, a, label='a')
plt.bar(x, b, bottom=a, label='b')
plt.legend()
plt.show()


# In[36]:


A = np.random.randint(2,15,5)
B = np.random.randint(2,15,5)
C = np.random.randint(2,15,5)
plt.bar(x, A, fc='#e63946', ec='none')
plt.bar(x, B, fc='#7fb069', ec='none', bottom = A)
plt.bar(x, C, fc='#e55934', ec='none', bottom = A+B)


# In[38]:


# plt.barh方法的签名为：

# barh(bottom, width, height=0.8, left=None, **kwargs)

# 使用barh方法绘制条形图

data = [5, 20, 15, 25, 10]

plt.barh(range(len(data)), data ,fc='#e55934', ec='none')
plt.show()


# In[39]:


#正负条形图
a = np.array([5, 20, 15, 25, 10])
b = np.array([10, 15, 20, 15, 5])

plt.barh(range(len(a)), a)
plt.barh(range(len(b)), -b)
plt.show()


# In[40]:


#12個月的銷售額
sale = np.array([22, 22, 17, 21, 22, 19, 21, 19, 20, 15, 24, 19])
#12個月的利潤
profit = np.array([12, 15, 11, 17, 11, 12, 11, 10, 16, 16, 13, 11])


# In[ ]:




