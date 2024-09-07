#For loop in python

name = "Saugat"
for char in name:
    print(char)
    if(char=="g"):
        print(" This is special keyword")

colors=["Red","Green","Blue","Purple"]
for color in colors:
    print(color)
    for char in color:
        print(char)

#Range
#from 0-9
for i in range(9):
    print(i)
#From 1-9, 9 is not included
for i in range(1,9):
    print(i)
#makes difference of two
for i in range(1,9,2):
    print(i)
#makes difference of three
for i in range(1,10,3):
    print(i)