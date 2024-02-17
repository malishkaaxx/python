#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Write a Python function to calculate the factorial of a given number
a=int(input("enter a no: "))
p=1
def factorial(a):
    global p
    for i in range(1,a+1):
        p=p*i
    print("factorial is",p)
factorial(a)


# In[12]:


#Write a Python function to check if a given string is a palindrome or not.
a=input("enter a string: ")
r=''
def check(a):
    global b,r
    b=a
    for i in range(1,len(a)+1):
        r=r+a[-i]
    if r==b:
        print("palindrome")
    else:
        print("not palindrome")
check(a)   


# In[12]:


#Write a Python function to generate the Fibonacci sequence up to a specified number of terms

a,b=0,1
def fibonacci(a,b):
    n=int(input("enter no of terms: "))
    print(a)
    print(b)
    for i in range(1,n-1):
        c=a+b
        print(c)
        a=b
        b=c
fibonacci(a,b)


# In[20]:


#Write a Python function to check if a given number is a prime number or not. 
def prime(a):
    a=int(input("enter a no: "))
    global c
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c=c+1
    if c<=2:
        print("prime")
    else:
        print("not prime")
prime(a)


# In[40]:


#GCD (Greatest Common Divisor):
#Write a Python function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm. 
a=int(input("enter a no: "))
b=int(input("enter next no: ")) #wrong
def gcd(a,b):
    global c
    while c!=0:
        c=a%b
        a=b
        b=c
    print("the GCD is",b)
gcd(a,b)


# In[29]:


#Write a Python function to reverse a list of elements.
l=[1,2,3,4,5,6,7,8,9]
def rev(l):
    a=l[0]
    l[0]=l[-1]
    l[-1]=a
    print(l)
rev(l)    


# In[30]:


#Write a Python function to calculate the sum of digits of a given integer number.
a=input("enter a no: ")
def sum(a):
    global s
    s=0
    for i in a:
        s=s+int(i)
    print(s)
sum(a)


# In[ ]:


#write a Python function to check if a given number is an Armstrong number or not



# In[32]:


#Write Python functions to calculate the area of various geometric shapes such as circle, rectangle, triangle, etc.
r=int(input("enter radius of circle: "))
def area_circle(r,a):
    a=3.14*r**2
    print("area is",a)
area_circle(r,a)


# In[34]:


l=int(input("enter length: "))
b=int(input("enter breadth: "))
def area_rect(l,b,a):
    a=l*b
    print("area of rectangle is",a)
area_rect(l,b,a)


# In[35]:


b=int(input("enter base: "))
h=int(input("enter height: "))
def area_triangle(b,h,a):
    a=1/2*b*h
    print("area of triangle is",a)
area_triangle(b,h,a)


# In[37]:


#write Python functions to perform common string manipulations such as counting the occurrences of a substring, converting to uppercase/lowercase, splitting, joining, etc.
a=input("enter string: ")
def upperlower(a):
    print(a.upper())
    print(a.lower())
upperlower(a)


# In[38]:


def split(a):
    for i in a:
        print(i)
split(a)


# In[39]:


a="whah"
b="iin"
def join(a,b):
    c=a+b
    print(c)
join(a,b)
        


# In[ ]:




