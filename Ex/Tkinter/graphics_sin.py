from tkinter import *
from math import sin


root = Tk()
root.title('Schedule table')
root.geometry('1320x640')

canvas = Canvas(root, width=1040, height=640, bg='#002')
canvas.pack(side='right')

for y in range(21):  # grid lines Y
    k = 50 * y
    canvas.create_line(20+k, 620, 20+k, 20, width=1, fill='#191938')

for x in range(13):  # grid lines X
    k = 50 * x
    canvas.create_line(20, 20+k, 1020, 20+k, width=1, fill='#191938')

canvas.create_line(20, 20, 20, 620, width=1, arrow=FIRST, fill='white')  # Oy
canvas.create_line(10, 320, 1020, 320, width=1, arrow=LAST, fill='white')  # Ox

canvas.create_text(20, 10, text="300", fill='white')
canvas.create_text(20, 630, text="-300", fill='white')
canvas.create_text(10, 310, text="0", fill='white')
canvas.create_text(1030, 310, text="1000", fill='white')

label_w = Label(root, text='w:')
label_w.place(x=0, y=10)
label_phi = Label(root, text='phi:')
label_phi.place(x=0, y=35)
label_amp = Label(root, text='amp:')
label_amp.place(x=0, y=60)
label_dy = Label(root, text='dy:')
label_dy.place(x=0, y=85)

entry_w = Entry(root)
entry_w.place(x=50, y=10)
entry_phi = Entry(root)
entry_phi.place(x=50, y=35)
entry_amp = Entry(root)
entry_amp.place(x=50, y=60)
entry_dy = Entry(root)
entry_dy.place(x=50, y=85)

btn_calc = Button(root, text='Calculate')
btn_calc.bind('<Button-1>', lambda event: sinus(float(entry_w.get()),
                                                float(entry_phi.get()),
                                                float(entry_amp.get()),
                                                float(entry_dy.get())))
btn_calc.place(x=10, y=120)

btn_clean = Button(root, text='Clean')
btn_clean.bind('<Button-1>', lambda event: clean())
btn_clean.place(x=100, y=120)

# w = 0.0209
# phi = 20
# amp = 200
# dy = 320


def sinus(w, phi, amp, dy):
    global sin_line
    xy = []
    for _x in range(1000):
        _y = sin(w * _x)
        xy.append(_x + phi)
        xy.append(_y * amp + dy)

    sin_line = canvas.create_line(xy, fill='blue')


def clean():
    canvas.delete(sin_line)


if __name__ == '__main__':
    root.mainloop()
