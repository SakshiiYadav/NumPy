
# coding: utf-8

# In[38]:


# NumPy for array
    
    #Numpy stands for Numerical Python. It is a core library for numeric and scientific computing 
    


# In[2]:


import numpy as np
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])


# In[3]:


n1


# In[4]:


n2


# In[5]:


print(n1)


# In[6]:


print(n2)


# In[7]:


# Initializing NumPy array with zeroes
    


# In[8]:


a1 = np.zeros((1,2))
a1


# In[9]:


type(a1)


# In[10]:


aa = np.zeros((3,3))


# In[11]:


aa


# In[12]:


type(aa)


# In[ ]:





# In[13]:


# Initializing NumPy with same number 


# In[14]:


a2 = np.full((6,2),22)       # full(row,column,parameter)


# In[15]:


a2


# In[16]:


# Initializing NumPy within a range
    


# In[17]:


n3 = np.arange(9)
n3


# In[18]:


n4 = np.arange(3,16)
print(n4)


# In[19]:


n5 = np.arange(1,60,5)       #arange(lb,exclusive_ub,skip parameter)
n5


# In[20]:


# NumPy array with RANDOM NUMBERS


# In[21]:


ra1 = np.random.randint(1,100,5)     
ra1


# In[22]:


# NumPy array to check SHAPE


# In[23]:


s1 = np.array([[1,2,5],[3,6,7]])
s1


# In[24]:


print(s1.shape)        #shape tells the dimension(no_of_row,no_of_column) of given array


# In[25]:


s1.shape = (3,2)
s1


# In[26]:


# NumPy array MATHEMATICS 
    


# In[27]:


# SUM
s2 = np.array([10,11,13])
s3 = np.array([15,66,48])


# In[28]:


s2


# In[29]:


s3


# In[30]:


np.sum([s2,s3])


# In[31]:


#SUM with AXIS = 0 (VERTICAL ADDITION)
np.sum([s2,s3],axis = 0)


# In[32]:


#SUM with AXIS = 1 (HORIZONTAL ADDITION)
np.sum([s2,s3],axis = 1)


# In[33]:


# JOINING NumPy array


# In[34]:


ab = np.array([11,12,13,14])
ac = np.array([15,16,17,18])


# In[35]:


np.vstack([ab,ac])


# In[36]:


np.hstack([ab,ac])


# In[37]:


np.column_stack([ab,ac])

