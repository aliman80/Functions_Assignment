
 #2. Use of Capitalize()
   name1 = "MUHAmmad Qasim"
   name1.capitalize()
   print(name1)


 # 3. USE OF CASEFOLD()
  firstString = "qasimA"
 secondString = "QASIM" 
 
 if firstString.casefold() == secondString.casefold():
     print('The strings are equal.')
 else:
     print('The strings are not equal.')

 # 4 Center ()
# :returns the string padded with specified fillchar.
# string = "Pakistan is our Country"
  new_string = string.center(30)
  print(new_string)

 # 5 Count() method counts how many times an element has occurred in a list and returns it.¶
  vowels = ['a', 'e', 'i', 'o', 'i', 'u']
 
 count = vowels.count('i')

 print('The count of i is:', count)




# 6  string encode() returns the encoded version of the string.
string = 'Pakistan'

print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

print('The encoded version is:', string_utf)

# 7. Use of endswith
statement = "Islama is our relegion."

result = statement.endswith('relegion.')
# returns False
print(result)

# 8. use of casefold()
 if firstString.casefold() == secondString.casefold():
     print('The strings are equal.')
 else:
    print('The strings are not equal.')
#9 Use of Center ()
 :returns the string padded with specified fillchar.
 string = "Pakistan is our Country"

new_string = string.center(30)
 print(new_string)

# 10 # Count() method counts how many times an element has occurred in a list and returns it.¶
 vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count = vowels.count('i')
# 
# print('The count of i is:', count)

# 11
# Method isdigit(). It gives us whether there is any digit in the string or not.
s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())

# 12 Use of .FORMAT 
s = "282# Use of .FORMAT()

print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))12"# Use of .FORMAT()

print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))


​
# 13 contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.expandtabs())
True
False

str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))
str = "xyz\t12345\tabc"
print('Original String:', str)
​
# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))
Original String: xyz	12345	abc
Tabsize 2: xyz 12345 ab

# 14 use of make trans() and  15 translate()
# first string
string = " Hello Guys and Welcome"
string1 = "abcde"
string2 = "12345"

translation = string.maketrans(string1, string2)
string.translate(translation)

# Ans is ' H5llo Guys 1n4 W5l3om5'


#16 The find() method returns the lowest index of the substring if it is found in given string
statement = "Islam is our relegion."

result = statement. find('relegion.')
# returns False
print(result)

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# 17 use of format_map function

# input stored in variable a. 
a = {'x':"geeksforgeeks", 'y':'b'} 
  
# Use of format_map() function 
print('{x} {y}'.format_map(a))


# 18  str.index(str, beg = 0 end = len(string))


# Python3 program for demonstration   
# of list index() method 
  
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
  
# Will print the index of '4' in list1 
print(list1.index(4)) 
  
list2 = ['cat', 'bat', 'mat', 'cat', 'pet'] 
  
# Will print the index of 'cat' in list2  
print(list2.index('cat'))  ls;p

# 19 The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.
name = "MonicaGeller"

if name.isalpha() == True:
   print("All characters are alphabets")
else:
    print("All characters are not alphabets.")

# 20 The isdecimal() method returns True if all characters in a string are decimal characters. If not, it returns False.
s = '23455'
print(s.isdecimal())
#s = '²3455'
s = '\u00B23455'
print(s.isdecimal())

# 21  The join() is a string method which returns a string concatenated with the elements of an iterable.


numList = ['1', '2', '3', '4']
seperator = ', '
print(seperator.join(numList))

# 22 The islower() method returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False

s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())


# 23 The isidentifier() method returns True if the string is a valid identifier in Python. If not, it returns False.
str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

#24  The string ljust() method returns a left-justified string of a given minimum width.

# example string
string = 'cat'
width = 5

# print left justified string
print(string.ljust(width))

# 25 The replace() method returns a copy of the string where all occurrences of a substring is replaced with another substring.
song = 'cold, cold heart'
print (song.replace('cold', 'hurt'))

#26 The partition() method splits the string at the first occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.

string = "Python is fun"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
 print(string.partition('not '))

 #27  The split() method breaks up a string at the specified separator and returns a list of strings.
 text= 'Love thy neighbor'

# splits at space
print(text.split())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))

# Splitting at ':'
print(grocery.split(':'))

#28 The input() method reads a line from input, converts into a string and returns it.
inputString = input()
print('The inputted string is:', inputString)
# The bytes() method returns a immutable bytes object initialized with the given size and data.
string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)

#29 PEMDAS Equation
    
ans = 2*3+4-1/2


print(float(ans))


