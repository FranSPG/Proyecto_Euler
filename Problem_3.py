
# coding: utf-8

# In[31]:


from random import randint
 
def is_probably_prime(n, k = 5):
    # The Fermat's little theorem
    
    if (n < 2):
        return False
    if (n % 2 == 0):
        return False
    for i in range(0, k):
        a = randint(1, n-1)
        if (pow(a, n-1, n) != 1):
            return False 
    return True


# In[62]:


def largest_prime_factor(n):
    i = 2
    while i * i < n:
        if(is_probably_prime(i) & (n%i == 0)):
            print(i)
        i = i+1


# In[63]:


largest_prime_factor(600851475143)

