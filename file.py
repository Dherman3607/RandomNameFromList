from tkinter import *
from tkinter import filedialog
import random
import csv



#choose a CSV file, and then process everyone into their respective tiers.
def chooseFile(tier1,tier2,tier3,tier4):
    fileName = filedialog.askopenfilename()

    with open(fileName) as csvfile:
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


        return allTiers
def clickChooseFile():
    tier1 = []
    tier2 = []
    tier3 = []
    tier4 = []
    chooseFile(tier1,tier2,tier3,tier4)

def clickChooseName():
    pass

#the main function when you click "Choose name" this rolls a random number,
#and will then choose a random name from that list
def chooseName(allTiers):
    print(allTiers)
    text = textBox.get(1.0,END)
    textLength = len(text)


    if textLength >1:
        textBox.delete(1.0,END)

    randomNumber = random.randrange(1,100,1)

    print(randomNumber)
    if randomNumber >= 60:
        print("Tier 4")
        selectFinalName(tier4)
    elif(randomNumber <60 and randomNumber>=30):
        print("Tier 3")
        selectFinalName(tier3)
    elif(randomNumber >30 and randomNumber<= 20):

        print("Tier 2")
        selectFinalName(tier2)
    else:

        print("Tier 1")
        selectFinalName(tier1)

    textBox.insert(INSERT,name)
    textBox.pack()

def selectFinalName(tier):
    pass


allTiers = []
root = Tk()
root.geometry("500x500")
root.title("The Book of Nook")
frame = Frame(root)
frame.pack()
textBox = Text(root)
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text = "Choose File", fg = "red",command = clickChooseFile)
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = "Choose a Name", fg = "brown", command = clickChooseName)


greenbutton.pack( side = LEFT )


clickChooseFile()
root.mainloop()
