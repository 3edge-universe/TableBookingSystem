from tkinter import *
from back_main import *
from tkinter import messagebox

l=login("Data.db")
	
def register():
	window=Tk()
	window.wm_title("CMS")
	window.geometry('1350x700')
	window.configure()
	l=login("Data.db")
	def register_fun():
		e1.config(highlightbackground="black",highlightcolor="black")
		e2.config(highlightcolor="black",highlightbackground="black")
		e3.config(highlightcolor="black",highlightbackground="black")
		e4.config(highlightcolor="black",highlightbackground="black")
		phone.config(highlightcolor="black",highlightbackground="black")
		status=0
		if e1_var.get()=="" or e2_var.get()=="" or e3_var.get()=="" or e4_var.get()=="" or e5_var.get()=="":
			messagebox.showinfo("Error","All Field Should Filled !!")
		elif len(re.findall(r'\w+@\w+\.\w+',e2_var.get()))==0:
			messagebox.showinfo("Error","Email structure is Wrong !! Try Again")
			e2.delete(0,END)
			e2.config(highlightbackground="red", highlightcolor="red")
			e2.focus_set()
		elif e3_var.get().isalpha() or e3_var.get().isnumeric():
			messagebox.showinfo("Error","Password is poor !! Use AphaNumeric with special symbol")
			e3.delete(0,END)
			e3.config(highlightbackground="red", highlightcolor="red")
			e3.focus_set()
		elif e3_var.get()!=e4_var.get():
			messagebox.showinfo("Error","Password Does Not Match !! Try again")
			e3.delete(0,END)
			e4.delete(0,END)
			e3.config(highlightbackground="red", highlightcolor="red")
			e4.config(highlightbackground="red", highlightcolor="red")
			e3.focus_set()
			
		elif (e5_var.get().isdigit()==False) or len(e5_var.get())!=10:
			messagebox.showinfo("Error","Phone No is Not Proper!! Try again")
			phone.delete(0,END)
			phone.config(highlightbackground="red", highlightcolor="red")
			phone.focus_set()
		else:	
			status=l.register(e1_var.get(),e2_var.get(),e3_var.get(),e5_var.get())
		if status=="e2":
			messagebox.showinfo("Error","Email is Already Exist !!Try Another Email")
			e2.delete(0,END)
			e2.config(highlightbackground="red", highlightcolor="red")
			e2.focus_set()
		elif status=='0':
			window.destroy()
			import main
	
	

	l1=Label(window,text="WELCOME TO CMS",font=("times",28,"italic bold"),fg="red",relief='raised',bd=5)
	l1.pack(side=TOP,fill=X,padx=10,pady=20)
	
	lab=Label(window,text="Register",font=("times",20,"bold"),fg="green")
	lab.pack(side=TOP,fill=X,padx=10,pady=20)
	
	# register frame
	f1=Frame(window,bg="white",height=400,relief='solid',bd=5)
	f1.pack(fill=BOTH,pady=20,padx=10)

	#Name
	lab1=Label(f1,text="Name",font=("times",18,"bold"),fg="black")
	lab1.grid(row=1,column=0, padx=5, pady=5)
	e1_var=StringVar()
	e1=Entry(f1,textvariable=e1_var,font=("times",18),highlightthickness=2)
	e1.focus_set()
	e1.grid(row=1,column=2,columnspan=3, padx=10, pady=10)

	#email
	lab2=Label(f1,text="Email",font=("times",18,"bold"),fg="black")
	lab2.grid(row=2,column=0, padx=5, pady=5)
	e2_var=StringVar()
	e2=Entry(f1,textvariable=e2_var,font=("times",18),highlightthickness=2)
	e2.grid(row=2,column=2,columnspan=3, padx=10, pady=10)

	#password
	lab3=Label(f1,text="Password",font=("times",18,"bold"),fg="black")
	lab3.grid(row=3,column=0, padx=5, pady=5)
	e3_var=StringVar()
	e3=Entry(f1,textvariable=e3_var,show="*",font=("times",18),highlightthickness=2)
	e3.grid(row=3,column=2,columnspan=3, padx=10, pady=10)

	#confirm password
	lab4=Label(f1,text="Confirm Password",font=("times",18,"bold"),fg="black")
	lab4.grid(row=4,column=0, padx=5, pady=5)
	e4_var=StringVar()
	e4=Entry(f1,textvariable=e4_var,show="*",font=("times",18),highlightthickness=2)
	e4.grid(row=4,column=2,columnspan=3, padx=10, pady=10)

	#phone no
	lab5=Label(f1,text="Phone No",font=("times",18,"bold"),fg="black")
	lab5.grid(row=5,column=0, padx=5, pady=5)
	e5_var=StringVar()
	phone=Entry(f1,textvariable=e5_var,font=("times",20,"bold"),highlightthickness=2)
	phone.grid(row=5,column=2,columnspan=3, padx=10, pady=10)
	
	b2=Button(f1,text="Register",bg="grey",fg="black",font=("times",20,"bold"),command=register_fun)
	b2.grid(row=7,column=2,padx=10,pady=10)
	window.mainloop()