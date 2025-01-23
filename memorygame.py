from tkinter import *
import random

def select():
    pass

def new_game():
    pass

def sequence():
    sample = random.sample(range(0,36),6)
    for samp in sample:

        ind = sample.index(samp)+1
        row = int(samp/6)
        column = (samp%6)

        buttons[row][column].config(bg = 'blue')
        buttons[row][column]['text'] = ind
        print(samp, row, column)

def ready():
    pass

window = Tk()

window.title('Sequence Memory Game')

buttons = [

    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],

]


restart_button = Button(text = ('Restart'), font = ('Helvetica', 20), command = new_game)
restart_button.pack(side = 'top')

ready_button = Button(text = ('Ready'), font = ('Helvetica', 20), command = ready)
ready_button.pack(side = 'bottom')

frame = Frame(window)
frame.pack()

for row in range(6):
    for column in range(6):

        buttons[row][column] = Button(frame, text = '', font = ('Helvetica',40), width = 3, height = 1,
                                      command = lambda row = row, column = column:select(row, column))
        buttons[row][column].grid(row=row, column=column)

sequence()
        
window.mainloop()

