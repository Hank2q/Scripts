from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from mover import mover
from os.path import basename as base


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Frame.title = 'Mover'
        self.folder_selected = ''
        select = Button(self, text='Select folder', command=self.select_folder)
        select.pack(side=TOP, pady=8)
        sort = Button(self, text='Move files', command=self.move_files)
        sort.pack(side=TOP, pady=8)

    def select_folder(self):
        self.folder_selected = filedialog.askdirectory()

    def move_files(self):
        if self.folder_selected:
            mover(self.folder_selected)
            showinfo('Done', f'Files in {base(self.folder_selected)} moved successfully')


if __name__ == '__main__':
    root = Tk()
    root.title = ('Mover')
    root.geometry('150x90')
    gui = MyGui(root)
    gui.pack()
    mainloop()
