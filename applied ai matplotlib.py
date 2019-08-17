
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot([2,4,6,4]) # y vals
#x vals are indices 
plt.ylabel("numbers")
plt.xlabel('indices')
plt.title("naman plot")
plt.show()


# In[5]:


#if we would have grid here it would be easy to read

plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel("index")
plt.ylabel("values")
plt.title("naman plot")
plt.grid()


# In[6]:


#fro different kind of plots
plt.plot([1,2,3,4],[1,4,9,16],'ro') 
plt.grid()
#ro means red and o means dots
plt.show()


# In[8]:


import numpy as np
t=np.arange(0.,5.,0.2)
plt.plot(t,t**2,'b--',label='^2')
plt.plot(t,t**2.2,'rs',label='^2.2')
plt.plot(t,t**2.5,'g^',label='^2.5')
plt.grid()
plt.legend() # it is variable explanation

plt.show()


# In[10]:


x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,linewidth=10.0)
plt.show()


# In[13]:


x1=[1,2,3,4]
y1=[1,4,9,16]
x2=[1,2,3,4]
y2=[2,4,6,8]
lines=plt.plot(x1,y1,x2,y2)

#lines is a tuple  ,pair in  this case

#setproperties
plt.setp(lines[0],color='r',linewidth=2.0)
plt.grid()


# In[16]:


#working with multiple figures and plots

#multiple plots in one figure

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.figure(1)

plt.subplot(211) #2 rows 1 coln for figure 1
#we want subplt with 2 row 1 col
plt.grid()
plt.plot(t1,np.exp(-t1),'b-')

plt.subplot(212) # 2row 1coln fig1
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()


# In[18]:


plt.figure(1)

plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.subplot(212)
plt.plot([4,5,6])

plt.figure(2)
plt.plot([4,5,6])

plt.figure(1)
plt.subplot(211)
plt.title('easy as 1,2,3')
plt.show()

