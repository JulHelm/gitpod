#!usr/bin/python3

#Importing
print("Importing is important:")
import sys                                  #system functions and parameters
from datetime import datetime

print(datetime.now())

from datetime import datetime as dt         #importing with alias
print(dt.now())

#Advanced Strings
print("Advanced Strings:")
my_name = "Julian"
print(my_name[0])
print(my_name[-1])
print(my_name[(len(my_name)-1)])

sentence = "This is a sentence!"
print(sentence[:4])
print(sentence[-9:-1])

sentence_split = sentence.split()
print(sentence_split)
sentence_join = " ".join(sentence_split)
print(sentence)
print("\n".join(sentence_split))

quoteception = " I said, 'give me all the money'"
print(quoteception)
quoteception = " I said, \"give me all the money\""
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter.lower() in word.lower())            #improved: caseinsesitive

word2 = "Bingo"
print(letter.lower() in word.lower() and not (letter.lower() in word2.lower()))

too_much_space = "          hello          "
print(too_much_space.strip())                  # strip als default mach leerzeichen weg

full_name = "ulian Helmholz "                  #strings are immutable.
print(full_name.replace("ulian", "Julian"))

print(full_name.find("Helmholz"))

#placeholders
movie = "The Hangover"
print("My favorite movie is '{}'".format(movie))

def book(title, author):
    fav = "My favorite book is \"{}\", which is written by {}.".format(title, author)
    print(fav)

book("Hero", "Paula")