#                                                              ----------------                                                         written by: JB
#                                    //////////////////////////////////▲\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                                   //////////////////////////// *  WELCOME  * \\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                                  ////////////////////////////       TO         \\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                                ◄||||||||||||||||||||||||||||       PYTON        ||||||||||||||||||||||||||||►
#                                  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\   /--------\   /////////////////////////////
#                                   \\\\\\\\\\\\\\\\\\\\\\\\\\\\\▼/          \▼/////////////////////////////
#                                    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  //////////////////////////////////
#                                                               ----------------

# BASICS

# write a comment within your code by using '#', this allows notes to be added
# these comment lines will be skipped when running your code
#-----------------------------------------------------------------------------
# BASIC DATA TYPES

# data types:
# boolean = True or False
# integer = 2, 8, 46, 400 ◄◄◄◄ whole numbers
# float = 3.2, 26.12 ◄◄◄◄ decimals
# string = word or sentence typed within "" or ''
#------------------------------------------------------------------------------
# OPERATORS

# comparison operators:
# ==    exact equal to
# !=    not equal to
# <     less than
# <=    less than or equal to
# >     greater than
# >=    greater than or equal to

# assignment operators:
#      example:          same as:
# =     x = 5             x = 5
# +=    x += 5          x = x + 5
# -=    x -= 5          x = x - 5
# *=    x *= 5          x = x * 5
# /=    x /= 5          x = x / 5
# %=    x %= 5          x = x % 5
# //=   x //= 5         x = x // 5
# **=   x **= 5         x = x ** 5
# &=    x &= 5          x = x & 5
# |=    x |= 5          x = x | 5
# ^=    x ^= 5          x = x ^ 5
# >>=   x >>= 5         x = x >> 5
# <<=   x <<= 5         x = x << 5

# mathmatical operator

# +     addition
# -     subtraction
# *     multiplication
# /     division
# %     modulous
# **    exponentiation
# //    floor division

# print funtion, when used properly, allows you to
# display items within () to the console

print("Self-taught code is hard work... ")

# Create variable and store a value within it, as seen below, to be used throughout your code
# Variables can also be given new values down the line and will use the new value from there on

learnings = "or is it?"

# Use format string to convert all values such as strings == self type lines within "",
# Booleans == True/False , integers == whole number w/o "", and floats == decimal numbers.
# To use the format string method, use print(f"self written lines {variable}" as shown below

print(f"... {learnings}")

# Leaving an empty print function, like below, leaves a blank line in the console

print()

# if statments are used to run a code block, the line with proper indent under the if line,
# depending on a boolean value, True or False. You can use multiple variables within a line
# of the if statement by using and, or, or. When the if statement does not run the code
# block, you can run a code block under and else: statement... SHOWN BELOW

# Multiple line can be check with runnable code blocks by writing and elif AFTER the
# initial if statement line

if learnings != "or is it?":
  print("I should just give up")
  quit()
else:
  print("I enjoy coding!")
print()

# Create a list value to a variable by creating none or multiple inputs seperate with
# a comma, these can be of any value, and typed within square brackets [] as SHOWN BELOW

learned = [
  "variables", "values", "functions", "booleans", "integers", "floats",
  "strings"
]

# Below shows a for loop. Write your comparison or statement  on the first line
# in this case, i is default for 'iterable'. This runs the code block to print each value
# in the list, one at a time, that has been divided by ',' within the given list. This will
# loop and print, as instructed, each item in the list to the very last value

for i in learned:
  print(i)

# use the input method, as shown below, to get users' input from the console. This is an
# advanced print method in a way where you can write a sentence or question you want to
# dislplay to the console for the user

test = input("answer correctly to continue, what is 2 + 2? ")
lst_functions = [
  "organizing lists", "adding to lists", "list counts", "I'm not huge on lists"
]

# The following shows how to combine lists. You can store it in a variable or print directly

combo = learned + lst_functions

if test == str(4):
  for i in lst_functions:
    print(i)
else:
  print('Wrong answer, try again')
  quit()

print()

#To convert values into a list, use variable.split()

list_convert = "This is how to divide a string into a list"
converted = list_convert.split()

print(list_convert)
print(
  'I used the .split instruction to convert original string into a list containing each item. Displayed below'
)
print()
print(converted)
print()
print('I printed the original variable giving me the string sentence')
print(
  'I then created a new variable and stored the list within the new variable')
print('new_variable = old_variable.split()')
print('Finally, print the new_variable')

# replace part of a string with .replace(), you must add the value that you want to replace
# in the parentheses first then comma and finally add the new value

# self assign the variable using the replace method to keep original variable and keeps
# the update from that point on

print(list_convert.replace('divide a string into', 'replace a value in'))

# divide a string into a list that doesn't have white spaces, website for example
# for a website instance, there are usually /'s and .'s... as shown below
# place the divider you want to split like so .split('/') or seperate two different
# divider characters using and, like this: .split('/' and '.')                  ◄◄◄◄ figured out the 'and' just by messing around with it!

site = 'www.facebook.com/profile/friends/asd5?541'

site = site.split("/" and ".")

print(site)
print()

# use the type() function to find out what data type the value is

type_1 = "Treasure"
type_2 = 46
type_3 = False
type_4 = 99.1

print(type(type_1))
print(type(type_2))
print(type(type_3))
print(type(type_4))
print()

# default values when converting booleans are: 1 = True and 0 = False

value = True

print(int(value), 'is the value for True')

# you can convert any of the following respectively: list, set, tuple, dict

# when converting data types, python will auto convert int's, bool's, and floats but
# combine any of these 3 with a string and a conversion will be necessary

print()

# convert list(s) to a dictionary. When converting, watch for different data types
# that may need converted also

player_1 = [1, 'Justin']
player_2 = [2, 'Alicia']

data = dict([player_1, player_2])

print(data)
print()

# when codes are group together and intended for repeated use, we use def var_name():
# this is called creating a function, run it by callin it. to call it, just type
# 'var_name()' where you want your code to run


def view_players():
  print(player_1)
  print(player_2)


view_players()
print()


def greet_user():
  name = input('Type your name: ')
  print()
  print(f"Hello {name}")


greet_user()
print()

# PARAMETERS

# act as a special variable that stores a value

# passing a parameter inside a funtion looks similar to the above code
# passing paramters is a way to run the same code for different variables
# below is what it looks like


def greet(name):
  print(f"The name {name} was passed as a parameter")


greet("Justin")
print()

# return any type of value from a function by coding the following


def age_label():
  label = input('My age ')
  return label  # using the return function here


# result = age_label("32")   you can store the function in a variable like this
print(
  age_label()
)  # this runs the code block in the funtion in which label is returned then printed
print()

# returning a value is useful because it will run that single line out of multiple within the functions code block

# ///////FUNCTIONS\\\\\\\\\

# you can pass multiple parameters in a function when divided with a comma
# to pass a value to a function with multiple parameter, the parameters must be in order as they are within the function


def get_price():
  first_name = "Final"
  last_name = 'price'
  return first_name + ' ' + last_name


print(get_price())

# locat scopes look like this function below. local scope variables can not be accessed or updated outside of the function


def apply_discount(price):
  discount = 20
  discount = 10
  return price - discount


final_price = apply_discount(50)
print(final_price)
print()

# Just getting through the 'def' functions: here's another way to create one

single_player = True

if single_player:
  player_1 = "Mario"

print(f'Player 1: {player_1}')
print()

# use condition functions to create decisions for passing different parameters in your code.


def total_balance(total):
  if total < 100:
    print(f"Your total is {total}. You will be charged shipping.")
  else:
    print(f"With your total of {total}, your shipping fee will be waived!")

total_balance(150)
print()

# decisions can be made within functions. 'if, elif, else';
# for loops can be nested within functions. 'for loops'; 'while loops'
# lists can be accessed and updated withing functions

def onboard_passengers(bookings):
  counter = 1
  while counter <= bookings:
    print(f'Passengers on board: {counter}')
    counter += 1         # counter -= 1 would display counting backwards from the parameter number given

onboard_passengers(4)
print()

def display_progress(total_files):
  for i in range(total_files):
    print(f'Downloading file {i} of {total_files}')
  
  
display_progress(6)          # assigning parameter for how many times the loop will run
print()

# leave the parameter open so that the function can be coded to the given amount of loops/function output

def display_progress():
  for i in range(3):
    i += 1
    print(f'{i} downloaded of 3')

display_progress()
print()

# iterating thorugh a list using a for loop nested in a function

def half_price(cart):
  for price in cart:
    print(f'Half off price: ${price/2}')

item_price = [48, 220, 182, 10]
half_price(item_price)
print()

# TUPLES

# tuples are good for grouping related data together
# you can't add, remove or update values in tuples. Check the code below

movie_lst = ["Vertigo", "Parasite", 1958, 2019]       # list []

movie_tuple = ("Vertigo", 1958), ("Parasite", 2019)   # tuple ()

print(movie_lst)
print(movie_tuple)
print()

# be sure to seperate data with a comma. 
# if only one peice of data is contained within a tuple, it must end with a comma

one_tuple = ("Larry",)
two_tuple = (1986,)

print(one_tuple)
print(two_tuple)
print()

# we can also store tuples within a list

tup_lst = [("Corvette", 1979), ("Mustang", 1968)]

print(tup_lst)
print()

# one of the main uses for tuples is to call multiple values in a function

# DICTIONARIES

# dictionaries store key-value pairs, key: value. keys can be any data type and very descriptive to the value
# each key can only store one value, each dict can only store 1 key. the value can be any data type including lists
# access the value by calling the var name followed by the key. you can store as many key-values as you'd like
# var_name["key"]

data = {
  "type_1": "string",
  "type_2": False,
  "type_3": 88,
  "type_4": 2.5
}

print(data)
print()

if "type_2" in data:
  print("Current value: ", data["type_4"])
print()

# update a keys value buy calling the var[key] = "new value"

data["type_4"] = 75.25

print("New value is ", data["type_4"])
print()

# you can store a keys value in a variable to be reused

age_dict = data["type_3"]

print("Pulling a stored value from a dictionary:", age_dict)
print()

# for loops can loop through all the keys in a dict

for type in data:
  print(data[type])
print()

# SETS

# sets are a collection of values that can't have any duplicates

unique_valu = {"Jon", "Frank", "Larry", "Paul"}     # this is what a set looks like

unique_valu.add("Tom")     # adds a value to the set

print(unique_valu)
print()

# sets are unordered meaning the values in a set do not have indices
# this means we can not access or update an individual value by an index
# you can check set values using 'in' or view them with a for loop

print("Jon" in unique_valu)
print()
print('Loop through a set')
print()

for name in unique_valu:
  print(f"name: {name}")
print()

print("Converting a list to a set.")
print()

adapters_list = ['USB', 'HDMI', 'VGA', 'DVI', 'HDMI']

print(adapters_list)
print()

print("Notice the duplicates within a list?")
print("Now let's convert to a set.")
print()

print(set(adapters_list))
print()

# you can store the conversion into a variable

adapters_set = set(adapters_list)

print(f"This is printing from a variable that stores the conversion: {adapters_set}")
print()

# you can compare sets to each other using .issubset() which will return a Boolean output
# each comparing set must contain exact values of the shortest set to pass as True
# if even one value does not exist or match the other sets' value, it will result in False

given_adapters = {'HDMI', 'USB'}

print(given_adapters)
print()

compatible = given_adapters.issubset(adapters_set)

print("Now let's check if adapters are compatible by comparing all adapters with the adapters we have.")
print()

print(f"Compatibile? {compatible}. You have {len(given_adapters)} of {len(adapters_set)} compatible adapters.")
print()

print("Notice the result came back true. This is because ALL subset values are stored in the set we compared to.")
print("If even one value is missing or different, it would result in 'false'")
print()

print("I've also included the number of adapters from each set using len()")
print()

# operating with sets
# you can use .union() to join 2 sets together, this will combine duplicate elements into 1 element
# you can use .intersection() to pull only the duplicated into 1 set while combining them into 1 element

apps = {'Tik Tok', 'Facebook', 'Youtube', 'Instagram'}
websites = {'Facebook', 'Youtube', 'Replit'}

print(f'Here is a set containing apps: {apps}')
print(f'Here is a set containing websites: {websites}')
print()

print('I just notices that the console displays sets in alphabetical order.')
print()

print('Lets combine these sets using out 2 operations.')
print()

combined = apps.union(websites)
dups = apps.intersection(websites)

print('Union')
print(combined)
print()

print('This result shows 1 set combining all of the elements and eliminating the duplicates.')
print()

print('Intersection')
print(dups)
print()

print('Our result is that Facebook and Youtube both share elements in websites and apps.')
print()

# .difference()
# use this to find out what elements are in one set and not the other and visa versa

print('We can also get the difference of the 2 sets leaving out any matched elements')
print()

diff = apps.difference(websites)
diff_flip = websites.difference(apps)

print('a.difference(b)')
print(diff)
print()

print('b.difference(a)')
print(diff_flip)
print()

print(f"These are the elements that don't share with each others' sets: {diff.union(diff_flip)}")
print()

# LIST COMPREHENSION

# Editing elements in a list. Using list comprehension to do so creates less code.

numbers = [46, 51, 8, 16, 2, 6]

num_halved_list = [number/2 for number in numbers]  # comprehended list

print('comprehension;', num_halved_list)
print()

num_halved_loop = []
for number in numbers:
  halved_loop = number/2
  num_halved_loop.append(halved_loop)

print('for loop;', num_halved_loop)
print()

print("On the user side we get the same output of the 2 lists above. Behind the scenes, we are using less code.")
print()

def halve(num):
  return num/2

halved_func = [halve(number) for number in numbers]

print('Original:', numbers)
print("Applied function")
print('Halved:', halved_func)
print()

# [expression for loop condition]
# adding a condition to the list comprehension statement

over_12 = [number for number in numbers if number > 12 and number < 50]

print(numbers)
print('Now we will set a condition to get numbers between 12 and 50 from the list above')
move_on = input('Press enter to continue: ')
print()

while move_on == "":
  break

print(over_12)
print()

# list fun

numbers.extend([62, 108, 7, 19, 223])   # .extend allows us to add multiple values

print(numbers)
print()

del numbers[-3]   # del allows us to delete values, note: I used negative indexing

print(numbers)
print()

#del numbers       # uncommenting 'del numbers' will delete all objects within the variable

#del numbers[:]    # deleting a list in full by leaving the slice open [:]

# INDEXING

# Access indices by the following: [start:stop:step]
# in this order, you type the number of the indices position of where you want to start and or stop and or step
# I say and or because leaving any of the index positions open will run it by default
# Example [0:] the zero position is the beginning of the list and will slice through the full list
# [:8] will default at the beginning of the list and access up to the 8th position of the index
# Use step to tell python how you want to access this list given the positions
# example: access every other element by coding [0:26:2]
# Leaving the step position open results in default which is a single step.

num_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = num_count[1::2]
odd_count = num_count[0::2]
thirds_count = num_count[2::3]

print('Full count:', num_count)
print()
print('Evens', even_count)
print('odds', odd_count)
print('Threes', thirds_count)

# CLASSES

# A class is a template that we use to create similar but distinct things

class Computer:                      # CLASS
  def __init__(self, size, storage): # DEFINITION
    self.size = size            # Variable within the definithion
    self.storage = storage

  def print_specs(self):
    print("Display size: " + self.size)
    print("Storage size: " + self.storage)

low_spec = Computer("13", "256GB")       # low_spec is the INSTANCE here
high_spec = Computer("27", "1TB")

print("Low Spec Computer:")
low_spec.print_specs()          # Accessing the defined variable
                                # do so by calling the Instance name followed by a "." then the varible
print("High Spec Computer:")    # that was created within the definition
high_spec.print_specs()         # Instance.Var_Within_def()
print()

# Classes can have functions which are called "Methods"

# Using the, special keyward, "self" parameter

class Virtual_Pet:
  color = "brown"              # Variable in a class
  legs = 4
  vocal = "bark"

  def bark(self):              
    print(self.vocal)

  def display_color(self):     # Method, aka function when outside of a class
    print(self.color)          # To use a class method, it's the same as using a variable, just with ()
                               # Use 'self' as a parameter within the method to access variables
  def display_legs(self):
    print(self.legs)

rocky = Virtual_Pet()          # We use self to make class variable scope accessible inside a method
rocky.bark()                   # In other words, we use the keyword self when we need to access a var or method inside of a class def
rocky.display_color()
rocky.display_legs()
print()

# you can create variables and functions in class definitions

# CONSTRUCTOR METHODS

# A constructor method looks like this, __init__()
# A class definition will always have the same value
# A constructor method allows us to create the value
# The purpose of a constructor is to create an instance of a class object with unique class variables

class virtual_pet_const:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

#  def display_color(self) *****
#    print(self.color)     *****

zues = virtual_pet_const("Black", 4) # This is where you construct your unique values. It is required to type your values
print(zues.color)                    # in the order which the parameter is layed out in the constructor method
print(zues.legs)                     # while true, skip the self parameter for no value get's attached to it.
#zues.display_color        *****  
print()

# The '*****' above displays another way to access specific parameters from another place in the class definition using self

# ENCAPSULATING OBJECTS

# Encapsulation is when the data and the function(s) are grouped together in an object.

# Different styles of coding are called paradigms.

# Functional programming (FP) is a common style

'''
def getTotal(a, b):
  return a + b

num1 = 2
num2 = 3
total = getTotal(num1, num2)
print(total)
'''

# In FP style, the data and the functionality are seperate. FP also returns new values then used in the code somewhere else.

# Object-oriented programming (OOP) groups data and functionality as properties and methods inside the object.

'''
class Dog:
  name = "Fido"
  hungry = False

  def eat(self):
    self.hungry = True
'''
###
# Applying inheritance
###

# Using inheritance, classes recieve methods from other classes.
# This makes our code more efficient

'''
class Parent:
  def __init__(self):     
    self.eyes = "green"

class Child(Parent):    ◄ This is where the Child class inherits the properties from the Parent class
  def __init__(self):
    super().__init__()  ◄ This line accesses the constructor Method from the Inherited class
    self.age = 7

child = Child()
print(child.eyes)
print(child.age)
'''

# super().__init__()

# SUPER refers to the parent class of Child : __init__ refers to the Parent cunstructor with parameters

'''
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

class Student(Person):

  def __init__(self, name, age, major)
    super().__init__(name, age)        NOTE: self is not used here because it's defined to the Person class
    self.major

student = Student("Sam", 23, "chemistry")
print(student.major)
student.greet()
'''

# In short, Methods and will be repeated should be inherited to eliminate repetitive code.

# ABSTRACTING OBJECTS

'''
class Car:

  def injectFuel(self):
    print("Spraying fuel")

  def igniteFuel(self):
    print("Boom!")

car = Car()
car.injectFuel()
car.igniteFuel()
car.injectFuel()
car.igniteFuel()
'''

# The above would be a bad way to write code that you want to continuously run
# Better example of this would look like the below code.

'''
class Car:
  def __init__(self):
    self.on = False

  def injectFuel(self):     {
    print("Spraying fuel")    
                              LOW-LEVEL functionality
  def igniteFuel(self):       
    print("Boom!")          }

  def startUp(self):     {
    self.on = True       
    while self.on:          CORE METHOD
      self.injectFuel()  
      self.igniteFuel()  }
'''

# Abstraction allows developers to use a class 
# without having to know what low-level methods it has or how they even work

# POLYMORPHIC OBJECTS

# Methods represent behaviors.
# With inheritance we can extend the funionality to a child's class.
# Parents class methods may not always be accurate for the subclass.
# You can override the parents method by creating the accurately needed method within the subclass.

'''
class Feline:
  def speak(self):
    print("Meow")

class Cat(Feline):
  def lick(self):
    print("Licking paw")

class Lion(Feline):
  def prey(self):
    print("Pounces on prey")
  def speak(self):          # Overrided the parent speak method
    print("ROAR!")

cat = Cat()
cat.speak()    ◄ Logs Meow
lion = Lion()
lion.speak()   ◄ Logs ROAR!
'''

# MODULES

# Add more organization to our code by calling a module.
# Modules usually contain lots of classes
# help('module_name') displays the functionalities for the module given

# 'import' followed by module name
# import math

'''
import math

print("The value of pi is")
print(math.pi)

print("The square root of 16 is")
print(math.sqrt(16))
'''

'''
import pygal       

pie = pygal.Pie()
pie.title = "Time spent on social networks"
pie.add("Twitter", 47)
pie.add("Facebook", 23)
pie.add("Instagram", 30)

pie.render_in_browser()
'''

# We can also import direct functionality like below
# from math import pi
# this creates clean efficient code because we don't need to add the module name as part of our code.

'''
from math import pi

print("The square rood of 16 is")
print(pi)
'''

# We can modify the name of the modules that we import by coding the following

'''
import statistics as stats

sales = [23, 43, 26, 26, 29, 18, 24]

median = stats.median(sales)
print(median)
'''

# It's good to modify the module name so that they don't interfere with variable in our code

# ////////ERRORS AND EXCEPTIONS//////////

# Syntax Errors are usually due to misspelled words

# Incorrect indentation will result in an indentation error

# Putting a keyword in the wrong place will throw a syntax error
# Leaving out symbols, such as colons and brackets, will also throw a syntax error
# Incomplete statements will throw a syntax error

# Exceptions are called by python when an operation can not be performed

'''
share = size/6
'''

# A 'Traceback' is an exception that has been raised.
# This helps us debug our code, which means finding errors

# ZeroDivisionError, NameError and TypeError are all examples of different types of exceptions

# Objects may not have attributes that we think they have
# An exception will be raised called AttributeError
# For example, finding the mean in a list when it doesn't exist

# The console displays the Traceback from bottom to top, to help understand what went wrong with our code

# ModuleNotFoundError is displayed when Python cannot find a module
# An out of range index will throw an IndexError
# NameErrors are thrown when a name in the code has not been defined as a variable
# Unexpected EOF (End Of File)

# You can code a statement to raise and exception

'''
slice = 18
diners = 0

if diners < 1:
  raise Excetion("There must be at least one diner")
else:
  slices_each = slices / diners
'''

# We can also raise ValueError

# Typically we want our program to run even when we encounter exceptions.
# A try and except code block can be used for exception handling

'''
try:
  login(user)

except:
  print("User not know, please try again")
'''

# We can also use 'pass' as the code statement after the except statement if you don't want anything to print

# we can use an else statement after the try and except statements to execute if no exceptions are raised

# We can also use a finally statement at the end of the try, except, else code blocks.
# This allows us to run more code regardless of execution from the other code blocks




















































































































