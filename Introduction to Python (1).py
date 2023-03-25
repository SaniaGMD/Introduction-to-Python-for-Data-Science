#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Python<center>

# # Hello Python

# Python is a popular high-level programming language that was first released in 1991. It is an interpreted language, which means that it doesn't need to be compiled before running like some other languages. Python is often used for web development, scientific computing, data analysis, artificial intelligence, and automation.
# 
# One of the reasons why Python is so popular is that it is relatively easy to learn and use. Its syntax is straightforward and simple, and it is very readable, which makes it easier for people to collaborate on projects. Additionally, there is a vast amount of documentation, tutorials, and community support available online.

# ## Topics Covered

# - Python Basics
#     - Varaibles and Types
#     - Python Types
#     - Conditional Operators
#     - Logical Operators
#     - Python Lists and its manipulation
# - Python Lists
# - python Functions, Methods and Packages
# - Introduction to Numpy

# ## Python Basics 

# ### Variables and Types

#  A variable is a named container that stores a value, which can be of any data type such as strings, integers, or floating-point numbers. You can assign a value to a variable using the equal sign (=) and use it throughout your code.

# In[75]:


height = 1.79
weight = 68.7
height


# In[76]:


#Calculate BMI
bmi = weight / height ** 2
print(bmi)


# ### Python Types

# float - real numbers <br>
# int - integer numbers <br>
# str - string, text <br>
# bool - True, False<br>

# In[77]:


type(bmi)


# In[78]:


rainbow_colors = 7
type(rainbow_colors)


# In[79]:


x = "this is a string"
y = 'this is a string too'
type(x)


# ### Conditional Operators

# In Python, conditional operators are used to create conditional expressions that evaluate to True or False based on whether a certain condition is met. The most commonly used conditional operators in Python are:<br>
# 
# - '==' --   equal to <br>
# - '!=' --   not equal to <br>
# - '>'  --  greater than<br>
# - '<'  --  less than<br>
# - '>='  --  greater than or equal to <br>
# - '<='  --  less than or equal to <br>

# In[104]:


"hello" == "Hello"


# In[105]:


10 >= 10


# ### Logical Operators

# In Python, logical operators are used to combine conditional expressions into more complex expressions that can be evaluated to True or False. The three logical operators in Python are: <br>
# 
# - and -- Returns True if both expressions are True. <br>
# - or -- Returns True if at least one of the expressions is True.<br>
# - not -- Returns True if the expression is False, and False if the expression is True.<br>

# In[107]:


# and
(3 > 2) and (5 < 3)


# In[108]:


# or
(1 == 2) or (2 == 3) or (4 == 4)


# ### Python Lists

# A list is a collection of ordered(because the elements of a list are stored in a specific index order) and mutable elements, which can be of any data type such as strings, integers, or other objects. Lists are defined using square brackets [] and each element is separated by a comma.

# In[81]:


marks = ["Ali", 99 , "Sara", 99 ,"Zara", 98]
print(marks)


# In[82]:


marks = [["Ali", 99],
         ["Sara", 99],
         ["Zara", 98]]
print(marks)


# In[83]:


#list Type
type(marks)


# ### Subsetting lists

# In[84]:


marks = ["Ali", 99 , "Sara", 99 ,"Zara", 98]
print(marks[0])   # Output: "Ali"
print(marks[1])   # Output: "99"
print(marks[2])   # Output: "Sara"


# ### List slicing

# [start : end]

# In[85]:


print(marks[1:3]) #start is inclusive, end is exclusive
print(marks[3:4])
print(marks[0:])
print(marks[:-1])


# ### Manipulating lists

# - Change list elements
# - Add list elements
# - Remove list elements

# In[86]:


#Change list elements
marks[1] = 92 #changing marks for Ali
print(marks)


# In[87]:


marks[2:4] = ["Sania" , 95]
print(marks)


# In[88]:


#Adding and removing elements
marks = marks + ["Sam" , 96]
print(marks)


# In[89]:


del(marks[7]) #Sam marks removed form list
print(marks)


# ### Functions

# In Python, a function is a named block of code that performs a specific task. Functions are used to break up large programs into smaller, more manageable pieces, and to reuse code that is needed in multiple places.
# 
# Functions in Python are defined using the def keyword followed by the function name, a set of parentheses, and a colon. The function body is then indented and contains the code that the function executes when called. Functions can also take parameters as inputs and return values as outputs.

# In[90]:


def sum(x, y):
    return x + y


# In[91]:


z = sum(2, 9)
print(z)   # Output: 11


# In[92]:


#there as built-in functions as well
len = [1.3, 8.6, 4.5, 3.4]
max(len)


# ### Help

# In[93]:


help(round) # Open up documentation


# In[94]:


round(1.68, 1)


# ![functions](functions.png)

# - round(number)
# - round(number, ndigits)

# ### Find Functions

# - How to know?
# - Standard task -> probably function exists!
# - The internet is your friend

# ### Methods

# In Python, a method is a function that is associated with an object. It is a type of function that is called on an instance of a class, and it operates on the data contained within that instance.
# 
# Methods are defined within a class definition and are accessed using dot notation on an instance of the class. The first parameter of a method is always the object instance itself, conventionally named self, which refers to the instance on which the method is called.

# In[95]:


# String methods
text = "Data Science" 
print(text.upper()) # "DATA SCIENCE"
print(text.lower()) # "data science"
print(text.capitalize()) # "Data science"


# In[96]:


# Lists methods
numbers = [1, 4, 0, 2, 9, 9, 10]
numbers.reverse()
print(numbers) # [10, 9, 9, 2, 0, 4, 1]
numbers.sort()
print(numbers) # [0, 1, 2, 4, 9, 9, 10]


# In[97]:


# Dictionaris methods
ratings = {
    "Ex Machina": 7.7,
    "Mad Max: Fury Road": 8.1,
    "1408" : 6.8
}
print(ratings.keys()) # dict_keys(['Ex Machina', 'Mad Max: Fury Road', '1408'])
print(ratings.values()) # dict_values([7.7, 8.1, 6.8])
print(ratings.items()) # dict_items([('Ex Machina', 7.7), ('Mad Max: Fury Road', 8.1), ('1408', 6.8)])


# ### Packages

# In Python, a package is a collection of related modules that are organized together in a directory hierarchy. A package can contain other packages as well as modules.Packages are a way to organize and reuse code in a modular and scalable way. They allow you to group related functionality together and make it easy to reuse across multiple projects. Packages also make it easy to distribute and install libraries and applications.
# 
# Python has a rich ecosystem of packages and libraries that are available for use, such as NumPy, Pandas, and Matplotlib, to name a few. These packages provide functionality for scientific computing, data analysis, and visualization, among other things.
# - “NumPy” is used for efficiently working with arrays
# - “matplotlib” and “seaborn” are popular libraries used for data visualization
# - “scikit-learn” is a powerful library for machine learning

# ### Installing Packages

# Install package<br>
# http://pip.readthedocs.org/en/stable/installing/ <br>
# Download get-pip.py <br>
# Terminal:<br>
# python3 get-pip.py <br>
# pip3 install numpy <br>

# NumPy arrays and Python lists are both used to store collections of data, but there are some important differences between them:
# 
# - Data type consistency: NumPy arrays are homogeneous, meaning they can only store elements of a single data type, whereas lists can store elements of different data types.
# 
# - Memory efficiency: NumPy arrays are more memory efficient than lists, particularly for large datasets. This is because NumPy stores data in contiguous blocks of memory, whereas lists store references to memory locations.
# 
# - Ease of use: NumPy provides a wide range of mathematical operations that can be performed on arrays without requiring loops, which can simplify code and make it faster. Lists, on the other hand, require explicit iteration to perform operations on their elements.
# 
# - Speed: NumPy is generally faster than lists, particularly for large datasets, because it is implemented in C and uses more efficient memory management.

# In[98]:


import numpy as np
height = [1.73, 1.68, 1.71, 1.89, 1.79]
height = np.array(height)
height


# In[99]:


weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
weight


# In[100]:


bmi = weight / height ** 2
bmi


# In[101]:


#list vs arrays
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])


# In[102]:


python_list + python_list


# In[109]:


numpy_array + numpy_array


# Different types: different behavior!

# ### Continued for Intermediate Python for Data Science
# Lets Connected: https://www.linkedin.com/in/sania-mohiu-ud-din-277047193 <br>
# GitHub: https://github.com/SaniaGMD
