from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from random import random
import re
import pyinputplus

form = Tk()

form.title("Search for word")
form.geometry('400x400')
form.config(bg='yellow')
form.configure(borderwidth=20)
form.resizable(False, False)

global word
global myList

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()


# Function definition to display an error when the user's input is a number
def TakeTextUser(text):
    if text == int:
        messagebox.showerror(message="Please Enter Just Letter!!!")


# Function definition to display an error when the user's input is a string or greater than 15
def TakeLen(num):
    if num >= 15:
        messagebox.showerror(message="Please Enter a True Number!!!")
    if num == str:
        messagebox.showerror(message="Please Enter just Number")


# Function definition to display an error when the user's input is a string or greater than 2000
def numberOfWord(num):
    if num == str:
        messagebox.showerror(message="Please Enter just Number")
    if num >= 2000:
        messagebox.showerror(message="Enter a True Number")


# Reading the file and separating the words
def readFile(file):
    OpenFile = open(file)
    ReadFile = OpenFile.read()
    SpiltWordInFile = ReadFile.split()
    return SpiltWordInFile


# To return to the first page for another search
def show():
    laAsk.place(x=1, y=30),
    choiceList.place(x=185, y=30),
    choiceList.state(),
    lblTakeLen.place(x=1, y=87),
    takeLenWord.place(x=185, y=87),
    takeLenWord.delete('1.0', END),
    lblNumWord.place(x=1, y=137),
    takeNumWord.place(x=185, y=137),
    takeNumWord.delete('1.0', END),
    btnOk.place(x=134, y=230)
    takeText.place_forget(),
    myList.place_forget(),
    btnTryAGain.place_forget(),
    textLetters.pack_forget(),
    textLetter.pack_forget(),
    btnSearchStarLetters.place_forget(),
    btnSearchStarLetter.place_forget(),
    btnSearchEndLetter.place_forget(),
    btnSearchEndLetters.place_forget(),
    btnSearchLetter.place_forget(),
    btnSearchLetters.place_forget()


# To go to the second page to search for the desired word or words
def public():
    laAsk.place_forget(),
    choiceList.place_forget(),
    takeNumWord.place_forget(),
    takeLenWord.place_forget(),
    lblTakeLen.place_forget(),
    lblNumWord.place_forget(),
    takeText.place(x=95, y=40),
    takeText.delete('1.0', END)
    myList.place(x=110, y=110),
    myList.delete('0', END)
    btnTryAGain.place(x=10, y=320),
    btnOk.place_forget()


# Each of the search types selected, what items to display on the second page
def Choiced(select):
    if select == 'Letter (be every where)':
        public(),
        btnSearchLetter.place(x=130, y=290),
        textLetter.pack(),



    elif select == 'Letters (be every where)':
        public(),
        btnSearchLetters.place(x=130, y=290),
        textLetters.pack(),


    elif select == 'Start Letter':
        public(),
        btnSearchStarLetter.place(x=130, y=290),
        textLetter.pack(),

    elif select == 'Start Letters':
        public(),
        btnSearchStarLetters.place(x=130, y=290),
        textLetters.pack(),

    elif select == 'End Letter':
        public(),
        btnSearchEndLetter.place(x=130, y=290),
        textLetter.pack(),

    else:
        public(),
        btnSearchEndLetters.place(x=130, y=290),
        textLetters.pack(),


# When the user only needs to enter
# one word to search for the desired word, if
# more than one word is entered, an error will be displayed.
def ONLetter(text):
    TakeTextUser(takeText)
    while len(text) >= 2:
        messagebox.showerror(message="Please Enter Just One Letter")
        takeText.delete('1.0', END)
        break


# Search words and display words
# according to user inputs (number of letters in each word, number of words)
# The letters we received from the user may be anywhere in the word
def Letters():
    Text = takeText.get(1.0, 'end-1c')
    NumWord = takeNumWord.get(1.0, 'end-1c')
    LenWord = takeLenWord.get(1.0, 'end-1c')

    OpenFile = readFile('WordsEnglish.txt')
    num = 0
    new = []
    for word in OpenFile:

        if all(x in word for x in Text):
            if len(word) == int(LenWord):
                myList.insert(END, word)
                num += 1
        if num == int(NumWord):
            break


# Search words and display words according
# to user inputs (number of letters in each word, number of words)
# The letter we received from the user may be anywhere in the word
def Letter():
    Text = takeText.get(1.0, 'end-1c')
    NumWord = takeNumWord.get(1.0, 'end-1c')
    LenWord = takeLenWord.get(1.0, 'end-1c')
    ONLetter(Text)
    number = 0

    file = readFile('WordsEnglish.txt')
    for word in file:
        ListWord = [word]
        for Item in ListWord:
            if Text in Item:
                if len(Item) == int(LenWord):
                    myList.insert(END, word)
                    number += 1

        if number == int(NumWord):
            break


# Search words and display words according
# to user inputs (number of letters in each word, number of words).
# The letter we have received is at the end of the words
# displayed to the user.
def EndLetter():
    Text = takeText.get(1.0, 'end-1c')
    NumWord = takeNumWord.get(1.0, 'end-1c')
    LenWord = takeLenWord.get(1.0, 'end-1c')
    ONLetter(Text)
    number = 0

    file = readFile('WordsEnglish.txt')
    for word in file:
        m = [word]
        for Item in m[0][-1]:

            if Text in Item:
                if len(word) == int(LenWord):
                    myList.insert(END, word)
                    number += 1

        if number == int(NumWord):
            break


# Search words and display words according
# to user inputs (number of letters in each word, number of words).
# The letters we have received are at the end
# of the words displayed to the user.
def EndLetters():
    Text = takeText.get(1.0, 'end-1c')
    NumWord = takeNumWord.get(1.0, 'end-1c')
    LenWord = takeLenWord.get(1.0, 'end-1c')

    number = 0
    lenTakeText = len(Text)
    file = readFile('WordsEnglish.txt')
    for word in file:
        m = [word]

        b = int(lenTakeText)

        lenW = m[0][-b:]
        if Text == lenW:

            if len(word) == int(LenWord):
                myList.insert(END, word)
                number += 1

        if number == int(NumWord):
            break


# Search words and display words according to user
# inputs (number of letters in each word, number of words)
# The letters we have received are at the end of
# the words displayed to the user
def StarLetter():
    Text = takeText.get(1.0, 'end-1c')
    NumWord = takeNumWord.get(1.0, 'end-1c')
    LenWord = takeLenWord.get(1.0, 'end-1c')
    ONLetter(Text)
    number = 0

    file = readFile('WordsEnglish.txt')
    for word in file:
        m = [word]

        for Item in m[0][0]:

            if Text in Item:

                if len(word) == int(LenWord):
                    print(Item)
                    myList.insert(END, word)
                    number += 1

        if number == int(NumWord):
            break


# Search words and display words according
# to user inputs (number of letters in each word, number of words).
# The letters we have received are at the beginning
# of the words displayed to the user.
def StarLetters():
    Text = takeText.get(1.0, 'end-1c')
    NumWord = takeNumWord.get(1.0, 'end-1c')
    LenWord = takeLenWord.get(1.0, 'end-1c')

    number = 0
    lenTakeText = int(len(Text))

    file = readFile('WordsEnglish.txt')

    for word in file:
        m = [word]
        if Text == m[0][0:int(lenTakeText)]:

            if len(word) == int(LenWord):
                myList.insert(END, word)
                number += 1

        if number == int(NumWord):
            break


# A list of search types
options = [
    'Letter (be every where)',
    'Letter (be every where)',
    'Letters (be every where)',
    'Start Letter',
    'Start Letters',
    'End Letter',
    'End Letters'

]

clicked = StringVar()

# The text asking the user to select the type of search
laAsk = Label(form, text='Please specify your search type:')
laAsk.place(x=1, y=30)

# List menu for selecting the type of search by the user
choiceList = OptionMenu(form, clicked, *options)
choiceList.place(x=185, y=30)

# The text asking the user
# to enter the number of letters of the desired words
lblTakeLen = Label(form, text="Please Enter Number of letter ")
lblTakeLen.place(x=1, y=87)

# The text asking the user to enter the number
# of letters of the words that the user wants in the search result
takeLenWord = Text(form, width=15, height=1)
takeLenWord.place(x=185, y=87)

# text box taking the number of words the
# user wants in the search result
lblNumWord = Label(form, text="Please Enter Number of Word")
lblNumWord.place(x=1, y=137)

# Getting the number of letters
# of the words that the user wants in the search result.
takeNumWord = Text(form, width=15, height=1)
takeNumWord.place(x=185, y=137)


def v(): Choiced(clicked.get())


btnOk = Button(text='OK', command=v)
btnOk.place(x=134, y=230)

# Text asking the user to enter letter to search for words
textLetter = Label(form, text="Please Enter Your letter:")

# Text asking the user to enter letters to search for words
textLetters = Label(form, text="Please Enter Your letters:")

# Taking letters from the user to search for the desired words
takeText = Text(width=20, height=1, )

# listScroll = Scrollbar(form)

myList = Listbox(form, )

# Search button
btnSearchLetter = Button(form, text='Search', command=Letter)

btnSearchLetters = Button(form, text='Search', command=Letters)

btnSearchStarLetter = Button(form, text='Search', command=StarLetter)

btnSearchStarLetters = Button(form, text='Search', command=StarLetters)

btnSearchEndLetter = Button(form, text='Search', command=EndLetter)

btnSearchEndLetters = Button(form, text='Search', command=EndLetters)

btnTryAGain = Button(form, text='Try again..', command=show)

form.mainloop()
