#CH2 of the book  Python Crash Course: A Hands-on, Project-Based Introduction to Programming  that is found at:
#https://snhu.skillport.com/skillportfe/assetNonSSOLaunch.action?courseName= _ss_chapter:106768-474402415&courseType=7
#2017-10-21


word = "Spam tastes great, but more spam is better... spam, spam, spam\n"

print("\n" + word.title()) #utilizing methods on a variable by adding .(modifier)

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

#exercise 2-3 Personal Message

message = "\n\t" + firstName.title() + ", spam is fun with Python! " + word
print (message)

print (0.2 + 0.1)

print (3 * 0.1)

print (0.1 * 2 )

#use str() to convert non-string integers to string when printing the message as a string
age = 23

message = "\nHappy " + str(age) + "rd Birthday!"
print (message)

#exercise 2-9 Favorite Number
favoriteNumber = 9
print ("\nThe favorite number is " + str(favoriteNumber))

