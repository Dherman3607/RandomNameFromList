# A python program to let nook import a list of patrons/subscribers, and randomly select 1
#Author: David Herman

#imports
from tkinter import *
from tkinter import filedialog
import random
import csv
import itertools

#variables
#lists for everyone that is currently in a tier, and then a list of lists for all of them.
tier1 = []
tier2 = []
tier3 = []
tier4 = []
allTiers = []

usedNames = []


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
def chooseName(allTiers = [], usedNames = []):
    print('inside choose name, usedNames is :')
    print(usedNames)
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
    #determine the length of the list that was passed in
    tierLength = len(allTiers[tierIndex])
    #choose a random index from 0 to tierLength
    if sum(map(len,allTiers)) >0:
    #there is still a name in this tier.
        if tierLength >0:
            nameIndex = random.randrange(0,tierLength,1)
            name = allTiers[tierIndex].pop(nameIndex)
            print(name)
            usedNames.append(name)
            textBox.insert(INSERT,name)
            textBox.pack()
            print(usedNames)
        else:
            #there is no name here, roll again!
            chooseName()
    else:
        print('There are no new names here')


#process the CSV file, in the same directory
with open("supporters.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:

        if row[1]=="1":
            tier1.append(row[0])

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

def saveNamesToFile(usedNames):
    savedFile = filedialog.asksaveasfilename(title = 'Select file to save as', filetypes = (('csv files',"*.csv"),))
    with open(savedFile,mode='w',newline = '\n') as file:
        file_writer = csv.writer(file,delimiter =",")

        file_writer.writerow(usedNames)

def loadNamesFromFile(usedNames):
    usedNamesTemp = []
    loadedFile = filedialog.askopenfilename(title = 'Select File', filetypes =(( "CSV File",'*.csv'),))
    with open(loadedFile) as File:
        csv_reader = csv.reader(File,delimiter = ',')
        for person in csv_reader:
            if person:
                usedNamesTemp.append(person)

        usedNames = usedNamesTemp
    print('After loading the file usedNames looks like:')
    print(usedNames[0])


def saveFileClick():
    saveNamesToFile(usedNames)

def loadNamesClick():
    loadNamesFromFile(usedNames)

def chooseNameClick():

    print('When clicking to choose a name')
    print(allTiers)
    print(usedNames)
    chooseName(allTiers,usedNames)
chooseButton = Button(bottomframe, text = "Choose a Name", fg = "blue", command = chooseNameClick)
chooseButton.pack( side = LEFT )

saveButton = Button(frame, text = "Save Names", fg = "blue",command = saveFileClick)
saveButton.pack(side = LEFT )

loadButton = Button(frame, text = "load Names", fg = "blue", command = loadNamesClick)
loadButton.pack(side = RIGHT )
root.mainloop()
