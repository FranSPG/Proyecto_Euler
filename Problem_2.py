
# coding: utf-8

# In[12]:


import sys
sys.setrecursionlimit(5000000)
def fib_sum_even_valued(n):
    if(n < 0): return 0
    if(n % 2 == 0):
        print(n)
        return (fib_sum_even_valued(n-1) + (n + (n-1)))
    return (fib_sum_even_valued(n-1))


# In[11]:


fib_sum_even_valued(3999999)

