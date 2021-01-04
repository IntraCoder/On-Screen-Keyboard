from tkinter import *
from tkinter import ttk
import pyautogui

root = Tk()
root.geometry("1300x470")
root.config(bg="black")
root.title("On-Screen Keyboard")
style = ttk.Style()
print(style.theme_names())
style.theme_use("vista")


def press():
    pass


class Buttons:
    def __init__(self, master, text, width=5, height=2, activebackground="white", activeforeground="black", bg='black',
                 fg="palegreen", font="None 13", command=NONE):
        self.root = master
        self.text = text
        self.width = width
        self.height = height
        self.activebackground = activebackground
        self.activeforeground = activeforeground
        self.bg = bg
        self.fg = fg
        self.font = font
        self.command = command
        self.but = Button(self.root, text=self.text, width=self.width, height=self.height, bg=self.bg, fg=self.fg,
                          font=self.font, activebackground=self.activebackground,
                          activeforeground=self.activeforeground, command=self.command)

    def place(self, x, y):
        self.but.place(x=x, y=y)

    def config(self, **arg):
        self.but.config(arg)


# When shift is pressed
def shift_press():
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
        capitalize()




# When Caps_lock or shift is pressed
def capitalize():
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


# TODO -> Row-1
esc = Buttons(root, text="Esc")
f1 = Buttons(root, text="F1")
f2 = Buttons(root, text="F2")
f3 = Buttons(root, text="F3")
f4 = Buttons(root, text="F4")
f5 = Buttons(root, text="F5")
f6 = Buttons(root, text="F6")
f7 = Buttons(root, text="F7")
f8 = Buttons(root, text="F8")
f9 = Buttons(root, text="F9")
f10 = Buttons(root, text="F10")
f11 = Buttons(root, text="F11")
f12 = Buttons(root, text="F12")
prtscr = Buttons(root, text="PrtScr")
insert = Buttons(root, text="Insert")
delete = Buttons(root, text="Delete")
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
delete.place(x=1220, y=0)

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
backspace = Buttons(root, text="Backspace", width=14, height=2)

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
tab = Buttons(root, text="Tab", width=9, height=2, )
q = Buttons(root, text="q", )
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

tab.place(x=0, y=140)
q.place(x=140, y=140)
w.place(x=220, y=140)
e.place(x=300, y=140)
r.place(x=380, y=140)
t.place(x=460, y=140)
y.place(x=540, y=140)
u.place(x=620, y=140)
i.place(x=700, y=140)
o.place(x=780, y=140)
p.place(x=860, y=140)
sqr_bracket_left.place(x=940, y=140)
sqr_bracket_right.place(x=1020, y=140)
backslash.place(x=1100, y=140)

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
enter = Buttons(root, text="Enter", width=12, height=2, )
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
lshift = Buttons(root, text="Shift", width=13, height=2, command=shift_press)
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
rshift = Buttons(root, text="Shift", width=14, height=2, font="None 13", )
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
rshift.place(x=1010, y=300)

# TODO -> Row-6
lctrl = Buttons(root, text="Ctrl", )
fn_key = Buttons(root, text="Fn", )
win_key = Buttons(root, text="Win")
l_alt = Buttons(root, text="Alt")
space = Buttons(root, text="Space", width=35, height=2)
r_alt = Buttons(root, text="Alt")
rctrl = Buttons(root, text="Ctrl")
left_arrow = Buttons(root, text="\u2190", width=5, height=1, )
up_arrow = Buttons(root, text="\u2191", width=5, height=1, )
down_arrow = Buttons(root, text="\u2193", width=5, height=1)
right_arrow = Buttons(root, text="\u2192", width=5, height=1)

lctrl.place(x=0, y=390)
fn_key.place(x=100, y=390)
win_key.place(x=190, y=390)
l_alt.place(x=270, y=390)
space.place(x=350, y=390)
r_alt.place(x=830, y=390)
rctrl.place(x=910, y=390)
up_arrow.place(x=1070, y=375)
left_arrow.place(x=990, y=417)
down_arrow.place(x=1070, y=417)
right_arrow.place(x=1150, y=417)

root.mainloop()
