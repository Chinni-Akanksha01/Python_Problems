#!/usr/bin/env python
# coding: utf-8

# In[2]:


#factorial of a number using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input())
result=fact(n)
print(result)


# In[4]:


num1=200
num2=2
if num1*num2<=100:
    print(num1*num2)
else:
    print(num1+num2)


# In[23]:


sum=0
def current_number():
    for i in range(1,11):
        previous_number=i-1
        current_number=i
        global sum
        sum=current_number+previous_number
        print(f"current number is: {current_number},previous number is: {previous_number},sum is: {sum}")
       

        
current_number()


# In[4]:


#sqyare of number using lambda function
f=lambda a,b:a+b
c=f(5,6)
print(c)


# In[4]:


String=input()
print(f"Original String is {String}")
print(len(String))
for i in range(0,len(String)-1,2):
    print(String[i])
    


# In[8]:


def remove_chars(string,n):
    x=string[n:]
    return x
print(remove_chars("Pynative",4))
print(remove_chars("Pynative",1))        


# In[ ]:




