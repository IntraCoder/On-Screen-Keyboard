from tkinter import *
import pyautogui
import os
from tkinter import ttk

lowercaes_letters = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "[", "]", ";", "'", "\\", ",",
                     ".", "/"]
uppercaes_letters = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", ":", '"', "|", "<", ">",
                     "?"]
keylist = []
win_OFF = True
shiftOFF = True
ctrlOFF = True
altOFF = True
FnOFF = True

writeMode_off = True
Caps_lockOFF = True


def writeMode_On():
    global text_area, scrollbar, copy, peast

    root.geometry('1445x470')
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_area = Text(root, height=25, yscrollcommand=scrollbar.set, width=23, bg="grey10", fg="floral white",
                     font=('comic.ttf', 13), insertbackground="white")
    text_area.pack(side=RIGHT, fill=X)
    scrollbar.config(command=text_area.yview)


def writeMode_Off():
    text_area.destroy()
    root.geometry('1225x470')
    scrollbar.destroy()


def pressed(event):
    global shiftOFF, altOFF, ctrlOFF, win_OFF, writeMode_off, Caps_lockOFF, FnOFF
    Button_name = event.widget
    try:
        Button_text = Button_name.cget('text')
        Button_text = Button_text.lower()

    except Exception as e:
        pass
    try:
        if Button_text == "shift":
            if shiftOFF:
                lshift.config(text="Shift", bg="floral white", fg="grey10")
                shiftOFF = False
                shift_press_ON()

            elif not shiftOFF:
                keylist.clear()
                lshift.config(text="Shift", fg='palegreen', bg='grey10')
                shiftOFF = True
                shift_press_OFF()
        elif Button_text == "write mode":
            if writeMode_off:
                write_mode.config(text="Write mode", bg="floral white", fg="grey10")
                writeMode_On()
                writeMode_off = False

            elif not writeMode_off:
                write_mode.config(text="Write mode", bg="grey10", fg="palegreen")
                writeMode_Off()
                writeMode_off = True

        elif Button_text == "caps lock":
            if Caps_lockOFF:
                caps_lock.config(text="Caps Lock", bg="floral white", fg="grey10")
                Caps_lockOFF = False
                uppercaes()

            elif not Caps_lockOFF:
                caps_lock.config(text="Caps Lock", fg='palegreen', bg='grey10')
                Caps_lockOFF = True
                shift_press_OFF()

        elif Button_text == "win":
            if win_OFF:
                win_key.config(text="Win", bg="floral white", fg="grey10")
                win_OFF = False

            elif not win_OFF:
                win_key.config(text="Win", fg='palegreen', bg='grey10')
                win_OFF = True

        elif Button_text == "alt":
            if altOFF:
                l_alt.config(text="Alt", bg="floral white", fg="grey10")
                r_alt.config(text="Alt", bg="floral white", fg="grey10")
                altOFF = False
            elif not altOFF:
                l_alt.config(text="Alt", fg='palegreen', bg='grey10')
                r_alt.config(text="Alt", fg='palegreen', bg='grey10')
                altOFF = True

        elif Button_text == "ctrl":
            if ctrlOFF:
                rctrl.config(text="Ctrl", bg="floral white", fg="grey10")
                lctrl.config(text="Ctrl", bg="floral white", fg="grey10")
                ctrlOFF = False
            elif not ctrlOFF:
                rctrl.config(text="Ctrl", fg='palegreen', bg='grey10')
                lctrl.config(text="Ctrl", fg='palegreen', bg='grey10')
                ctrlOFF = True

        elif Button_text == "fn":
            if FnOFF:
                fn_key.config(text="Fn", bg="floral white", fg="grey10")
                FnOFF = False
            elif not FnOFF:
                fn_key.config(text="Fn", fg='palegreen', bg='grey10')
                FnOFF = True

        elif Button_text == "\u1438":
            pyautogui.press("left")

        elif Button_text == "\u1433":
            pyautogui.press("right")

        elif Button_text == "\u1431":
            pyautogui.press("up")

        elif Button_text == "ptrscr":
            pyautogui.press("printscreen")

        elif Button_text == "\u142f":
            pyautogui.press("down")
        else:
            if not shiftOFF:
                keylist.clear()
                keylist.append('shift')
                keylist.append(Button_text)
                try:

                    Next_key = keylist[1]
                    if Next_key in uppercaes_letters:
                        indexs = uppercaes_letters.index(Next_key)
                        Next_key = lowercaes_letters[indexs]
                        keylist[1] = Next_key

                    pyautogui.hotkey('shift', Next_key)
                    keylist.clear()
                    shiftOFF = True
                    lshift.config(text="Shift", fg='palegreen', bg='grey10')
                    shift_press_OFF()
                except Exception as e:
                    pass

            elif not altOFF:
                keylist.clear()
                keylist.append('atl')
                keylist.append(Button_text)
                try:
                    Next_key = keylist[1]
                    pyautogui.hotkey('atl', Next_key)
                    keylist.clear()
                    l_alt.config(text="Alt", fg='palegreen', bg='grey10')
                    r_alt.config(text="Alt", fg='palegreen', bg='grey10')
                    altOFF = True
                except Exception as e:
                    pass


            elif not win_OFF:
                keylist.clear()
                keylist.append('win')
                keylist.append(Button_text)
                try:
                    Next_key = keylist[1]
                    pyautogui.hotkey('win', Next_key)
                    keylist.clear()
                    win_key.config(text="Win", fg='palegreen', bg='grey10')
                    win_OFF = True
                except Exception as e:
                    pass

            elif not ctrlOFF:
                keylist.clear()
                keylist.append('ctrl')
                keylist.append(Button_text)
                print(keylist)
                try:
                    Next_key = keylist[1]
                    pyautogui.hotkey('ctrl', Next_key)
                    keylist.clear()
                    lctrl.config(text="Ctrl", fg='palegreen', bg='grey10')
                    rctrl.config(text="Ctrl", fg='palegreen', bg='grey10')
                    ctrlOFF = True
                except Exception as e:
                    pass

            elif not Caps_lockOFF:
                keylist.clear()
                keylist.append('caps lock')
                keylist.append(Button_text)
                try:
                    Next_key = keylist[1]
                    pyautogui.hotkey('shift', Next_key)
                    keylist.clear()
                except Exception as e:
                    pass

            elif not FnOFF:
                keylist.clear()
                keylist.append('fn')
                keylist.append(Button_text)
                try:
                    Next_key = keylist[1]
                    pyautogui.hotkey('fn', Next_key)
                    fn_key.config(text="Fn", fg='palegreen', bg='grey10')
                    keylist.clear()
                except Exception as e:
                    pass
            else:
                pyautogui.press(Button_text)


    except Exception as e:
        pass


class Buttons:
    def __init__(self, master, text, width=5, height=2, activebackground="grey30", activeforeground="black",
                 bg='grey10',
                 fg="palegreen", font=(None, 13)):
        self.root = master
        self.text = text
        self.width = width
        self.height = height
        self.activebackground = activebackground
        self.activeforeground = activeforeground
        self.bg = bg
        self.fg = fg
        self.font = font
        self.cget = text
        self.bind = root.bind
        self.borderwidth = 0
        self.highlightbackground = "red"
        self.highlightcolor = "red"
        self.highlightthickness = 0

        self.but = Button(self.root, text=self.text, width=self.width, height=self.height, bg=self.bg, fg=self.fg,
                          font=self.font, activebackground=self.activebackground,
                          activeforeground=self.activeforeground, borderwidth=1)

        self.but.bind("<Enter>", self.enter_size)
        self.but.bind("<Leave>", self.leave_size)

    def place(self, x, y, side=BOTTOM):
        self.but.place(x=x, y=y)

    def config(self, **arg):
        self.but.config(arg)

    def keybind(self):
        self.bind('<Button-1>', pressed)

    def enter_size(self, event):
        self.but.config(borderwidth=3)

    def leave_size(self, event):
        self.but.config(borderwidth=1)


# When shift is pressed
def shift_press_ON():
    twiddle.config(text="~")
    one.config(text="!")
    two.config(text="@")
    three.config(text="#")
    four.config(text="$")
    five.config(text="%")
    six.config(text="^")
    seven.config(text="&")
    eight.config(text="*")
    nine.config(text="(")
    zero.config(text=")")
    minus.config(text="_")
    equal_to.config(text="+")
    sqr_bracket_left.config(text="{")
    sqr_bracket_right.config(text="}")
    backslash.config(text="|")
    semi_colon.config(text=":")
    single_quote.config(text='"')
    comma.config(text="<")
    full_stop.config(text=">")
    division.config(text="?")
    uppercaes()


# When Caps_lock or shift is pressed
def uppercaes():
    q.config(text="Q")
    w.config(text="W")
    e.config(text="E")
    r.config(text="R")
    t.config(text="T")
    y.config(text="Y")
    u.config(text="U")
    i.config(text="I")
    o.config(text="O")
    p.config(text="P")
    a.config(text="A")
    s.config(text="S")
    d.config(text="D")
    f.config(text="F")
    g.config(text="G")
    h.config(text="H")
    j.config(text="J")
    k.config(text="K")
    l.config(text="L")
    z.config(text="Z")
    x.config(text="X")
    c.config(text="C")
    v.config(text="V")
    b.config(text="B")
    n.config(text='N')
    m.config(text="M")


def shift_press_OFF():
    twiddle.config(text="`")
    one.config(text="1")
    two.config(text="2")
    three.config(text="3")
    four.config(text="4")
    five.config(text="5")
    six.config(text="6")
    seven.config(text="7")
    eight.config(text="8")
    nine.config(text="9")
    zero.config(text="0")
    minus.config(text="-")
    equal_to.config(text="=")
    sqr_bracket_left.config(text="[")
    sqr_bracket_right.config(text="]")
    backslash.config(text="\\")
    semi_colon.config(text=";")
    single_quote.config(text="'")
    comma.config(text=",")
    full_stop.config(text=".")
    division.config(text="/")
    q.config(text="q")
    w.config(text="w")
    e.config(text="e")
    r.config(text="r")
    t.config(text="t")
    y.config(text="y")
    u.config(text="u")
    i.config(text="i")
    o.config(text="o")
    p.config(text="p")
    a.config(text="a")
    s.config(text="s")
    d.config(text="d")
    f.config(text="f")
    g.config(text="g")
    h.config(text="h")
    j.config(text="j")
    k.config(text="k")
    l.config(text="l")
    z.config(text="z")
    x.config(text="x")
    c.config(text="c")
    v.config(text="v")
    b.config(text="b")
    n.config(text='n')
    m.config(text="m")


if __name__ == "__main__":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400, 50)

    root = Tk()
    root.geometry("1225x470")
    # root.iconbitmap('icon.ico')
    root.title("On-Screen Keyboard")
    root.config(bg="grey10")
    root.focus_force()
    root.attributes("-topmost", True)
    style = ttk.Style()
    root.resizable(0, 0)

    # TODO -> Row-1
    esc = Buttons(root, text="Esc", height=1)
    f1 = Buttons(root, text="F1", height=1)
    f2 = Buttons(root, text="F2", height=1)
    f3 = Buttons(root, text="F3", height=1)
    f4 = Buttons(root, text="F4", height=1)
    f5 = Buttons(root, text="F5", height=1)
    f6 = Buttons(root, text="F6", height=1)
    f7 = Buttons(root, text="F7", height=1)
    f8 = Buttons(root, text="F8", height=1)
    f9 = Buttons(root, text="F9", height=1)
    f10 = Buttons(root, text="F10", height=1)
    f11 = Buttons(root, text="F11", height=1)
    f12 = Buttons(root, text="F12", height=1)
    prtscr = Buttons(root, text="PrtScr", height=1)
    insert = Buttons(root, text="Insert", height=1)
    esc.place(x=0, y=0)
    f1.place(x=100, y=0)
    f2.place(x=180, y=0)
    f3.place(x=260, y=0)
    f4.place(x=340, y=0)
    f5.place(x=420, y=0)
    f6.place(x=500, y=0)
    f7.place(x=580, y=0)
    f8.place(x=660, y=0)
    f9.place(x=740, y=0)
    f10.place(x=820, y=0)
    f11.place(x=900, y=0)
    f12.place(x=980, y=0)
    prtscr.place(x=1060, y=0)
    insert.place(x=1140, y=0)

    # TODO -> Row-2
    twiddle = Buttons(root, text="`")
    one = Buttons(root, text="1")
    two = Buttons(root, text="2")
    three = Buttons(root, text="3")
    four = Buttons(root, text="4")
    five = Buttons(root, text="5")
    six = Buttons(root, text="6")
    seven = Buttons(root, text="7")
    eight = Buttons(root, text="8")
    nine = Buttons(root, text="9")
    zero = Buttons(root, text="0")
    minus = Buttons(root, text="-")
    equal_to = Buttons(root, text="=")
    backspace = Buttons(root, text="Backspace", width=15, height=2)
    twiddle.place(x=0, y=60)
    one.place(x=100, y=60)
    two.place(x=180, y=60)
    three.place(x=260, y=60)
    four.place(x=340, y=60)
    five.place(x=420, y=60)
    six.place(x=500, y=60)
    seven.place(x=580, y=60)
    eight.place(x=660, y=60)
    nine.place(x=740, y=60)
    zero.place(x=820, y=60)
    minus.place(x=900, y=60)
    equal_to.place(x=980, y=60)
    backspace.place(x=1060, y=60)

    # TODO -> Row-3
    tab = Buttons(root, text="Tab", width=8, height=2, )
    q = Buttons(root, text="q")

    w = Buttons(root, text="w")
    e = Buttons(root, text="e")
    r = Buttons(root, text="r")
    t = Buttons(root, text="t")
    y = Buttons(root, text="y")
    u = Buttons(root, text="u")
    i = Buttons(root, text="i")
    o = Buttons(root, text="o")
    p = Buttons(root, text="p")
    sqr_bracket_left = Buttons(root, text="[")
    sqr_bracket_right = Buttons(root, text="]")
    backslash = Buttons(root, text="\\")
    delete = Buttons(root, text="Delete")

    tab.place(x=0, y=140)
    q.place(x=115, y=140)
    w.place(x=195, y=140)
    e.place(x=275, y=140)
    r.place(x=355, y=140)
    t.place(x=435, y=140)
    y.place(x=515, y=140)
    u.place(x=595, y=140)
    i.place(x=675, y=140)
    o.place(x=755, y=140)
    p.place(x=835, y=140)
    sqr_bracket_left.place(x=915, y=140)
    sqr_bracket_right.place(x=995, y=140)
    backslash.place(x=1075, y=140)
    delete.place(x=1151, y=140)

    # TODO -> Row-4
    caps_lock = Buttons(root, text="Caps Lock", width=10, height=2)
    a = Buttons(root, text="a")
    s = Buttons(root, text="s")
    d = Buttons(root, text="d")
    f = Buttons(root, text="f")
    g = Buttons(root, text="g", width=5, height=2)
    h = Buttons(root, text="h")
    j = Buttons(root, text="j")
    k = Buttons(root, text="k")
    l = Buttons(root, text="l")
    semi_colon = Buttons(root, text=";")
    single_quote = Buttons(root, text="'")
    enter = Buttons(root, text="Enter", width=13, height=2, )
    caps_lock.place(x=0, y=220)
    a.place(x=150, y=220)
    s.place(x=230, y=220)
    d.place(x=310, y=220)
    f.place(x=390, y=220)
    g.place(x=470, y=220)
    h.place(x=550, y=220)
    j.place(x=630, y=220)
    k.place(x=710, y=220)
    l.place(x=790, y=220)
    semi_colon.place(x=870, y=220)
    single_quote.place(x=950, y=220)
    enter.place(x=1030, y=220)

    # TODO -> Row-5
    lshift = Buttons(root, text="Shift", width=13, height=2)
    z = Buttons(root, text="z", )
    x = Buttons(root, text="x")
    c = Buttons(root, text="c")
    v = Buttons(root, text="v")
    b = Buttons(root, text="b")
    n = Buttons(root, text="n")
    m = Buttons(root, text="m")
    full_stop = Buttons(root, text=".", width=5, height=2, font="None 13 bold")
    comma = Buttons(root, text=",", height=2, font="None 13 bold")
    division = Buttons(root, text="/")
    write_mode = Buttons(root, text="Write mode", width=17, height=2, font="None 13", )
    lshift.place(x=0, y=300)
    z.place(x=190, y=300)
    x.place(x=270, y=300)
    c.place(x=350, y=300)
    v.place(x=430, y=300)
    b.place(x=510, y=300)
    n.place(x=590, y=300)
    m.place(x=670, y=300)
    comma.place(x=750, y=300)
    full_stop.place(x=830, y=300)
    division.place(x=910, y=300)
    write_mode.place(x=990, y=300)

    # TODO -> Row-6
    lctrl = Buttons(root, text="Ctrl", )
    fn_key = Buttons(root, text="Fn", )
    win_key = Buttons(root, text="Win")
    l_alt = Buttons(root, text="Alt")
    space = Buttons(root, text="Space", width=40, height=2)
    r_alt = Buttons(root, text="Alt")
    rctrl = Buttons(root, text="Ctrl")
    left_arrow = Buttons(root, text="\u1438", height=1)
    up_arrow = Buttons(root, text="\u1431", height=1)
    down_arrow = Buttons(root, text="\u142f", height=1)
    right_arrow = Buttons(root, text="\u1433", height=1)
    home = Buttons(root, text="Home", height=1)
    end = Buttons(root, text="End", height=1)

    lctrl.place(x=0, y=390)
    fn_key.place(x=100, y=390)
    win_key.place(x=190, y=390)
    l_alt.place(x=270, y=390)
    space.place(x=350, y=390)
    r_alt.place(x=743, y=390)
    rctrl.place(x=824, y=390)
    home.place(x=1145, y=373)
    up_arrow.place(x=985, y=373)
    left_arrow.place(x=905, y=417)
    down_arrow.place(x=985, y=417)
    right_arrow.place(x=1067, y=417)
    end.place(x=1145, y=417)
    a.keybind()
    root.mainloop()
