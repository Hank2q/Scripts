from tkinter import *
from gradiant_generator import get_levels
import display_html


def parse_colors(starting_colors, ending_colors, levels, choice):
    sr, sg, sb = int(starting_colors[:2], base=16), int(
        starting_colors[2:4], base=16), int(starting_colors[4:6], base=16)
    er, eg, eb = int(ending_colors[:2], base=16), int(
        ending_colors[2:4], base=16), int(ending_colors[4:6], base=16)

    r_range = get_levels(sr, er, levels)
    g_range = get_levels(sg, eg, levels)
    b_range = get_levels(sb, eb, levels)
    complete = list(zip(r_range[0], g_range[0], b_range[0]))
    complete_hex = [''.join(t)
                    for t in list(zip(r_range[1], g_range[1], b_range[1]))]

    if choice == 1:
        display(complete_hex)
    else:
        display_html.make_html(complete_hex)


def get_colors():
    window = Tk()
    window.geometry('300x400')
    Label(window, text='Enter starting hex color:').pack(pady=8)
    starting_color = Entry(window)
    starting_color.pack(pady=8)
    Label(window, text='Enter ending hex color:').pack(pady=8)
    ending_color = Entry(window)
    ending_color.pack(pady=8)
    Label(window, text='Enter levels of transition:').pack(pady=8)
    levels = Entry(window)
    levels.pack(pady=8)
    Label(window, text='Select where to display the results').pack(pady=8)
    num = IntVar()
    Radiobutton(window, text='GUI', variable=num, value=1).pack(pady=5)
    Radiobutton(window, text='HTML', variable=num, value=2).pack(pady=5)
    Button(window, text='Convert', command=lambda: parse_colors(
        starting_color.get(), ending_color.get(), int(levels.get()), num.get())).pack(pady=8)
    window.mainloop()


def display(hexes):
    root = Tk()
    for color in hexes:
        frame = Frame(root)
        Canvas(frame, bg='#'+color, height=100, width=100).pack(side=TOP)
        # data_string = StringVar()
        # data_string.set("#"+color)
        name = Label(frame, text=f'#{color}', fg="black", bg="white", bd=0)
        name.pack(side=TOP, padx=2)
        frame.pack(side=LEFT)
    root.mainloop()


if __name__ == "__main__":
    get_colors()
