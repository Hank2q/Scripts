import time
from tkinter import *
from sys import exit


def app():
    root = Tk()
    root.title('Move Away')
    root.geometry('350x250')
    Label(root, font=("Helvetica", 15),
          text="You have been sitting for an hour\nGet up and do something for a bit.").pack(pady=20)
    Button(root, text='DONE!', command=root.destroy,
           font=(10), bg='green', fg='white').pack(pady=20)
    Button(root, text='Kill Program', command=exit,
           font=(10), bg='red', fg='white').pack(pady=5)
    root.mainloop()


while True:
    time.sleep(3600)
    app()
