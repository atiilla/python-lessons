# Basic Syntax and Data Types

# 1. Print Statement
print("Hello World!")

# 2. Variables
# Variables are containers for storing data values.
# Unlike other programming languages, Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5

# 3. Comments
# Comments can be used to explain Python code.
# Comments can be used to make the code more readable.
# Comments can be used to prevent execution when testing code.
# Comments start with a #, and Python will render the rest of the line as a comment:
# This is a comment.
print("Hello, World!")

# 4. Multi Line Comments
# Python does not really have a syntax for multi line comments.
# To add a multiline comment you could insert a # for each line:
# This is a comment
# written in
# more than just one line
print("Hello, World!")

# 5. Docstrings
# Python also has extended documentation capability, called docstrings.
# Docstrings can be one line, or multiline.
# Unlike regular comments, docstrings are not ignored by the Python interpreter.
# They are specified in source code that is used to generate documentation for a module,
# function, class or method.
# Docstrings are accessible from the doc attribute for any of the Python object and also with the built-in help() function
# They are written within triple quotes.
# They can be accessed using the __doc__ method of the object or using the help function.
# The docstrings are associated with the object as their __doc__ attribute.
# The docstrings can be accessed using the __doc__ attribute of the object or using the help function.
# The docstrings are written within triple quotes.
# They can be one line, or multiline.
# Unlike regular comments, docstrings are not ignored by the Python interpreter.
# They are specified in source code that is used to generate documentation for a module, function, class or method.

# 6. Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.
# Indentation is very important in Python.
# Indentation refers to the spaces at the beginning of a code line.
# Where in other programming languages the indentation in code is for readability only,
# the indentation in Python is very important.

# 7. Python Variables
# Variables are containers for storing data values.
# Unlike other programming languages, Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type and can even change type after they have been set.
# Variable names are case-sensitive.
# Variable names must start with a letter or an underscore.
# Variable names cannot start with a number.
# Variable names can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# Variable names cannot contain spaces.
# Variable names should be descriptive, without abbreviations.

# 8. Assign Multiple Values
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 9. Output Variables
# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

# 10. Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# Create a variable outside of a function, and use it inside the function

# 11. The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
# If you use the global keyword, the variable belongs to the global scope:
# Also, use the global keyword if you want to change a global variable inside a function.

# 12. Data Types
# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# 13. Getting the Data Type
# You can get the data type of any object by using the type() function:
x = 5
print(type(x))

# 14. Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex

# 15. Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")  # str
x = int(20)  # int
x = float(20.5)  # float
x = complex(1j)  # complex

# 16. Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1, 10))

# 17. Casting
# Specify a Variable Type
# There may be times when you want to specify a type on to a variable.
# This can be done with casting.
# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
# Casting in python is therefore done using constructor functions:

# 18. Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# 19. Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# 20. Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
names = "John"
print(names[1])

# 21. Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in the word "banana":
for x in "banana":
    print(x)

# 22. String Length
# To get the length of a string, use the len() function.
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# 23. Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
isPresent = "free" in txt
print(isPresent)

# 24. Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
isPresent = "expensive" not in txt
print(isPresent)


# 25. Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
c = slice(b, 2, 5)
print(c)

# 26. Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
c = slice(b, -5, -2)
print(c)

# 27. Modify Strings
# Python has a set of built-in methods that you can use on strings.
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# 28. Lower Case

