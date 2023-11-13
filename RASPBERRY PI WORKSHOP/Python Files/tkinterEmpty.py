from tkinter import *


def leftButton():
    print("You pressed the left one")


def rightButton():
    print("You pressed the right one")


def main():
    root = Tk()
    root.title("Title of your Window")
    root.geometry("300x200")  # width x height
    root.configure(background="white")

    label = Label(root, text="Hi! I am label").pack()
    button = Button(root, text="Button 1", command=leftButton).pack(side=LEFT, fill=Y)
    button2 = Button(root, text="Button 2", command=rightButton).pack(
        side=RIGHT, fill=Y
    )

    root.mainloop()


main()
