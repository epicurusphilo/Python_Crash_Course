#CH3 Introducing Lists of the book  Python Crash Course:
#https://snhu.skillport.com/skillportfe/main.action?assetid=106768
#2017-10-21

#create a list of names and print them
drawings = ['draw-0001', 'draw-0002', 'draw-0003', 'draw-0004', 'draw-0005']
print ("\nPrint out the list of drawings:")
print (drawings)

#accessing list elements by using index and formatting list item
print ('\nPrint drawing 3 in list: ' + drawings[2].upper())
print ('\nPrint drawing 1 and 4: ' + drawings[0].upper() + " " + drawings[3].upper())
print ('\nPrint the last drawing in the list: ' + drawings[-1].upper())

#adding items to a list using append will add items to the end of the list
drawings.append('draw-ooo6')
print(drawings)

print ("\nList has been appended:\n")
drawing = []
drawing.append('new-draw-0001')
drawing.append('new-draw-0002')
drawing.append('new-draw-0003')
drawing.append('new-draw-0004')
print (drawing)

#inserting items in a list at specific locations
print ("\nInsert new element into the list:\n")
drawing.insert(0, 'new-draw-0000')
drawing.insert(2, 'old-drawing-0001')
print(drawing)

#deleting item from list
print("\nRemove element from the list:\n")
del drawing[0]
print(drawing)

print("\nUsing pop to remove item in list, but still use it:\n")
popped_drawing = drawing.pop()
print (drawing)
print ("Print the popped item to show it can still be used even when removed from list")
print (popped_drawing)

last_drawing = drawing.pop()
print("\nThe last drawing name I used was:\n" + last_drawing.upper())

# Ch3 Avoiding Index Errors When Working with Lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles[2])
print (motorcycles[-1])

motorcycle = ['yamaha R6']
print (motorcycle[-1])












