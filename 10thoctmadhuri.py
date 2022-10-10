#!/usr/bin/env python
# coding: utf-8

# In[3]:


#mean
def mean(list):
    
    sum=0
    for i in list:
        sum=sum+i
        
    mean=sum/len(list)
    return mean
list=(10,20,30,40,50,60,70)
print("mean",mean(list))


# In[6]:


#median
l1=(10,20,30,40,50,60,70)
i=int(len(l1)/2)
if(i%2==0):
    res=(l1[i]+l1[i+1])/2
else:
    res=l1[i]
print("median",res)    


# In[8]:


#mode
l1=(10,20,30,30,40,50,60,70)
d={}
for i in l1:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
max=0
for i in d:
    if(d[i]>max):
        max=d[i]
        ans=i
print("MODE",ans)        
        
        


# In[9]:


#variance
def var(l):
    ans=mean(l)
    
    sum=0
    for i in l:
        sum+=(ans-i)**2
        
    return sum/len(l)
l=(10,20,30,40,50,60,70)
print("variance",var(l))


# In[11]:


#standard deviation
def sd(l):
    temp=var(l)
    return temp**0.5

l=(10,20,30,40,50,60,70)
print("standard deviation",sd(l))


# In[ ]:




