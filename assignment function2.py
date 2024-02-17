#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a Python function that takes a single argument and returns its square.
def squ(n):
    s=pow(n,2)
    return s
n=int(input("enter a no"))
squ(n)


# In[4]:


#Create a Python function named 'greet' that takes a name as an argument and prints "Hello, [name]!" If no name is provided, it should print "Hello, World!".
def greet(name):
    if len(name)!=0:
        print("hello,",name)
    else:
        print("hello, world")
name=input("enter name")
greet(name)
    


# In[ ]:


#Define a Python function called 'calculate_total' that calculates the total cost of items in a shopping cart.
price=int(input("enter cost of items: "))
def calculate_total(price): #idkk
    total=total+price


# In[22]:


#Implement two Python functions: one named 'print_info' which only takes one argument (name) and prints "Name: [name]", and another function named 'print_details' which takes both 'name' and 'age' as keyword arguments and prints "Name: [name], Age: [age]".
def print_info(name):
    print("\n Name:",name)
def print_details(name,age):
    print(f"\n Name: {name} \n Age: {age}")
name=input("enter name: ")
age=int(input("enter age: "))
print_info(name)
print_details(name,age)


# In[7]:


#Write a Python function called 'calculate_discounted_price' that calculates the discounted price of a product. The function should take the original price as a single argument and apply a default discount of 10%.
cp=int(input("enter original price: "))
def calculate_discounted_price(cp):
    global d
    d=10/100*cp
    print("The discounted price is:",d)
calculate_discounted_price(cp)
    


# In[8]:


#Create a Python function named 'print_items' that accepts any number of arguments and prints each item on a new line.
def print_items(*item):
    print(item)
item=input("enter: ") #idkk
print_items(item)


# In[15]:


#Define a Python function called 'create_person' that accepts keyword arguments such as 'name', 'age', and 'gender', and returns a dictionary containing these details.
name=input("enter name: ")
age=input("enter age: ")
gender=input("enter gender: ")
def create_person(name,age,gender):
    global dict
    dict={"Name":"",
         "Age":0,
         "Gender":""}
    dict["Name"]=name
    dict["Age"]=age
    dict["Gender"]=gender
    print(dict)
create_person(name,age,gender)


# In[18]:


#Write a Python function named 'calculate_area' that calculates the area of a rectangle. It should accept the dimensions as either positional arguments (length and width) or as keyword arguments (length=, width=).

l=int(input("enter length: "))
b=int(input("enter breadth: "))
def calculate_area(l,b):
    global a
    a=l*b
    print("area of rectangle is",a)
calculate_area(l,b) #l=int(input("enter length:")),b=int(input("enter breadth:"))
    


# In[20]:


#Implement a Python function named 'send_email' that accepts keyword arguments such as 'recipient', 'subject', and 'message', and simulates sending an email using these details.
recipient=input("enter name of reciever: ")
subject=input("enter subject: ")
message=input("enter message: ")
def send_email(recipient,subject,message):
    print("\n EMAIL")
    print("Recipient:",recipient)
    print("Subject:",subject)
    print("Message:",message)
send_email(recipient,subject,message)


# In[ ]:


#create a Python function called 'average' that accepts any number of arguments and returns their average
a=input("enter numbers: ")

def avg(a):

