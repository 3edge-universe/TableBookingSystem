from tkinter import *
from tkinter import messagebox
from back_main import *

l=login('Data.db')

def find():
        row=l.view_free_table(date.get(),timein.get(),timeout.get())
        for i in range(len(row)):
                cols = []
                for j in range(4):
                        e = Entry(subf,relief="ridge")
                        e.grid(row=i+1,column=j,padx=10,pady=10)
                        e.insert(END,row[i][j])
                        cols.append(e)
	
def book_table():
    dates.config(highlightcolor="black",highlightbackground="black")
    tno.config(highlightbackground="black", highlightcolor="black")
    pno.config(highlightbackground="black", highlightcolor="black")
    status=0
    try:
        if date.get()=="":
                messagebox.showinfo("Error","All Field Should Filled !!")
                dates.config(highlightcolor="red",highlightbackground="red")
                dates.delete(0,END)
                dates.focus_set()
        elif no_var.get()==0 or name_var.get()=="" or phone_var.get()=="":
                messagebox.showinfo("Error","All Field Should Filled !!")
        elif (phone_var.get().isdigit()==False) or len(phone_var.get())!=10:
                messagebox.showinfo("Error","Phone No is Not Proper!! Try again")
                pno.delete(0,END)
                pno.config(highlightbackground="red", highlightcolor="red")
                pno.focus_set()
        else:
                status=l.book(no_var.get(),name_var.get(),phone_var.get(),date.get(),timein.get(),timeout.get())
        if status=='e2':
                messagebox.showinfo("Error","Phone No is Already registered!! Try again")
                pno.delete(0,END)
                pno.config(highlightbackground="red", highlightcolor="red")
                pno.focus_set()    
        elif status=='0':
                window.destroy()
                import cust
        elif status=='e1':
                messagebox.showinfo("Error","This Table is already occupied!! Try again")
                tno.delete(0,END)
                tno.config(highlightbackground="red", highlightcolor="red")
                tno.focus_set()
        elif status=='e3':
                messagebox.showinfo("Error","this table no does not exist!! Try again")
                tno.delete(0,END)
                tno.config(highlightbackground="red", highlightcolor="red")
                tno.focus_set()
        
    except Exception as e:
        messagebox.showinfo("Error","Number fields should be with number only!!")
        print(e)

        

window=Tk()
window.wm_title("CMS")
window.geometry('1350x700')
window.configure()

l1=Label(window,text="WELCOME TO CMS",font=("times",28,"italic bold"),fg="red",relief='raised',bd=5)
l1.pack(side=TOP,fill=X,padx=10,pady=10)

#select frame
f1=Frame(window,bg="grey",height=100,relief='solid',bd=5)
f1.pack(fill=BOTH,pady=10,padx=10)

#Date
lab1=Label(f1,text="Date",font=("times",18,"bold"),fg="black")
lab1.grid(row=1,column=0, padx=5, pady=5)
date=StringVar()
dates=Entry(f1,textvariable=date,font=("times",18),highlightthickness=2)
dates.focus_set()
dates.grid(row=1,column=2,columnspan=3, padx=10, pady=10)

#Timein
lab1=Label(f1,text="Check In Time",font=("times",18,"bold"),fg="black")
lab1.grid(row=2,column=0, padx=5, pady=5)
timein=IntVar()
time1=Entry(f1,textvariable=timein,font=("times",18),highlightthickness=2)
time1.grid(row=2,column=2,columnspan=3, padx=10, pady=10)

#timeout
lab1=Label(f1,text="Check Out Time",font=("times",18,"bold"),fg="black")
lab1.grid(row=3,column=0, padx=5, pady=5)
timeout=IntVar()
time2=Entry(f1,textvariable=timeout,font=("times",18),highlightthickness=2)
time2.grid(row=3,column=2,columnspan=3, padx=10, pady=10)

b1=Button(f1,text="Find Tables",bg="grey",fg="black",font=("times",20,"bold"),command=find)
b1.grid(row=4,column=2,padx=10,pady=10)

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
e2 = Label(subf,text='No of chairs',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e2.grid(row=0,column=1,padx=10,pady=10)
e3 = Label(subf,text='Price',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e3.grid(row=0,column=2,padx=10,pady=10)
e4 = Label(subf,text='Describe',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
e4.grid(row=0,column=3,padx=10,pady=10)




#book table
f2=Frame(window,bg="grey",height=200,relief='solid',bd=5)
f2.pack(side=BOTTOM,fill=BOTH,pady=10,padx=10)

#table no
lab1=Label(f2,text="Your table No",font=("times",18,"bold"),fg="black")
lab1.grid(row=0,column=0,padx=10,pady=10)
no_var=IntVar()
tno=Entry(f2,textvariable=no_var,font=("times",18),highlightthickness=2)
tno.grid(row=0,column=2,padx=10,pady=10)

#name
lab2=Label(f2,text="Your Name",font=("times",18,"bold"),fg="black")
lab2.grid(row=1,column=0,padx=10,pady=10)
name_var=StringVar()
tname=Entry(f2,textvariable=name_var,font=("times",18),highlightthickness=2)
tname.grid(row=1,column=2,padx=10,pady=10)
#phone no
lab3=Label(f2,text="Your Phone No",font=("times",18,"bold"),fg="black")
lab3.grid(row=2,column=0,padx=10,pady=10)
phone_var=StringVar()
pno=Entry(f2,textvariable=phone_var,font=("times",18),highlightthickness=2)
pno.grid(row=2,column=2,padx=10,pady=10)

b2=Button(f2,text="Book Table",bg="grey",fg="black",font=("times",20,"bold"),command=book_table)
b2.grid(row=2,column=4,padx=10,pady=10)

window.mainloop()
