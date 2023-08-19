import tkinter
from game import Game

window = tkinter.Tk()
window.title("Home Screen")
window.minsize(width=400, height=600)
game_object = Game()


def play_button_clicked():
    window.withdraw()
    game_object.start_game()
    window.deiconify()


def exit_button_clicked():
    window.destroy()


background_image = tkinter.PhotoImage(file="home_screen_images/background.png")
background = tkinter.Label(image=background_image)
background.place(x=0, y=0)

play_image = tkinter.PhotoImage(file="home_screen_images/Start_BTN.png")
exit_image = tkinter.PhotoImage(file="home_screen_images/Exit_BTN.png")

play_button = tkinter.Button(width=150, height=50, highlightthickness=0, borderwidth=0, image=play_image,
                             command=play_button_clicked)
exit_button = tkinter.Button(width=150, height=50, highlightthickness=0, borderwidth=0, image=exit_image,
                             command=exit_button_clicked)

play_button.place(x=125, y=400)
exit_button.place(x=125, y=460)

window.mainloop()
