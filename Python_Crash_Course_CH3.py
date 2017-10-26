import sys

#'''
# 2017-10-23 Exercise 3-4 Python Crash Course
# create list called guestNames
guestNames = []

# append the list with 3 guest names
guestNames.append('mark twain')
guestNames.append('richard dawkins')
guestNames.append('charles darwin')

# print the list of guests as proper names
print ("\nPrint the guest list:")
print (guestNames[0].title())
print (guestNames[1].title())
print (guestNames[2].title())
print ("\n")

# send message to each guest
message1 = "Mr." + guestNames[0].title() + " you are invited to the party!\n"
message2 = "Mr." + guestNames[1].title() + " you are invited to the party!\n"
message3 = "Mr." + guestNames[2].title() + " you are invited to the party!\n"
print (message1)
print (message2)
print (message3)

# Exercise 3-5 print guest name who can't attend
print ("\nMr." + guestNames[0].title() + " can't attend the party.\n")

# remove name from list
del guestNames[0]

# add new name
guestNames.insert(0, 'john smith')
message1 = "Mr." + guestNames[0].title() + " you are invited to the party!\n"

# print new set of invites
print (message1)
print (message2)
print (message3)

# Exercise 3-6 adding new guests with insert() at beginning. middle, and end
guestNames.insert(0, 'mike blueth')
guestNames.insert(2, 'buster blueth')
guestNames.insert(5, 'fin ending')
print (guestNames)

message1 = "\nMr." + guestNames[0].title() + " you are invited to the party!\n"
print (message1)
message2 = "\nMr." + guestNames[1].title() + " you are invited to the party!\n"
print (message2)
message3 = "\nMr." + guestNames[2].title() + " you are invited to the party!\n"
print (message3)
message4 = "\nMr." + guestNames[3].title() + " you are invited to the party!\n"
print (message4)
message5 = "\nMr." + guestNames[4].title() + " you are invited to the party!\n"
print (message5)
message6 = "\nMr." + guestNames[5].title() + " you are invited to the party!\n"
print (message6)

# Exercise 3-7 shrink list with pop

pop1 = guestNames.pop(-1)
print ("Mr." + pop1 + " you have been removed from the party.\n")
pop2 = guestNames.pop(-1)
print ("Mr." + pop2 + " you have been removed from the party.\n")
pop3 = guestNames.pop(-1)
print ("Mr." + pop3 + " you have been removed from the party.\n")
pop4 = guestNames.pop(-1)
print ("Mr." + pop4 + " you have been removed from the party.\n")
# print the last two members of the list
print (guestNames)

# delete the final list members to have an empty list
del guestNames[0]
print (guestNames)
del guestNames[0]
print ("\nThe list contains zero items:")
print (guestNames)
#'''

# sorting a list alphabetically
drawings = ['bsg', 'rsg', 'rlr', 'oom', 'lsa', 'cran', 'vde']
print ("Drawings list original:")
print (drawings)
drawings.sort()
print ("\nSorted list:")
print (drawings)

# sorting a list in reverse order
drawings.sort(reverse=True)
print ("\nReverse order sort:")
print (drawings)

# sorting list but only temporarily
print ("\nOriginal list:")
print (drawings)

print ("\nSorted List:")
print (sorted(drawings))

print ("\nOriginal list again:")
print (drawings)

# sorting in reverse order
print ("\nSorting in reverse:")
drawings.reverse()
print (drawings)

# find length of list
print ("\nLength of list:")
print (len (drawings))

# exercise 3-8
locations = ['tokyo', 'london', 'portland', 'california', 'mexico', 'honduras', 'india']
print ("\nList of locations raw:")
print (locations)

# temp sort the list
print ("\nTemp sorted list:")
print (sorted(locations))
print ("\nOriginal list:")
print (locations)

# temp reverse order
print ("\nTemp reverse ordered list:")
print (sorted(locations, reverse=True))
print ("\nOriginal list:")
print (locations)

# reverse order
print ("\nReverse order list:")
locations.reverse()
print (locations)
print ("\nReverse the reverse list:")
locations.reverse()
print (locations)

# alphabetical sort
print ("\nAlphabetical sorted list:")
locations.sort()
print (locations)
print ("\nReverse alphabetical sorted list:")
locations.sort(reverse=True)
print (locations)
# exercise 3-9
print ("\nThe number of locations to visit:")
print (len (locations))

# freestyle, video game ideas: list of enemies
enemyGnawty = ['red', 'blue', 'green', 'brown', 'orange', 'yellow']
print (enemyGnawty)
print (sorted(enemyGnawty))
print (enemyGnawty)
print ("\nFirst Gnawty killed:")
popGnawty1 = enemyGnawty.pop(-1)
print (popGnawty1)
print ("\nNumber of Gnawtys left:")
print (len(enemyGnawty))
print ("\nNames of Gnawtys left: ")
print (sorted(enemyGnawty))