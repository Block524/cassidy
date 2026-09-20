# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, a number containing the imaginary number i

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters delineated by 2 quote marks

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, specifically containing integers

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, an object used to store multiple pieces of data in a set of pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple (I call it an n-tuple), an ordered list of n pieces of information

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, specifically containing strings

i = True
print(i)
print(type(i)) # i is a boolean, which depicts true or false

j = None
print(j)
print(type(j)) # j is a nonetype data type, representing the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is another list, this time containing 3 different data types

l = str(14)
print(l)
print(type(l)) # l becomes a string, as str() converts a given data type into a string

m = 1e4
print(m)
print(type(m)) # m is a float, depicted using exponential notation

'1. How many different data types did you find?'
'9 different data types'
'2. List all the data types you found'
'int, float, complex, str, list, dict, tuple, boolean, NoneType'
'3. What variables have the same data type?'
'float: b, m'
'str: d, l'
'list: e, h, k'
'4. What was the data type of l? Why is it not an integer? What does str() do?'
'l was a string. Its not an integer because str() converted the integer 14 into a string'
'Look up one more data type not given above. Repeat the same procedure'

n = range(5)
print(n)
print(type(n)) # n is a range data type 

# --- Booleans ---
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, that's a nonempty data set
print(bool(123)) # True, that's a nonempty data set
print(bool(["apple", "cherry", "banana"])) # True, that's a nonempty data set
print(bool(True)) # True, the boolean converted data type of True is true
print(bool(False)) # False, the boolean converted data type of False is false
print(bool(0)) # False, I know that taking the bool of 0 is false, and 1 is true
print(bool("")) # False, it's an empty datatype
print(bool(" ")) # True, it's a nonempty datatype
print(bool(())) # False, it's an empty datatype
print(bool([])) # False, it's an empty datatype
print(bool({})) # False, it's an empty datatype
print(bool(True and False)) # False, true and false == false
print(bool(True and True)) # True true and true == true
print(bool(False and False)) # False, false and false == false
print(bool(True or False)) # True, true or false == true
print(bool(True or True)) # True, true or true == true
print(bool(False or False)) # False, false or false == false
print(bool(not(False))) # True, opposite of false is true
print(bool(not(True))) # False, opposite of true is false

'1. What pattern do you notice about expressions returning True or False?'
'Empty data types, like quotes with no space, or lists with nothing, are false. Things with info are true'
'2. Which expression surprised you about its result?'
'The 3 list types, with tuples, dicts, and lists'
'3'
'bool((True and True) or False)'
'Its true because it takes the logical operators for and, with two trues, leaving a true operating on an or, which guarantees truth'
'bool((True or False) and False)'

# ------ Operators -----

# --- Arithmetic Operators ---
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2, / performs division, converting to float output
print(5 % 2) # 1, % performs mod
print(3 ** 2) # 9, ** performs exponents
print(15 // 2) # 7, // performs integer division, outputting division w/o remainder

# --- Comparison Operators ---
print(5 == 2) # false, 5 is not 2
print(10 != 10) # false, 10 is 10
print(2 < 5) # true, 2 is less than 5
print(12 > 5) # true, 12 is greater than 5
print(5 <= 6) # true, 5 is less than or equal to 6
print(1 >= 10) # false, 1 is not greater than or equal to 10

# --- Assignments Operators ---
x = 5
print(x) # 5
x += 5
print(x) # 10, adds 5 to x
x -= 4
print(x) # 6, subtracts 4 from x
x *= 3
print(x) # 18, multiplies x by 3

# --- Logical Operators ---
# and uses the logical and (if both are true, return true, otherwise return false)
print(True and True)
print(True and False)
# or uses the logical or (if either a or b are true, return true, otherwise return false)
print(False or True)
print(False or False)
# not is the logical inversion (takes a true and returns false, and vice versa)
print(not False)
print(not True)

# --- More Questions ---
# 1. The difference between / and // is that / applies normal division, outputting decimals 
# if the remainder is !0, while // essentially truncates the answer at the ones place
# 2. % gives the modulus, essentially giving the remainder of the division
# while // does division
# 3. I would just use %
print(3 % 2) # outputs a remainder of 1
# 4. Assignment operators take the value (x in x += y), and performs then assigns to x again (assigns x + y to x)

# --- Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(7 * my_string) # Prints: hellohellohellohellohellohellohello
# 1. Slicing means you take a start and end point, and an interval length, so you create a string with the starting letter, then pop out every letter at intervals until the end point
name = "Oski"
print("Hello, my name is", name)
# 2. This appends, then prints a list made of the two different strings
print(f"Hello, my name is {name}")
# 3. Makes a singular string, and prints the singular string

# --- Terminal Commands ---
# cd
# Changes directories. Moves you from folder to folder
# Example: cd desktop
# ls
# Lists files. Lists the files contained in your current directory
# Example: ls
# ls -a
# Lists all files. Includes files otherwise not seen
# Example: ls -a
# mkdir
# Makes directory. Creates an empty folder within your current folder
# Example: mkdir FILENAME
# cat
# Concatenate. Reads the text of the file you choose, lets you look at it without running it
# Example: cat FILENAME
# pwd
# Print working directory. Prints the file path of your current folder
# Example: pwd
# cd ..
# Changes directory to one folder deeper
# Example: cd ..
# cd .
# Changes directory to your current directory
# Example: cd .
# cd ~
# Brings you to root folder.
# Example: cd ~
# cp
# Copies/duplicates a chosen file
# Example: cp SOURCE DIRECTORY
# mv
# Moves a chosen file to a chosen folder
# Example: mv SOURCE DIRECTORY
# rm
# Remove. Deletes a chosen file
# Example: rm CHOSENFILE
# clear
# Clears terminal
# clear
# grep
# Searches a file for a given string of text
# Example: grep PATTERN FILENAME

# 1. 