
from tkinter import *
from datetime import date
root=Tk()
root.title("Otters Club")
root.geometry('350x200')  #width and size
root.resizable(0,0)

img=PhotoImage(file="csumbtransparent.png")
label=Label(root, image=img, width=350, height=200)
label.grid(row=1, column=1)


typingbox=Entry(root)
typingbox.grid(row=2, column=1)

Datebox=Entry(root)
Datebox.grid(row=2, column=2)

Namebox=Entry(root)
Namebox.grid(row=2, column=3)

button1=Button(root, text="Submit your answer", fg='Purple')
button1.grid(row=1, column=1)

label1= Label(root, text="Are you an otter?")        #a label is created to display a question for the user
label1.grid(row=3, column=1)     #this is similar to grid. place is used with x-axis and y-axis. grid is used with columns and rows

label2=Label(root, text="What is your name?")
label2.grid(row=3, column=2)

label3=Label(root, text="   ")
label3.grid(row=3, column=2)

def submit():
   today=date.today()
   age=today.year - int(Datebox.get())
   label2.configure(text="Your age is " + str(age) + "   " + Namebox.get())




root.mainloop()
