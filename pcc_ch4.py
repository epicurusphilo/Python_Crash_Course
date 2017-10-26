# CH4 Introducing Lists of the book Python Crash Course:
# https://snhu.skillport.com/skillportfe/main.action?assetid=106768
# 2017-10-225

# Working with lists
# -Looping through a list

users = ['jimmy', 'amanda', 'cleve']
for user in users:
    print (user)

# for loop manages the length of the list and can perform an action with the items in the list
fishes = ['clown', 'trigger', 'damsel', 'tang', 'parrot', 'angel', 'wrasse', 'seahorse', 'eel', 'tuna', 'salmon']
for fish in fishes:
    print ("\nHave you ever seen this fish?: " + fish.title())
    print ("Yes or No?\n")

print ("Those fish can be found in the ocean and are either kept ornamentally or are eaten")

# for loop in a game
characters = ['player 1', 'player 2', 'player 3', 'player 4', 'player 5', 'player 6']
for character in characters:
    print ("Player will fight " + character.title() + " first in the game!\n" )

print ("All players have been defeated! Congratulations!\n")

for fish in fishes:
    print ("The next battle is with: " + fish.title() + "\n")

# forgetting to indent for loop will create an error or not run a second loop line

#Exercise 4-1
# create list then loop through and print some text with the list item
corals = ['anemone', 'polyp', 'zoanthid', 'sinularia', 'colt', 'leather', 'mushroom', 'starburst', 'bubble', 'galaxy']
for coral in corals:
    print ("\n" + coral.title() + " coral")
    print ("\nOne of my favorite corals is the " + coral.title())

# end with a finishing statement outside loop to indicate list has finished
print ("\nI enjoy the many different types of corals within the aquarium hobby and around the world's oceans.")
print ("Because of evolution, some very interesting sessile animals have developed within the sea!")

for coral in corals:
    print ("The " + coral.title() + " is a sessile organism and can be found attached to rocks.\n")

print ("Each coral can be kept in a home aquarium so long as the correct environment and care are provided.")

# numerical lists and loops
# list of number 1-100 multiplied by 10 and printed with statements
for value in range(1,101):
    total = value * 10
    print ("The value of ")
    print (value)
    print ("is equal to: ")
    print (total)
    print ("\n")

print ("You have calculated the number 1 through 100 multiplied by 10!\n")

# use range to create a list of numbers
numbers = list(range(1,101))
print ("The following list of numbers has been created: ")
print (numbers)

# use range to skip numbers
even_numbers = list(range(2, 200, 2))
print (even_numbers)

# put square root of number in a list using a for loop
# create empty list
squares = []
# run for loop and append the list with each cycle within range
for value in range(1,11):
    square = value**2
    squares.append(square)

print ("\nList of squares:")
print (squares)

# do the same square loop but make the code more concise by removing temp variable square
double = []
for value in range(1,101):
    double.append(value * 2)

print ("\nRange of 1-100 doubled and made into a list:")
print (double)

# finding the min and max of a list of numbers
print ("\nThe min double number:")
print (min(double))
print ("\nThe max double number:")
print (max(double))
print ("\nThe sum of the numbers:")
print (sum(double))

# list comprehensions, doing more with less code
evens = [value * 2 for value in range(1,100)]
print (evens)

# Exercise 4-3

for value in range(1,21):
    print (value)

# test github commit
for value in range(1,101):
    print (value)