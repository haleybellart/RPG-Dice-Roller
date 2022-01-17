from tkinter import *
from random import *
import os 

window = Tk()

#prepare window
window.wm_title("Dice Roller")
window.geometry("300x100")


#define function to clear previous roll result 
def clear_textbox():
    str(t1)
    t1.delete(1.0, 'end')

#define function to roll dice 
def dice_roll():
    #check to see if value is a number and proceed if true 
    try:
        roll_list = []
        clear_textbox()

        #get inputs 
        dice_type = int(e1_value.get())
        amount_of_dice = int(e2_value.get())
        #This was the old equation I Had issues with logically: total_roll = int((randint(1, dice_type))^int(amount_of_dice))
        for i in range (0, amount_of_dice):
            n = randint(1, dice_type)
            roll_list.append(n)
        print(roll_list)
        total_roll = sum(roll_list)
        t1.insert(END, total_roll)
        print(total_roll)

    #if value is a str, pass 
    except ValueError: 
        pass

#set up GUI
b1 = Button(window, text="Roll!", command=dice_roll)
b1.grid(row=2, column=3)

l1 = Label(window, text="Sides Of Dice:")
l1.grid(row = 1, column = 0 )

l2 = Label(window, text="# Of Dice:")
l2.grid(row = 2, column = 0 )

l3 = Label(window, text="Result:")
l3.grid(row=3, column = 0)

e1_value=StringVar()
e1= Entry(window, textvariable=e1_value)
e1.grid(row=1, column=1)

e2_value=StringVar()
e2= Entry(window, textvariable=e2_value)
e2.grid(row=2, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=3, column=1)


window.mainloop()
