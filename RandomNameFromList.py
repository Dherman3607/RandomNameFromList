# A python program to let nook import a list of patrons/subscribers, and randomly select 1
#Author: David Herman

#imports
from tkinter import *
from tkinter import filedialog
import random
import csv

#variables
#lists for everyone that is currently in a tier, and then a list of lists for all of them.
tier1 = []
tier2 = []
tier3 = []
tier4 = []
allTiers = []

usedNames = [[],[],[],[]]


#setting up the display window
root = Tk()
root.geometry("500x100")
root.title("Random Name Picker")
frame = Frame(root)
frame.pack()
textBox = Text(root)
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

#the main function when you click "Choose name" this rolls a random number,
#and will then choose a random name from that list
def chooseName(allTiers = allTiers, usedNames = usedNames):

    text = textBox.get(1.0,END)
    textLength = len(text)


    if textLength >1:
        textBox.delete(1.0,END)

    randomNumber = random.randrange(1,100,1)
    if randomNumber >= 60:
        tierIndex = 3
        selectFinalName(allTiers,tierIndex,usedNames)
    elif(randomNumber <60 and randomNumber>=30):
        tierIndex = 2
        selectFinalName(allTiers,tierIndex,usedNames)
    elif(randomNumber <30 and randomNumber>= 20):
        tierIndex = 1
        selectFinalName(allTiers,tierIndex,usedNames)
    else:
        tierIndex = 0
        selectFinalName(allTiers,tierIndex,usedNames)



def selectFinalName(allTiers,tierIndex,usedNames):
    print(tierIndex)
    #determine the length of the list that was passed in
    tierLength = len(allTiers[tierIndex])
    #choose a random index from 0 to tierLength
    if usedNames:
        if len(allTiers[tierIndex]) > len(usedNames[tierIndex]):
            nameIndex = random.randrange(0,tierLength,1)
            name = allTiers[tierIndex][nameIndex]


            while name in usedNames:
                nameIndex = random.randrange(0,tierLength,1)
                name = allTiers[tierIndex][nameIndex]
            else:
                usedNames[tierIndex].append(name)
                textBox.insert(INSERT,name)
                textBox.pack()
        else:
            #Everyone in this group has already been used, and we need to choose another tier
            if sum(map(len,allTiers)) == sum(map(len,usedNames)):
                textBox.insert(INSERT,"You appear to have run out of names.")
                textBox.pack()
            else:
                return
    else:
        nameIndex = random.randrange(0,tierLength,1)
        name = allTiers[tierIndex][nameIndex]
        usedNames[tierIndex].append(name)
        textBox.insert(INSERT,name)
        textBox.pack()
#process the CSV file, in the same directory
with open("supporters.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        print(row[1])
        if row[1]=="1":
            tier1.append(row[0])
            print(tier1)
        elif row[1] == "2":
            tier2.append(row[0])
        elif row[1] == "3":
            tier3.append(row[0])
        elif row[1] == "4":
            tier4.append(row[0])
    allTiers.append(tier1)
    allTiers.append(tier2)
    allTiers.append(tier3)
    allTiers.append(tier4)

greenbutton = Button(frame, text = "Choose a Name", fg = "brown", command = chooseName)
greenbutton.pack( side = LEFT )

root.mainloop()
