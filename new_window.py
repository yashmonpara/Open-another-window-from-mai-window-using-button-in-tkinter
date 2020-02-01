import tkinter as tk

win = tk.Tk()
win.geometry("200x150")

def new_window():
    window = tk.Toplevel()
    a_l = tk.Label(window,text="This Is Another \n Window")
    a_l.pack()

label = tk.Label(win,text="Click Here To Open\n Another Window",
                font=("",15,'bold'))
label.pack()

button = tk.Button(win,text="New Window",command=new_window,
                    font=("",8,'bold'),bg="pink",width=20)
button.pack()

win.mainloop()
