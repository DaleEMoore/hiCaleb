import os

__author__ = "calebw"

# TODO: Prompt the user to guess a number, end when 5 is guessed

a = raw_input("Guess a number between 1 and 10: ")
while a.strip() != '5':
    a = raw_input("Please try again:")

#That part works fine.
if a == '5':
	print("Correct!")
    #This one doesn't. I'm trying to set this so that if the variable is 5, it spits out the "Correct!" string.
