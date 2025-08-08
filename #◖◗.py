#◖◗
import random
import tkinter as tk
a = tk.Tk()
a.geometry("800x500")
a.title("擲筊模擬器")
cup = ["◖","◗"]
l = tk.Label(a,text=f"{cup[0]}",font=("",300),fg="tomato")
r = tk.Label(a,text=f"{cup[1]}",font=("",300),fg="tomato")
l.place(x=180,y=10)
r.place(x=410,y=10)
al = tk.Label(a,text="無")
al.place(x=30,y=250)
def go():
    global cup,l,r,al
    a = None
    b = None
    for i in range(15):
        a = random.randint(0,1)
        b = random.randint(0,1)
        l.config(text=f"{cup[a]}")
        r.config(text=f"{cup[b]}")
    if a == 0 and b == 0:
        l.config(fg="tomato")
        r.config(fg="red")
        al.config(text="聖筊")
    elif a == 1 and b == 1:
        l.config(fg="red")
        r.config(fg="tomato")
        al.config(text="聖筊")
    elif a == 1 and b == 0:
        l.config(fg="red")
        r.config(fg="red")
        al.config(text="陰筊")
    elif a == 0 and b == 1:
        l.config(fg="tomato")
        r.config(fg="tomato")
        al.config(text="笑筊")
obj = tk.Button(a,text="擲筊!",font=("",25),command=go)
obj.place(x=350,y=400)
a.mainloop()