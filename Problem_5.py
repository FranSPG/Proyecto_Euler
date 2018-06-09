
# coding: utf-8

# In[8]:


m = 20;

def multiplication(n, m):
    for i in range(1, m):
        if not (n/i).is_integer():
            return False
            break
    return True

n = 1000000000
def count(n):
    for i in range(1, n):
        if multiplication(i, m):
            print('encontro ', i)
            break
            
count(n)

