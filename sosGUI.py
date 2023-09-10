#python gui testing area using tkinter

from tkinter import *
#GUI window
window = Tk()
#title of window
window.title('SOS Game')
#board size & user input
board_size = Label(window, text="Board Size")
board_size.place(x=350, y=0)
board_size_input = Text(window, height=1, width=2)
board_size_input.place(x=420, y=0)
#replay check box
record_game = Checkbutton(window, text="Record Game", onvalue=1, offvalue=0)
record_game.place(x=0, y=350)
#sizes the window and adjusts opening placement
window.geometry('500x400+650+350')
sos = Label(window, text="SOS")
sos.place(x=0, y=0)
#replay and new game buttons
replay = Button(window, text="Replay", width=10)
replay.place(x=400, y=340)
new_game = Button(window, text="New Game", width=10)
new_game.place(x=400, y=370)
#radio buttons
simple_game = Radiobutton(window, text="Simple Game", value=1)
simple_game.place(x=50, y=0)
general_game = Radiobutton(window, text="General Game", value=2)
general_game.place(x=150, y=0)
#simple_game is selected by default
simple_game.select()

#tkinter event loop
window.mainloop()
