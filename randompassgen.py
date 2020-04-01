import random
import pyperclip
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


root = Tk()
def MyShuffle(password):
    password1=''
    password2=[i for i in password]
    random.shuffle(password2)
    for i in password2:
        password1=password1+i
    print(password1)
    return password1
def take():
    entry2.delete(0,END)
    num1=entry1.get()
    l=int(num1)
    length=strength1.get()
    lower='abcdefghijklmnopqrstuvwxyz'
    digits='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    special='!@#$%^&*()'
    password=''
    if l<5:
        messagebox.showinfo('Random Password Generator','please enter a value greater than 4')
    else:
        if length==1:
            for i in range(l):
                password=password+random.choice(lower)
            password1=MyShuffle(password)
            entry2.insert(0,password1)
        if length==2:
            for i in range(l):
                password=password+random.choice(digits)
            password1=MyShuffle(password)
            entry2.insert(0,password1)
            
        if length==3:
            list1=[int(i) for i in range(1,l)]
            random.shuffle(list1)
            l1=random.choice(list1)
            l2=l-l1
            for i in range(l1):
                password=password+random.choice(digits)
            for i in range(l2):
                password=password+random.choice(special)
            password1=MyShuffle(password)
            entry2.insert(0,password1)
        if length==0:
            messagebox.showinfo('Random Password Generator','please select any one from strength field')

root.configure(bg='black')
root.title('Random Password Generator')
root.geometry('500x300')

##entry screen
label1 = Label(root,text='length').place(x=30,y=50)
label2 = Label(root,text='strength').place(x=30,y=90)

'''radiobutton'''

style=ttk.Style(root)
style.configure('TRadiobutton',background='black',foreground='white',font=('arial',10,'bold'))
##values={'easy':1,'medium':2,'hard':3}
##for text,value in values.items():
##    r1=ttk.Radiobutton(root,text=text,value= value).place(x=value*100,y=90)
strength1=IntVar()
r1=ttk.Radiobutton(root,text='easy',value=1,variable=strength1).place(x=100,y=90)
r2=ttk.Radiobutton(root,text='medium',value=2,variable=strength1).place(x=200,y=90)
r3=ttk.Radiobutton(root,text='strong',value=3,variable=strength1).place(x=300,y=90)
    
label3 = Label(root,text='password').place(x=30,y=130)
num1=IntVar()
entry1 = Entry(root,textvariable=num1)
entry1.place(x=100,y=50)
button2 = Button(root,text='submit',fg='green',command=take).place(x=400,y=90)
entry2 = Entry(root)
entry2.place(x=100,y=130)
button3= Button(root,text='Quit',width=10,command=root.destroy)
button3.place(x=200,y=170)
root.mainloop()
