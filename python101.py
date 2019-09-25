#!usr/bin/python3

# to print a string
from ipython_genutils.testing.decorators import skip_if_no_x11
from rx.linq.enumerable import whiledo
from rx.linq.observable import ifthen

print("Strings and things:")
print('Hello world')
print("""Hello, this is
a multiline string.""")
print("This is" + " a string")
print('\n')  # new line

# Math
print("Math time:")
print(50 + 50)
print(50 - 50)
print(50 * 50)
print(50 / 50)
print(50 + 50 - 50 * 50 / 50)
print(50 ** 2)
print(50 % 6)
print(50 // 6)  # number without leftover = modulo erster teil quasi

# variables + methods
print("variables + methods:")
quote = "All is fair in love and war"
print(quote)
print("Anzahl Buchstaben: " + str(len(quote)))
print(quote.upper())
print(quote.lower())
print(quote.title())
name = "Heith"
age = 29  # int int(29)
gpa = 3.7
print(int(age))
print(int(29.9))  # int rundet nicht, laesst nur weg
print("May name is: " + name + " and I am " + str(age) + " years old.")
print("\n")
age += 1
print(age)
birthday = 1
age += birthday
print(age)
print("\n")

# Functions
print("Some Functions:")


def who_am_i():
    name1 = "Heith"
    age = 29
    print("May name is: " + name1 + " and I am " + str(age) + " years old.")


who_am_i()


# adding in parameters
def add_one_hundred(num):
    print(num + 100)


add_one_hundred(2)


# add in multiple parameters
def add(x, y):
    print(x + y)


add(7, 7)
add(21, 88)


# using return
def multiply(x, y):
    return x * y


print(multiply(7, 7))


def square_root(x):
    return x ** .5

def nl():
    print("\n")


print(square_root(7))
nl()
# boolean expression (True or False)
print("boolean expression (True or False):")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9
print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = 'True'
print(type(bool5))
nl()

#relational and boolean Operators
print("#relational and boolean Operators")
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = ( 7 > 5 ) and ( 8 < 7)
test_or =  (7 > 5 ) or ( 5 < 7)
test_not = not True
print(test_and, test_or, test_not)

#conditional statements
print("conditional statements")

def soda(money):
    if money >= 5:
        print("soda gekauft")
    else:
        print("soda nicht gekauft")

soda(2)
soda(9)

def alcohol(age, money):
    if (age >=21) and (money >= 5):
        return "We are gettin tipsy!"
    elif (age >=21) and (money < 5):
        return "Come back with more money"
    elif (age < 21) and (money >= 5):
        return "too young"
    else:
        return "go home"

print(alcohol(22, 9))
print(alcohol(6, 9))

nl()
# lists
print("lists have brackets")

movies = ["hangover", "perps", "googles"]
print(movies)
print(movies[1])
print(movies[0:2])      #man muss die letzte ziffer um 1 erhöhen falls man die wirklich haben will
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("jaws")
print(movies)
movies.pop()        #removes last
print(movies)
movies.pop(1)
print(movies)

movies = ["hangover", "perps", "googles"]
person = ["julian", "jake", "leah"]

combine = zip(movies, person)
print(list(combine))
nl()

#tupels
print("tupels have parantheses and cannot be changed:")         #means immutable
grades = ("A", "B", "C", "D", "E", "F")
print(grades[0])
nl()

#looping
print("loops:")
liste = [1, 4, 7, 8]
for zahl in liste:
    print(zahl)

i = 1
while i <= 10 :
    print(i)
    i += 1


