
# coding: utf-8

# In[2]:


from random import randint
def is_probably_prime(n, k = 3):
    # The Fermat's little theorem
    
    if (n == 2):
        return True
    if (n < 2):
        return False
    if (n % 2 == 0):
        return False
    
    for i in range(0, k):
        a = randint(1, n-1)
        if (pow(a, n-1, n) != 1):
            return False 
    return True


# In[1]:


2%2

