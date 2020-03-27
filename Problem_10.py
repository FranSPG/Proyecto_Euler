
# coding: utf-8

# In[5]:


import Fermat_theorem as ft
import sys
sys.setrecursionlimit(5000000)


# In[6]:


def sum_prime(n):
    if (n == 0):
        return 0
    if(ft.is_probably_prime(n)):
        return (sum_prime(n-1) + n)
    return sum_prime(n-1)

    
# In[ ]:


result = sum_prime(2000000)
print('The sum of the primes below 2000000: {}'.format(result))
