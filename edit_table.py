from tkinter import *
from tkinter import messagebox
from back_main import *

l=login('Data.db')

def find():
    status=0
    e1.config(highlightcolor="black",highlightbackground="black")
    status=l.find(e1_var.get())
    if status==0:
        messagebox.showinfo("Error","Table no is not registerd!!")
        e1.delete(0,END)
        e1.config(highlightbackground="red", highlightcolor="red")
        e1.focus_set()
    else:
        e2_var.set(status[1])
        e3_var.set(status[2])
        e4_var.set(status[3])
        
def edit_tables():
    e4.config(highlightcolor="black",highlightbackground="black")
    status=0
    try:
        if e4_var.get()=="":
            messagebox.showinfo("Error","All Field Should Filled !!")
        else:
            status=l.edit_tables(e1_var.get(),e2_var.get(),e3_var.get(),e4_var.get())
    except:
        messagebox.showinfo("Error","Number fields should be with number only!!")
    if status=='0':
        window.destroy()
        import admin


window=Tk()
window.wm_title("CMS")
window.geometry('1350x700')
window.configure()


l1=Label(window,text="WELCOME TO CMS",font=("times",28,"italic bold"),fg="red",relief='raised',bd=5)
l1.pack(side=TOP,fill=X,padx=10,pady=20)
#select frame
f1=Frame(window,bg="grey",height=100,relief='solid',bd=5)
f1.pack(fill=BOTH,pady=20,padx=10)

#Table No
lab1=Label(f1,text="Table no",font=("times",18,"bold"),fg="black")
lab1.grid(row=1,column=0, padx=5, pady=5)
e1_var=IntVar()
e1=Entry(f1,textvariable=e1_var,font=("times",18),highlightthickness=2)
e1.focus_set()
e1.grid(row=1,column=2,columnspan=3, padx=10, pady=10)

b1=Button(f1,text="Find Details",bg="grey",fg="black",font=("times",20,"bold"),command=find)
b1.grid(row=2,column=2,padx=10,pady=10)


#NO of chairs
lab2=Label(f1,text="No of chairs",font=("times",18,"bold"),fg="black")
lab2.grid(row=3,column=0, padx=5, pady=5)
e2_var=IntVar()
e2=Entry(f1,textvariable=e2_var,font=("times",18),highlightthickness=2)
e2.grid(row=3,column=2,columnspan=3, padx=10, pady=10)

#Price
lab3=Label(f1,text="Price",font=("times",18,"bold"),fg="black")
lab3.grid(row=4,column=0, padx=5, pady=5)
e3_var=IntVar()
e3=Entry(f1,textvariable=e3_var,font=("times",18,'bold'),highlightthickness=2)
e3.grid(row=4,column=2,columnspan=3, padx=10, pady=10)

#Desc
lab4=Label(f1,text="Describe",font=("times",18,"bold"),fg="black")
lab4.grid(row=5,column=0, padx=5, pady=5)
e4_var=StringVar()
e4=Entry(f1,textvariable=e4_var,font=("times",18),highlightthickness=2)
e4.grid(row=5,column=2,columnspan=3, padx=10, pady=10)

b2=Button(f1,text="Edit Table",bg="grey",fg="black",font=("times",20,"bold"),command=edit_tables)
b2.grid(row=8,column=2,padx=10,pady=10)

window.mainloop()
