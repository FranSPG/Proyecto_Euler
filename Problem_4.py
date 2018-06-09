
# coding: utf-8

# In[13]:


# https://projecteuler.net/problem=4

# Función para determinar si un numero es palindromic
def palindromic(n):
    if str(n)[::-1] == str(n) and n > 900000: # n > 900000 es para no ver todos los resultados posibles
                                              # elegí un numero al azar alto
        print('Palindromic {}'.format(n))
        return True
    
def multiplication():
    b = 999
    for b in range(b, 1, -1):
        a = 999
        for a in range(a, b,-1):    
            if palindromic(b*a):
                print('a y b ', a,b)


# In[14]:


multiplication()

