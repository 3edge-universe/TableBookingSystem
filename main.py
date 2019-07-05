from tkinter import *
from tkinter import messagebox
from back_main import *

l=login('Data.db')

window=Tk()
window.wm_title("CMS")
window.geometry('1350x700')
window.configure()

def select_fun():
    if v1.get()==2:
        window.destroy()
        import cust
        
        
def login_fun():
    status=0
    e1.config(highlightbackground="black",highlightcolor="black")
    e2.config(highlightcolor="black",highlightbackground="black")
    if e1_var.get()=="" or e2_var.get()=="" :
        messagebox.showinfo("Error","All Field Should Filled !!")
        e1.config(highlightbackground="red",highlightcolor="red")
        e2.config(highlightcolor="red",highlightbackground="red")
    elif len(re.findall(r'\w+@\w+\.\w+',e1_var.get()))==0:
        messagebox.showinfo("Error","Email structure is Wrong !! Try Again")
        e1.delete(0,END)
        e1.config(highlightbackground="red", highlightcolor="red")
        e1.focus_set()
    else:
        status=l.login(e1_var.get(),e2_var.get())
        if status==0:
            window.destroy()
            import admin
        elif status==1:
            e2.delete(0,END)
            e2.config(highlightbackground="red", highlightcolor="red")
            e2.focus_set()
        elif status==2:
            e1.delete(0,END)
            e2.delete(0,END)
            e1.config(highlightbackground="red", highlightcolor="red")
            e1.focus_set()
    
    

def register_fun():
    window.destroy()
    from register import register
    register()

l1=Label(window,text="WELCOME TO CMS",font=("times",28,"italic bold"),fg="red",relief='raised',bd=5)
l1.pack(side=TOP,fill=X,padx=10,pady=20)

#select frame
f=Frame(window,bg="grey",height=100,relief='solid',bd=10)
f.pack(fill=BOTH,pady=20,padx=10)

l2=Label(f,text="Choice any option",font=("times",18,"bold"),fg="blue")
l2.grid(row=0,column=0,columnspan=2,pady=20,padx=100)

v1=IntVar()
select=Radiobutton(f,text="Admin Login",value=1,variable=v1,font=("times",18,"italic"),command=select_fun)
select2=Radiobutton(f,text="Customer Panel",value=2,variable=v1,font=("times",18,"italic"),command=select_fun)
select.grid(row=0,column=3,pady=20,padx=10)
select2.grid(row=0,column=4,pady=20,padx=10)
v1.set(1)

# login frame
f1=Frame(window,bg="white",height=400,relief='solid',bd=5)
f1.pack(fill=BOTH,pady=20,padx=10)

#email
lab3=Label(f1,text="Email",font=("times",18,"bold"),fg="black")
lab3.grid(row=1,column=0, padx=5, pady=5)
e1_var=StringVar()
e1=Entry(f1,textvariable=e1_var,font=("times",18),highlightthickness=2)
e1.focus_set()
e1.grid(row=1,column=2,columnspan=3, padx=10, pady=10)

#password
lab4=Label(f1,text="Password",font=("times",18,"bold"),fg="black")
lab4.grid(row=2,column=0, padx=5, pady=5)
e2_var=StringVar()
e2=Entry(f1,textvariable=e2_var,show="*",font=("times",18),highlightthickness=2)
e2.grid(row=2,column=2,columnspan=3, padx=10, pady=10)

b1=Button(f1,text="Login",bg="grey",fg="black",font=("times",20,"bold"),command=login_fun)
b1.grid(row=3,column=0,padx=10, pady=10)
b2=Button(f1,text="Register",bg="grey",fg="black",font=("times",20,"bold"),command=register_fun)
b2.grid(row=3,column=2,padx=10,pady=10)

window.mainloop()
