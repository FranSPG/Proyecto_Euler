
# coding: utf-8

# In[2]:


def gauss(n):    
    return (n*(n+1))/2

def gauss_pow_2(n):
    a = 0
    for i in range(1, n+1):
        a = i**2 + a
    return a

n = 100
print((gauss(n)**2) - gauss_pow_2(n))

