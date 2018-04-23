import tkinter as tk
# import time

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('650x350+300+200')
    root.title('Schedule table')
    label = tk.Label(root, text='HELLO WORLD!')
    label.place(x=10, y=30)

    btn = tk.Button(root, text='Destroy')
    btn.bind('<Button-1>', lambda event: label.destroy())
    btn.place(x=10, y=60)
    root.mainloop()
