from tkinter import *
root = Tk()


def myClick():  #how to define a function in python || note auto indent
    myLab = Label(root, text="I clicked")
    myLab.pack()

#very similar to label except we are putting the state
#myButton = Button(root, text="click me", state= DISABLED);
#myButton = Button(root, text="click me", padx=15) the pad just changes size

myButton = Button(root, text="Click me!", command=myClick) # telling it to do whatever function is in command

myButton.pack()

root.mainloop()