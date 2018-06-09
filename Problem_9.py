
# coding: utf-8

# In[1]:


def constr_pythagorean_triple(m, n):
    
    a = n**2 - m**2
    b = 2*n*m
    c = n**2 + m**2
    if a+b+c == 1000:    
        return print('encontre ',a*b*c, ' n m ',n,m)

for i in range(0,1000):
    for x in range(0, i-1):
        constr_pythagorean_triple(x, i)
        

