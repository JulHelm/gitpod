
#!usr/bin/python3

# to print a string
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