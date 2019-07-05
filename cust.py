from tkinter import *
from tkinter import messagebox

window=Tk()
window.wm_title("CMS")
window.geometry('1350x700')
window.configure()

def view_table():
    window.destroy()
    import view_table_cust   

def viewb_table():
    window.destroy()
    import viewb_table
	
def cancle_table():
    window.destroy()
    import cancle_table



l1=Label(window,text="WELCOME TO Customer Panel",font=("times",28,"italic bold"),fg="red",relief='raised',bd=5)
l1.pack(side=TOP,fill=X,padx=10,pady=20)

#select frame
f=Frame(window,bg="grey",height=100,relief='solid',bd=5)
f.pack(fill=BOTH,pady=20,padx=10)


img=PhotoImage(file="logo.png")
l=Label(f,image=img,bg="black",relief='raised',bd=2)
l.pack(fill=BOTH,ipadx=100,ipady=100)

l2=Label(f,text="Choice Any Option From Menu Bar",font=("times",24,"bold"),fg="blue")
l2.pack(fill=BOTH,pady=20,padx=10)
	
#menu bar code below
menubar = Menu(window)
tablemenu = Menu(menubar, tearoff=0)
tablemenu.add_command(label="View Free Tables", command=view_table)
tablemenu.add_command(label="View Booked Table", command=viewb_table)
tablemenu.add_command(label="Cancle Booked Table", command=cancle_table)
tablemenu.add_separator()
tablemenu.add_command(label="Exit", command=exit)

menubar.add_cascade(label="Tables Details", menu=tablemenu)

window.config(menu=menubar)
window.mainloop()
