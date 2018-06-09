
# coding: utf-8

# In[5]:


def is_prime(n):
    if n > 1:
        x = n // 2
        for i in range(2, x + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False


# In[9]:


def count():
    a = 0
   
    for i in range(1, 10000000):
        if is_prime(i):
            a += 1
            if a == 10001:  
                return i


# In[ ]:


a = count()
print(a)

