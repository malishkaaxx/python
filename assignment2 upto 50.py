#!/usr/bin/env python
# coding: utf-8

# In[1]:


#16. calculate sum of digits
a=input("enter a multi-digit no: ")
s=0
for i in str(a):
    s=s+int(i)
print(s)


# In[1]:


#17. reverse of items of list
a=["a","b","c"] 
b=[]
for i in range(1,len(a)+1):
    b.append(a[-i])
print(b)


# In[1]:


#18.generate random no betn 1 and 10
import random
gen=random.randint(1,10)
print(gen)


# In[3]:


#19.prime or composite
a=input("enter a no: ") 
a=int(a)
i=1
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1
    else:
        pass
if c==2:
    print("prime")
else:
    print("composite")


# In[2]:


#20. create list of square no from 1 to 5 using a for loop
a=[]
for i in range(1,6):
    a.append(pow(i,2))
print(a)


# In[15]:


#21. remove duplicate from list
l=["ram",2,"shyam","wow",67,9,"ram","d",67]
li=[]
c=0
for i in l:
    if i not in li:
        li.append(i)
    else:
        continue
print(l.replace(li))


# In[16]:


#22. calculate factorial of given no using recursion
a=input("enter a no")


# In[11]:


#23. calculate average of 10,15,20 without using sum() function
a=(10+15+20)/3
print(a)


# In[4]:


#24.count no of vowels in given string
a=input("enter string: ")
c=0
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        c=c+1
print("the no of vowels in the string is",c)


# In[5]:


#25. check if list is empty
s=input("enter items: ")
a=list(s)
print(a)
if len(a)==0:
    print("empty")
else:
    print("not empty")


# In[8]:


b=[]
for i in range(1,5):
    a=input("enter smth: ")
    b.append(a)
if len(b)==0:
    print("empty")
else:
    print("non empty")


# In[13]:


#26.
a='*'
for i in range(1,6):
    print(a)
    a=a+'*'


# In[14]:


for i in range(1,6):
    print('*'*i)


# In[20]:


#27. find the maximum value in a list without using the built-in max() function
a=[1,34,4354,6,7,53,5]
m=a[0]
for i in a:
    if i>m:
        m=i
print("maximum value is",m)


# In[6]:


#28. Write a program that checks if a given string is a palindrome.
a=input("enter string: ")
m=a
r=''
for i in range(1,len(a)+1):
    r=r+a[-i]
if m==r:
    print("palindrome")
else:
    print("not palindrome")


# In[20]:


#29. Calculate the product of the first five prime numbers 
a=1
p=1
for i in range(1,10):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c<=2:
        p=p*i
print(p)


# In[22]:


a=1 #alternate if range is more but we only need first five 
p=1
end=0
for i in range(1,100):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c<=2:
        p=p*i
        end=end+1
    if end==5:
        break
print(p)


# In[10]:


#30. Create a tuple with the elements 3, "apple", and True
 
a=(3, "apple", True)
type(a)


# In[13]:


#31. checks if a number is positive, negative, or zero.
a=int(input("enter a no: "))
if a>0:
    print(a,"is positive")
elif a<0:
    print(a,"is negative")
else:
    print(a,"is zero")


# In[22]:


#32. sum of the digits of the product of 6 and 7
a,b=6,7
p=str(6*7)
s=0
for i in p:
    s=s+int(i)
print("sum of digit is",s)


# In[25]:


#33. Remove the element "apple" from a list of fruits
l=["banana","litchi","apple","strawberry","avocado"]
l.remove("apple")
print(l)


# In[30]:


#34. Create a dictionary with keys as fruits and values as their respective colors
d={
    "apple":"red",
    "banana":"yellow",
    "watermelon":"green",
    "mango":"yellow",
    "stwarberry":"red"
}
print(d)


# In[31]:


#35. print the numbers from 1 to 20, but skip multiples of 3.
for i in range(1,21):
    if i%3==0:
        continue
    else:
        print(i)


# In[23]:


#36. leap year using function
a=int(input("enter a year: "))
def leapyr(a):
    if a%4==0 and a%100!=0 or a%400==0:
        print("leap year")
    else:
        print("not leap year")
leapyr(a)


# In[36]:


#37. Convert the string "hello" to uppercase
a="hello"
print(a.upper())


# In[7]:


#38. o find the common elements between two lists.
a=["app",8,3,56,9,23,"fat"]
b=["what","oo",8,3,6,56,"fat",2]
l=set(a)
li=set(b)
print(l.intersection(li))


# In[41]:


#39. Check if a given character is a vowel.
n=input("enter a character: ")
if n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='A' or n=='E' or n=='I' or n=='O' or n=='U':
    print("vowel")


# In[43]:


#40.Calculate the area of a circle with radius 3.14
r=3.14
area=3.14*r*r
print(area)


# In[45]:


#41. Create a program that prints the sum of even numbers from 1 to 10.
s=0
for i in range(1,11):
    if i%2==0:
        s=s+i
print("sum of even no from 1 to 10 is",s)


# In[4]:


#42. Check if a number is a perfect square.
a=int(input("enter a no: "))
b=a**2
if b%a==0:
    print("perfect square")
else:
    print("not perfect square")


# In[16]:


#43. swap the first and last elements of a list.
a=[1,2,3,4,5,6,7,8,9]
c=a[0]
a[0]=a[-1]
a[-1]=c
print(a)


# In[18]:


#44. Calculate the factorial of the sum of 4 and 5
a,b=4,5
s=a+b
f=1
for i in range(1,s+1):
    f=f*i
print(f)


# In[16]:


#45. Write a function that takes two numbers as parameters and returns their sum.
def sum(a,b):
    s=a+b
    print("sum is",s)
a=int(input("enter first no: "))
b=int(input("enter 2nd no: "))
sum(a,b)


# In[8]:


#46. Check if a list contains only unique elements.
a=[1,2,3,4,5,6,7,4,2,9,6]
s=set(a)
if s


# In[19]:


#47. Create a program that prints the Fibonacci series up to 10 terms.
a=1
b=2
print(a)
print(b)
for i in range(1,9):
    c=a+b
    print(c)
    a=b
    b=c
    


# In[24]:


#48. Write a program that generates a random password of length 8 containing letters and digits.


# In[21]:


#49. Write a program that checks if a number is divisible by both 2 and 3.
a=int(input("enter a no: "))
if a%2==0 and a%3==0:
    print("divisible by both 2 and 3")
else:
    print("not divisible by both 2 and 3")


# In[ ]:


#50. Create a program that prints the square of numbers from 1 to 5 in a formatted way

