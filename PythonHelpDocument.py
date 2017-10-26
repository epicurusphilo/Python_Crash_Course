import sys

#Learning Python from the user manual. Another round of learning 2017-10-21 - G. Barnett

'''print("\nIf the world is flat then....\n")
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!\n")

input(print("Would you like to learn about fish?\n Enter yes or no:"))

fish_breath_underwater = True
if fish_breath_underwater:
    print("\nDon't take them out of the water!\n")'''

#Using Python as a calculator

print("Let's do some simple math problems to show Python as a calculator!\n")

print("Step 1: 2 + 2 =", 2 + 2, "\n" )

print("Step 2: 40 hours a week - 31.45 hours already worked =", 40 - 31.45, "hours remaining to work!\n")

print ("----------------------------------------------------------------------------\n")

print("Working with division: The first example returns a floating point number\n")

print("Classic Division with float: 365 days / 12 months =", 365 / 12, "days in a month!\n")

print("Floor Division removes fractional: 365 days // 12 months =", 365 // 12, "days in a month!\n ")

print("Return the remainder: 365 days % 12 months =", 365 % 12, "remaining days!\n")

print("Check your work: Result 30 days in a month * 12 months + 5 remaining days =", 30 * 12 + 5, "total days in a year!\n")

print("These calculations show that there are some months with more or less than 30 days!\n")

print("Finding the square of 5 is done with: 5 ** 2 =", 5 ** 2, "\n")

print("Solve for 2 to the power of 10: 2 ** 10 =", 2 ** 10, "\n")

#Assigning values to a variable

print("Find the volume of an aquarium with length (3) * width (1.5) * height (4)=")
length = 3
width = 1.5
height = 4
print(length * width * height, "\n")

print('The girl said, "Doesn\'t that spam look grand?" The boy said "Yes, that is grand spam!"\n') #examples of escape key

spam = "First Spam!\nSecond Spam!"

print(spam, "\n")

spam = "Another taste of spam!"

print(spam, "\n")

print(r"Getting \n raw spam with r!""\n") #ignores escape key (\)

#applying formatting to text by using '''...'''
print("""\
I want formatting! [SPAM]
        -b          A taste of spam in a box
        -B          Even more spam
""")

word = "Python"
print (word[0], "\n") #prints the first letter of the word by using [#]

word = "Spam tastes great, but more spam is better... spam, spam, spam\n"
print (word[0], word[6], word[13], "\n")

print(word.title()) #utilizing methods on a variable by adding .(modifier)

names = "glenn barnett, irina barnett"
print(names.title(), "\n")

#showing how to set variable, concatenate them, and apply a method
firstName = "glenn"
lastName =  "barnett"
fullName = firstName + " " + lastName

print("Hello " + fullName.title() + " welcome to the spam show!\n")

#creating a message within a variable, then calling the variable to print the message
message = "Hello " + fullName.title() + " welcome to the spam show!\n"
print (message)

#using the message variable and adding a tab with "\t"
print ("\t" + message)

#adding a tab and new line with the combination of "\n\t"
print ("\n\t" + message)

#removing whitespace from a string using method .rstrip() and lstrip() right and left strip
spam = " the spam!   "
print (spam.rstrip() + fullName)
print ("\n\t" + spam.lstrip() + fullName.title())




