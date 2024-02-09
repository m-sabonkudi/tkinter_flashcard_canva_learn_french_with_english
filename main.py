BACKGROUND_COLOR = "#B1DDC6"
from time import sleep
from tkinter import *
from random import choice
import pandas



chosen = {}

try:
    datas = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = datas.to_dict(orient="records")


def french_word():
    global chosen, timer
    print(data_dict)
    chosen = choice(data_dict)
    chosen_f = chosen["French"]
    screen.after_cancel(timer)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(bg_image, image=front_image)
    canvas.itemconfig(card_, text=chosen_f, fill="black")
    timer = screen.after(3000, english)

def english():
    canvas.itemconfig(bg_image, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_, text=chosen['English'], fill="white")


def is_known():
    print(len(data_dict))
    data_dict.remove(chosen)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    french_word()







screen = Tk()
screen.title("FLASHY")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = screen.after(3000, english)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
bg_image = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_ = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=3)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=french_word)
wrong_button.grid(column=0, row=3)

french_word()




screen.mainloop()



