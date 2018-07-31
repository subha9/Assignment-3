
# coding: utf-8

# In[72]:


#1.1 Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()

def app(lst1):
    app=lst1[0]
    for i in range(1,len(lst1)):
        app*=lst1[i]
    return app
print(app([4,3,2,1]))

#from functools import reduce
#n=[4,3,2,1]
#print(reduce(lambda x,y:x*y,n))



# In[75]:


#Write a Python program to implement your own myfilter() function which works exactly like
#Python's built-in function filter()
def my_fun(lst1):
    lst2=[x for x in lst1 if x>2]
    return lst2
print (my_fun([4,3,2,1]))

#n=[4,3,2,1]
#print(list(filter(lambda x :x>2,n)))


# In[ ]:


#Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', 'L’, ]


# In[84]:


word ='ACADGILD'
a_lst =[x for x in word]
print( 'word' + str(a_lst))


# In[101]:


#Write List comprehensions to produce the following Lists
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
input_list =['x','y','z']
res = [ item*num for item in input_list for num in range(1,5)  ]
print('input_list ='+str(res))


# In[99]:


lst = ['x','y','z']
i = [ item*num for num in range(1,5) for item in lst  ]
print( str(i))


# In[98]:


a = [2,3,4]
b = [ [item+num] for item in a for num in range(0,3)]
print(str(b)) 


# In[107]:


a=[2,3,4,5]
b= [[item+num for item in a] for num in range(0,4)]
print(str(b))


# In[116]:


a=[1,2,3]
t=tuple(a)
r =[(x,y) for x in a for y in a]
print(str(r))


# In[117]:


def long_word(word_lists):
    word_length=[]
    for n in word_lists:
        word_length.append((len(n),n))
        word_length.sort()
    return  word_length[-1][1]
print(long_word(["python","java","Science"]))

