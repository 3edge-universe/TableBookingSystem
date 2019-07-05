from tkinter import *
from tkinter import messagebox
from back_main import *

l=login('Data.db')

def find():
    status=0
    pno.config(highlightcolor="black",highlightbackground="black")
    status=l.find_table(pno_var.get())
    if status==0:
        messagebox.showinfo("Error","No tables Booked Yet!!")
        pno.delete(0,END)
        pno.config(highlightbackground="red", highlightcolor="red")
        pno.focus_set()
    else:
        for i in range(len(status)):
                cols = []
                for j in range(7):
                        e = Entry(subf,relief="ridge")
                        e.grid(row=i+1,column=j,padx=10,pady=10)
                        e.insert(END,status[i][j+2])
                        cols.append(e)
        
def cancle_table():
    status=l.cancle(no_var.get(),pno_var.get())
    window.destroy()
    import main

def back():
    window.destroy()
    import main


window=Tk()
window.wm_title("CMS")
window.geometry('1350x700')
window.configure()


l1=Label(window,text="WELCOME TO CMS",font=("times",28,"italic bold"),fg="red",relief='raised',bd=5)
l1.pack(side=TOP,fill=X,padx=10,pady=20)
#select frame
f1=Frame(window,bg="grey",height=100,relief='solid',bd=5)
f1.pack(fill=BOTH,pady=20,padx=10)

#Phone no
lab1=Label(f1,text="Phone no",font=("times",18,"bold"),fg="black")
lab1.grid(row=1,column=0, padx=5, pady=5)
pno_var=IntVar()
pno=Entry(f1,textvariable=pno_var,font=("times",18),highlightthickness=2)
pno.focus_set()
pno.grid(row=1,column=2,columnspan=3, padx=10, pady=10)

b1=Button(f1,text="Find Book Tables",bg="grey",fg="black",font=("times",20,"bold"),command=find)
b1.grid(row=2,column=2,padx=10,pady=10)


#select frame
subframe=Frame(window,bg="white",relief='solid',bd=5)
subframe.pack(fill=BOTH,pady=10,padx=10)

canvas=Canvas(subframe,scrollregion=(0,0,300,100))
sc=Scrollbar(subframe,orient=VERTICAL)
sc.pack(side=RIGHT,fill=Y)
sc.config(command=canvas.yview)
canvas.config(yscrollcommand=sc.set)
canvas.pack(fill=BOTH,expand=True)

subf=Frame(canvas,bg="white",relief='solid',bd=5)
subf.pack(fill=BOTH)


e1 = Label(subf,text='Table No',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e1.grid(row=0,column=0,padx=10,pady=10)
e2 = Label(subf,text='Date',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e2.grid(row=0,column=1,padx=10,pady=10)
e3 = Label(subf,text='Timein',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e3.grid(row=0,column=2,padx=10,pady=10)
e4 = Label(subf,text='Timeout',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e4.grid(row=0,column=3,padx=10,pady=10)
e5 = Label(subf,text='No of chairs',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e5.grid(row=0,column=4,padx=10,pady=10)
e6 = Label(subf,text='Price',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e6.grid(row=0,column=5,padx=10,pady=10)
e7 = Label(subf,text='Describe',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e7.grid(row=0,column=6,padx=10,pady=10)

#book table
f2=Frame(window,bg="grey",height=200,relief='solid',bd=5)
f2.pack(side=BOTTOM,fill=BOTH,pady=10,padx=10)

#table no
lab1=Label(f2,text="Your table No",font=("times",18,"bold"),fg="black")
lab1.grid(row=0,column=0,padx=10,pady=10)
no_var=IntVar()
tno=Entry(f2,textvariable=no_var,font=("times",18),highlightthickness=2)
tno.grid(row=0,column=2,padx=10,pady=10)

b2=Button(f2,text="Cancle Table",bg="grey",fg="black",font=("times",20,"bold"),command=cancle_table)
b2.grid(row=2,column=2,padx=10,pady=10)
b3=Button(f2,text="Back",bg="grey",fg="black",font=("times",20,"bold"),command=back)
b3.grid(row=2,column=4,padx=10,pady=10)

window.mainloop()
