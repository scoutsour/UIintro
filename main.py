from tkinter import *

root = Tk(); # the window widget I am creating
myLabel1 = Label(root, text = "Hellow World!"); 
myLabel2 = Label(root, text = "My Name is Nick");
#creating a label widget, saying where to put it, and what to say on it

#packing - first available spot of where to go, need to put it in root
# code : myLabel.pack();

#placing is more specific and what we will be using often || note all columns are relative to other labels
myLabel1.grid(row=0, column=0);
myLabel2.grid(row=1, column=0);


#event looping, contantly checking in to see any change mad
root.mainloop();