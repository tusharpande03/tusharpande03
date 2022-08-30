#!/usr/bin/env python
# coding: utf-8

# # Copy and View in Numpy

# In[4]:


# view 
import numpy as np

arr = np.array([1,2,3,4,5,6])
x = arr.view()

print(id(arr))
print(id(x))

x[0] = 100

print(arr)
print(x)


# In[6]:


# view 
import numpy as np

arr = np.array([1,2,3,4,5,6])
x = arr

print(id(arr))
print(id(x))

x[0] = 100

print(arr)
print(x)


# In[2]:


a = [1,2,3,4,5]
b = a

print(id(a))
print(id(b))

b[1] = 100

print(a)
print(b)


# In[8]:


# copy 
import numpy as np

arr = np.array([1,2,3,4,5,6])
x = arr.copy()

print(id(arr))
print(id(x))

x[0] = 100

print(arr)
print(x)


# In[9]:


# copy 
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
x = arr.copy()

print(id(arr))
print(id(x))

x[0][1] = 100

print(arr)
print(x)


# In[12]:


# copy 
import numpy as np

arr = np.array([1,2,3,4,5,6])
x = arr.view()

print(id(arr))
print(id(x))

x[0] = 100

print(arr)
print(x)


# #### The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
# 
# 1. The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# 
# 2. The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
# 

# In[22]:


# view 

arr = np.array([1,2,3,4,5,6])
x = arr.view()

print(id(arr))
print(id(x))
x[0] = 100

print(arr)
print(x)


# In[14]:


# copy 

arr = np.array([1,2,3,4,5,6])
x = arr.copy()

print(id(arr))
print(id(x))

x[0] = 100

print(arr)
print(x)


# # Pandas

# In[ ]:


- data representation in pandas is better than numpy
- Can store hetrogenous data


# In[23]:


import pandas as pd


# In[ ]:


# We have 2 main data structures

* Seriesdata ---> 1D
* Dataframe ----> 2D


# # Series 

# In[ ]:


Different ways to create a series

1. List
2. Array
3. dic


# In[24]:


# List

river = ['Ganga', 'Yamuna', 'neil', 'kaveri', 'godavari']


# In[25]:


river_name = pd.Series(river)
print(type(river_name))


# In[26]:


river_name


# In[27]:


# array

random_series = pd.Series(np.random.randn(5))
random_series


# In[28]:



random_series = pd.Series(np.random.randn(5) , index = ['a','b','c','d','e'])
random_series


# In[29]:



random_series = pd.Series(np.random.randn(5) , index = ['a','b','c','d'])
random_series


# In[31]:



random_series = pd.Series(np.random.randn(5) , index = ['a','b','c','d','e','f'])
random_series


# In[33]:


river_name


# In[34]:


river_name = pd.Series(river , index = ['a','b','c','d','e'])


# In[35]:


river_name


# In[36]:


river_name[3]


# In[37]:


river_name['d']


# In[39]:


river_name['d'] = 'Krishna'


# In[40]:


river_name


# In[41]:


river_name[2:4]


# In[42]:


river_name[::-1]


# In[44]:


river_name


# In[45]:


river_name['b':'e']


# In[46]:



river_name['b':'c']


# 1. For default index values [inclusive: exclusive]
# 2. For user defined index values [inclusive:inclusive]

# In[47]:



river_name['c':'b':-1]


# In[49]:



river_name['a':'e':2]


# In[48]:


river_name


# In[85]:


brics_country = ['Brazil', 'Russia', 'India', 'China', 'South Africa']

brics_currency = ['Real', 'Ruble', 'Rupee', 'Renminbi', 'Rand' ]


# pd.Series(values , index = var)

# In[51]:


data = pd.Series(brics_country , index = brics_currency)
data


# In[52]:


# If you want to see only the index data

data.index


# In[53]:


# If you want to see only the values data

data.values


# In[54]:


a = data.values
print(type(a))


# In[ ]:


pd.Series()


# In[55]:


contry = ['Afghanistan', 'Albania', 'Algeria', 'Andorra']

capital = ['Kabul', 'Tirane', 'Algiers', 'Andorra la Vella' ]

currency = ['Afghani', 'Lek' ,'Dinar' ,'Euro']


# In[75]:


data_series = pd.Series(capital , index=[contry, currency], dtype= 'str')
data_series


# In[63]:


print(type(data_series))


# In[64]:


data_series.index


# In[65]:


data_series.values


# In[66]:


data_series['Albania']


# In[73]:


dic = {(1,2,3):(1,2,43), 'b':2 , 'c':4 }

dic


# In[79]:


dic = {'a':1 , 'b':2 , 'c':4 }

dic


# In[77]:


data = pd.Series(dic)
data


# In[82]:


data = pd.Series(dic , index = ['b', 'd' , 'e'])
data


# In[83]:


data_series


# In[88]:


river_name


# In[89]:


data


# In[90]:


pd.concat([river_name , data])


# # Dataframe

# In[97]:


country = ['Afghanistan', 'Albania', 'Algeria', 'Andorra']

capital = ['Kabul', 'Tirane', 'Algiers', 'Andorra la Vella' ]

currency = ['Afghani', 'Lek' ,'Dinar' ,'Euro']


# In[95]:


data = pd.DataFrame(country)
data


# In[100]:


data = pd.DataFrame(country )
data


# In[96]:


data = pd.DataFrame([country ,capital , currency])
data


# In[118]:


df = pd.read_csv('C://Users//MIT//Desktop//datasets/ted_data.csv')


# In[119]:


df


# In[120]:


df = pd.read_csv('datasets/ted_data.csv')


# In[121]:


df


# In[122]:


# excel
df_excel = pd.read_excel('datasets/football_worldcup.xlsx')
df_excel


# In[123]:


df_dict = {'Year' : [1990, 1994, 1998, 2002 , 2004],
           'Country' : ['Italy', 'USA', 'France', 'Japan'],
           'Winner' : ['Germany', 'Brazil', 'France', 'Brazil'],
           'GoalScored' : [115, 141, 171, 161]
          }


# In[124]:


data = pd.DataFrame(df_dict)
data


# In[125]:


df_dict = {'Year' : [1990, 1994, 1998, 2002 ],
           'Country' : ['Italy', 'USA', 'France', 'Japan'],
           'Winner' : ['Germany', 'Brazil', 'France', 'Brazil'],
           'GoalScored' : [115, 141, 171, 161]
          }


# In[126]:


data = pd.DataFrame(df_dict)
data


# In[129]:


df_dict = {'Year' : pd.Series([1990, 1994, 1998, 2002 , 2004]),
           'Country' : pd.Series(['Italy', 'USA', 'France', 'Japan']),
           'Winner' : pd.Series(['Germany', 'Brazil', 'France', 'Brazil']),
           'GoalScored' : pd.Series([115, 141, 171, 161])
          }


# In[130]:


data = pd.DataFrame(df_dict)
data


# In[138]:


brics_country


# In[139]:


brics_currency


# In[140]:


data = pd.DataFrame([brics_country,brics_currency])
data


# In[ ]:


country -->
currency -->


# In[141]:


df_dict = {'Country': brics_country,
          'currency': brics_currency}


# In[142]:


data = pd.DataFrame(df_dict)
data


# In[149]:


brics_country = ['Brazil', 'Russia', 'India', 'China', 'South Africa' , 'country']

brics_currency = ['Real', 'Ruble', 'Rupee', 'Renminbi' ,np.nan ,'values']


# In[150]:


df_dict = {'Country': pd.Series(brics_country),
          'currency': pd.Series(brics_currency)}


# In[151]:


data = pd.DataFrame(df_dict)
data


# In[ ]:





# In[ ]:




