from tkinter import *
from tkinter import messagebox
from sqlite3 import *
import re

class login():
	def __init__(self,db):
		self.conn=connect(db)
		self.curr=self.conn.cursor()
		s='create table if not exists data (name varchar2(30),email varchar2(30) primary key,pass varchar2(30),phone integer)'
		self.curr.execute(s)
		s='create table if not exists tables (no integer primary key,noc integer,price intger,desc varchar2(50))'
		self.curr.execute(s)
		s='create table if not exists booktable (name varchar2(30),phone integer,no integer,date varchar2(8),timein integer,timeout integer)'
		self.curr.execute(s)
		self.conn.commit()

	def login(self,email,pwd):
		'''This is login function for both admin'''
		s="select pass from data where email='%s'"%(email)
		self.curr.execute(s)
		data=self.curr.fetchall()
		if len(data)==1:
			if pwd==data[0][0]:
				messagebox.showinfo("Login","Login succesfull!!")
				return 0
			else:
				messagebox.showinfo("Login","Wrong Password!! Try Again")
				return 1
		elif len(data)==0:
			messagebox.showinfo("Login","Email Not Exist!! Try Again")
			return 2
			
	def find(self,no):
		'''This is find function for tables'''
		s="select * from tables where no='%d'"%(no)
		self.curr.execute(s)
		data=self.curr.fetchall()
		if len(data)==1:
			return data[0]
		elif len(data)==0:
			return 0
	def find_table(self,no):
		'''This is find function for tables'''
		s="select * from booktable where phone='%d'"%(no)
		self.curr.execute(s)
		data=self.curr.fetchall()
		if len(data)==0:
			return 0
		else:
			for i in range(len(data)):
				s1="select noc,price,desc from tables where no='%d'"%(int(data[i][2]))
				self.curr.execute(s1)
				data[i]+=self.curr.fetchall()[0]
		return data
	
	
	
	def view_free_table(self,date,timein,timeout):
		'''This is find function for free tables'''
		s="select no from tables"
		self.curr.execute(s)
		data=self.curr.fetchall()
		data=[data[i][0] for i in range(len(data))]
		table=[]
		for i in data:
			s="select * from booktable where no=%d and date='%s' and timein=%d and timeout=%d"%(i,date,int(timein),int(timeout))
			self.curr.execute(s)
			book=self.curr.fetchall()
			if len(book)==0:
				table.append(i)
		data_table=[]
		for i in table:
			data_table.append(self.find(i))
		return data_table
	
	def register(self,name,mail,pwd,phone):
		"""This is register Function"""
		s="select email from data"
		self.curr.execute(s)
		data=self.curr.fetchall()
		data=[i[0] for i in data]
		if mail in data:
			return "e2"
		query="insert into data values('%s','%s','%s',%d)"%(name,mail,pwd,int(phone))
		self.curr.execute(query)
		self.conn.commit()
		messagebox.showinfo("Success","Sucessfully Registered")
		return '0'

	def book(self,no,name,phone,date,timein,timeout):
		"""This is  Function for booking a table"""
		s="select phone from booktable where no=%d and date='%s' and timein=%d and timeout=%d"%(int(no),date,int(timein),int(timeout))
		self.curr.execute(s)
		data=self.curr.fetchall()
		data=[i[0] for i in data]
		if phone in data:
			return "e2"
		s="select * from booktable where no=%d and date='%s' and timein=%d and timeout=%d"%(int(no),date,int(timein),int(timeout))
		self.curr.execute(s)
		book=self.curr.fetchall()
		if len(book)!=0:
			return 'e1'
		s="select no from tables"
		self.curr.execute(s)
		data=self.curr.fetchall()
		data=[i[0] for i in data]
		if no not in data:
			return "e3"
		query="insert into booktable values('%s',%d,%d,'%s',%d,%d)"%(name,int(phone),int(no),date,int(timein),int(timeout))
		self.curr.execute(query)
		self.conn.commit()
		messagebox.showinfo("Success","Table Booked Sucessfully")
		return '0'

	def add_tables(self,no,noc,price,desc):
		"""This is add_tables Function"""
		s="select no from tables"
		self.curr.execute(s)
		data=self.curr.fetchall()
		data=[i[0] for i in data]
		if no in data:
			return "e2"
		query="insert into tables values(%d,%d,%d,'%s')"%(int(no),int(noc),int(price),desc)
		self.curr.execute(query)
		self.conn.commit()
		messagebox.showinfo("Success","Table added succesfully")
		return '0'

	def edit_tables(self,no,noc,price,desc):
		"""This is update_tables Function"""
		query="update tables set noc=%d,price=%d,desc='%s' where no= %d"%(int(noc),int(price),desc,int(no))
		self.curr.execute(query)
		self.conn.commit()
		messagebox.showinfo("Success","Table updated succesfully")
		return '0'

	def delete_tables(self,no):
		"""This is delete_tables Function"""
		query="delete from  tables where no= %d"%(int(no))
		self.curr.execute(query)
		self.conn.commit()
		messagebox.showinfo("Success","Table Deleted succesfully")
		return '0'

	def cancle(self,no,pno):
		"""This is cancle_tables Function"""
		query="delete from  booktable where no= %d and phone=%d"%(int(no),int(pno))
		self.curr.execute(query)
		self.conn.commit()
		messagebox.showinfo("Success","Table Cancle succesfully")
		return '0'

	def __del__(self):
		self.conn.commit()
		self.conn.close()
