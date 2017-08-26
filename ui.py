import os
from datetime import  *
import time
from Tkinter import *
import Tkinter
from tomato import Tomato
from threading import Thread

class Ui:
	def __init__(self ):
		self.tomato = Tomato()
		self.stopbo = False
		self.addbo = False
		self.deletebo = False
		self.root = Tkinter.Tk()
		self.root.title("tomato")
		self.root.geometry("320x120+100+100")
		self.build_1()
		self.root.mainloop()

	def tran1_2( self):
		self._destroy_1()
		self.build_2()

	def build_1(self ):
		self.frame_1 = Tkinter.Frame(self.root)
		global bool_1 
		global string_1
		global string_2
		string_1 = StringVar()
		string_2 = StringVar()
		bool_1 = IntVar()
		bool_1.set(False)
		self.la_1 = Tkinter.Label(self.frame_1, text = "user name")
		self.la_2 = Tkinter.Label(self.frame_1,text = "password")
		self.en_1 = Tkinter.Entry(self.frame_1 , textvariable = string_1 )
		self.en_2 = Tkinter.Entry(self.frame_1 , textvariable = string_2 )
		self.en_2.config(show = '*')
		self.ra_1 = Tkinter.Radiobutton(self.frame_1 , text = "need register" , variable = bool_1 , value = True )
		self.ra_2 = Tkinter.Radiobutton(self.frame_1 , text = "   just log in   " , variable = bool_1 , value = False )
		self.bu_1 = Tkinter.Button(self.frame_1, text = "OK ",command = self.login_ok )
		self.la_1.grid()
		self.la_2.grid()
		self.en_1.grid(row = 0 , column = 1)
		self.en_2.grid(row = 1 , column = 1)
		self.ra_1.grid(row = 2 , column = 0)
		self.ra_2.grid(row = 3 , column = 0)
		self.bu_1.grid(row = 3 , column = 1)
		self.frame_1.pack()
	def build_2(self):
		self.root.geometry("320x150+100+100")
		self.frame_2 = Tkinter.Frame(self.root)
		self.la_3 =Tkinter.Label(self.frame_2, text = "start with an issue") 
		self.la_4 = Tkinter.Label(self.frame_2 , text = self.get_time())
		self.bu_2 = Tkinter.Button(self.frame_2, text = self.tomato.user.issue[0]  ,command = self.time_reminder_th_0 , disabledforeground = "#708090")
		self.bu_3 = Tkinter.Button(self.frame_2, text = self.tomato.user.issue[1]  ,command = self.time_reminder_th_1 , disabledforeground = "#708090")
		self.bu_4 = Tkinter.Button(self.frame_2, text = self.tomato.user.issue[2]  ,command = self.time_reminder_th_2 , disabledforeground = "#708090")
		self.bu_5 = Tkinter.Button(self.frame_2, text = self.tomato.user.issue[3]  ,command = self.time_reminder_th_3 , disabledforeground = "#708090")
		self.bu_6 = Tkinter.Button(self.frame_2, text = self.tomato.user.issue[4]  ,command = self.time_reminder_th_4 , disabledforeground = "#708090")
		self.bu_7 = Tkinter.Button(self.frame_2, text = self.tomato.user.issue[5]  ,command = self.time_reminder_th_5 , disabledforeground = "#708090")
		self.bu_8 = Tkinter.Button(self.frame_2,  text = "stop" , height = 2  ,cursor = "cross" ,command = self.stop )
		self.bu_9 = Tkinter.Button(self.frame_2, text = "add" , command = self.add )
		self.bu_10 = Tkinter.Button(self.frame_2 , text = "delete" ,command = self.delete )
		self.bu_11 = Tkinter.Button(self.frame_2 , text = "print record" , command = self.print_rec )
		self.la_3.grid(row = 0 , column = 1)
		self.bu_2.grid(row = 1 , column = 0)
		self.bu_3.grid(row = 1 , column = 1)
		self.bu_4.grid(row = 1 , column = 2)
		self.bu_5.grid(row = 2 , column = 0)
		self.bu_6.grid(row = 2 , column = 1)
		self.bu_7.grid(row = 2 , column = 2)
		self.bu_8.grid(row = 3,  column = 0)
		self.la_4.grid(row = 3 , column =1)
		self.bu_9.grid(row = 4 , column =0)
		self.bu_10.grid(row = 4 , column =1)
		self.bu_11.grid(row = 4 ,column = 2)
		self.frame_2.pack()

	def _destroy_1(self ):
		self.frame_1.destroy()
	def _destroy_2(self ):
		self.frame_2.destroy()

	def login_ok(self):
		if bool_1.get() == True:
			if self.tomato.add_user(string_1.get() , string_2.get()) == False:
				error_1 = Tkinter.Tk()
				error_1.title("error")
				error_1.geometry("200x50+150+150")
				Tkinter.Label(error_1, text = " the user has been created").pack()
				Tkinter.Button(error_1,text = "try again" ,command = error_1.destroy).pack()
				error_1.mainloop()
				return

		if self.tomato.log_in(string_1.get() , string_2.get()) == True:
			self.tran1_2()
		else:
			error = Tkinter.Tk()
			error.title("error")
			error.geometry("200x50+150+150")
			Tkinter.Label(error, text = " valid username or password").pack()
			Tkinter.Button(error,text = "try again" ,command = error.destroy).pack()
			error.mainloop()

	def get_time(self ):
		re = ""
		zero = "0"
		mi = str(self.tomato.mins)
		se = str(self.tomato.secs)
		if(self.tomato.mins < 10):
			re = re + zero
		re = re + mi
		re = re + ":"
		if(self.tomato.secs < 10):
			re = re + zero
		re = re + se
		return re


	def time_reminder_th_0(self):
		if self.tomato.user.issue[0] == "":
			error_3 = Tkinter.Tk()
			error_3.title("error")
			error_3.geometry("200x50+150+150")
			Tkinter.Label(error_3, text = " no issue here").pack()
			Tkinter.Button(error_3,text = "try again" ,command = error_3.destroy).pack()
			error_3.mainloop()
			return
		self.la_3["text"] = self.tomato.user.issue[0]
		self.bu_2["state"] = DISABLED
		self.bu_3["state"] = DISABLED
		self.bu_4["state"] = DISABLED
		self.bu_5["state"] = DISABLED
		self.bu_6["state"] = DISABLED
		self.bu_7["state"] = DISABLED
		thread_0 = Thread(target =self.time_reminder , args = (0,))
		thread_0.start()
	def time_reminder_th_1(self):
		if self.tomato.user.issue[1] == "":
			error_3 = Tkinter.Tk()
			error_3.title("error")
			error_3.geometry("200x50+150+150")
			Tkinter.Label(error_3, text = " no issue here").pack()
			Tkinter.Button(error_3,text = "try again" ,command = error_3.destroy).pack()
			error_3.mainloop()
			return
		self.la_3["text"] = self.tomato.user.issue[1]
		self.bu_2["state"] = DISABLED
		self.bu_3["state"] = DISABLED
		self.bu_4["state"] = DISABLED
		self.bu_5["state"] = DISABLED
		self.bu_6["state"] = DISABLED
		self.bu_7["state"] = DISABLED
		thread_1 = Thread(target =self.time_reminder , args = (1,))
		thread_1.start()
	def time_reminder_th_2(self):
		if self.tomato.user.issue[2] == "":
			error_3 = Tkinter.Tk()
			error_3.title("error")
			error_3.geometry("200x50+150+150")
			Tkinter.Label(error_3, text = " no issue here").pack()
			Tkinter.Button(error_3,text = "try again" ,command = error_3.destroy).pack()
			error_3.mainloop()
			return
		self.la_3["text"] = self.tomato.user.issue[2]
		self.bu_2["state"] = DISABLED
		self.bu_3["state"] = DISABLED
		self.bu_4["state"] = DISABLED
		self.bu_5["state"] = DISABLED
		self.bu_6["state"] = DISABLED
		self.bu_7["state"] = DISABLED
		thread_2 = Thread(target =self.time_reminder , args = (2,))
		thread_2.start()
	def time_reminder_th_3(self):
		if self.tomato.user.issue[3] == "":
			error_3 = Tkinter.Tk()
			error_3.title("error")
			error_3.geometry("200x50+150+150")
			Tkinter.Label(error_3, text = " no issue here").pack()
			Tkinter.Button(error_3,text = "try again" ,command = error_3.destroy).pack()
			error_3.mainloop()
			return
		self.la_3["text"] = self.tomato.user.issue[3]
		self.bu_2["state"] = DISABLED
		self.bu_3["state"] = DISABLED
		self.bu_4["state"] = DISABLED
		self.bu_5["state"] = DISABLED
		self.bu_6["state"] = DISABLED
		self.bu_7["state"] = DISABLED
		thread_3 = Thread(target =self.time_reminder , args = (3,))
		thread_3.start()
	def time_reminder_th_4(self):
		if self.tomato.user.issue[4] == "":
			error_3 = Tkinter.Tk()
			error_3.title("error")
			error_3.geometry("200x50+150+150")
			Tkinter.Label(error_3, text = " no issue here").pack()
			Tkinter.Button(error_3,text = "try again" ,command = error_3.destroy).pack()
			error_3.mainloop()
			return
		self.la_3["text"] = self.tomato.user.issue[4]
		self.bu_2["state"] = DISABLED
		self.bu_3["state"] = DISABLED
		self.bu_4["state"] = DISABLED
		self.bu_5["state"] = DISABLED
		self.bu_6["state"] = DISABLED
		self.bu_7["state"] = DISABLED
		thread_4 = Thread(target =self.time_reminder , args = (4,))
		thread_4.start()
	def time_reminder_th_5(self):
		if self.tomato.user.issue[5] == "":
			error_3 = Tkinter.Tk()
			error_3.title("error")
			error_3.geometry("200x50+150+150")
			Tkinter.Label(error_3, text = " no issue here").pack()
			Tkinter.Button(error_3,text = "try again" ,command = error_3.destroy).pack()
			error_3.mainloop()
			return
		self.la_3["text"] = self.tomato.user.issue[5]
		self.bu_2["state"] = DISABLED
		self.bu_3["state"] = DISABLED
		self.bu_4["state"] = DISABLED
		self.bu_5["state"] = DISABLED
		self.bu_6["state"] = DISABLED
		self.bu_7["state"] = DISABLED
		thread_5 = Thread(target =self.time_reminder , args = (5,))
		thread_5.start()

	def time_refresh(self):
		self.la_3["text"] = "start with an issue"
		self.bu_2["state"] = NORMAL
		self.bu_3["state"] = NORMAL
		self.bu_4["state"] = NORMAL
		self.bu_5["state"] =  NORMAL
		self.bu_6["state"] =  NORMAL
		self.bu_7["state"] =  NORMAL
		self.tomato.mins = 25
		self.tomato.secs = 0

	def stop(self):
		self.stopbo = True
		self.time_refresh()

	def time_reminder(self , idx):
		time_st = time.time()
		while True:
			time_now = time.time()
			self.tomato.mins = int(1500 - time_now + time_st) / 60
			self.tomato.secs = int(1500 - time_now + time_st) % 60
			self.la_4["text"] = self.get_time()
			if self.stopbo == True:
				self.stopbo = False
				return
			if time_now - time_st > 1500:
				break
		self.la_3["text"] = "start with an issue"
		cur_time=date.today()
		year=str(cur_time.year)
		month=str(cur_time.month)
		day=str(cur_time.day)
		self.tomato.user.record( self.tomato.user.issue[idx] , year,month,day)
		self.time_refresh()

	def add(self):
		en = Tkinter.Tk()
		en.title("enter")
		en.geometry("200x100+150+150")
		ff = Tkinter.Frame(en)
		Tkinter.Label(ff, text = "issue:").pack()
		self.eee = Tkinter.Entry(ff )
		bbb = Tkinter.Button(ff,text = "OK" ,command = self.add_he )
		bbb2 = Tkinter.Button(ff,text = "finish" ,command = en.destroy )
		self.eee.pack()
		bbb.pack()
		bbb2.pack()
		ff.pack()
		en.mainloop()

	def add_he(self ):
		if self.tomato.user.add_issue( self.eee.get() ) == False:
			error_2 = Tkinter.Tk()
			error_2.title("error")
			error_2.geometry("200x50+150+150")
			Tkinter.Label(error_2, text = "max or repeat").pack()
			Tkinter.Button(error_2,text = "try again" ,command = error_2.destroy).pack()
			error_2.mainloop()
		else:
			su = Tkinter.Tk()
			su.title("succes!")
			su.geometry("200x50+150+150")
			Tkinter.Label(su, text = "succes !").pack()
			Tkinter.Button(su,text = "OK" ,command = su.destroy).pack()
			self.bu_2["text"] = self.tomato.user.issue[0]
			self.bu_3["text"] = self.tomato.user.issue[1]
			self.bu_4["text"] = self.tomato.user.issue[2]
			self.bu_5["text"] = self.tomato.user.issue[3]
			self.bu_6["text"] = self.tomato.user.issue[4]
			self.bu_7["text"] = self.tomato.user.issue[5]
			su.mainloop()

	def delete(self):
		een = Tkinter.Tk()
		een.title("enter")
		een.geometry("200x100+150+150")
		eff = Tkinter.Frame(een)
		Tkinter.Label(eff, text = "issue:").pack()
		self.ttt = Tkinter.Entry(eff )
		ebbb = Tkinter.Button(eff,text = "OK" ,command = self.delete_he )
		ebbb2 = Tkinter.Button(eff,text = "finish" ,command = een.destroy )
		self.ttt.pack()
		ebbb.pack()
		ebbb2.pack()
		eff.pack()
		een.mainloop()

	def delete_he(self ):
		if self.tomato.user.delete_issue( self.ttt.get() ) == False:
			error_2 = Tkinter.Tk()
			error_2.title("error")
			error_2.geometry("200x50+150+150")
			Tkinter.Label(error_2, text = "issue not exist").pack()
			Tkinter.Button(error_2,text = "try again" ,command = error_2.destroy).pack()
			error_2.mainloop()
		else:
			su = Tkinter.Tk()
			su.title("succes!")
			su.geometry("200x50+150+150")
			Tkinter.Label(su, text = "succes !").pack()
			Tkinter.Button(su,text = "OK" ,command = su.destroy).pack()
			self.bu_2["text"] = self.tomato.user.issue[0]
			self.bu_3["text"] = self.tomato.user.issue[1]
			self.bu_4["text"] = self.tomato.user.issue[2]
			self.bu_5["text"] = self.tomato.user.issue[3]
			self.bu_6["text"] = self.tomato.user.issue[4]
			self.bu_7["text"] = self.tomato.user.issue[5]
			su.mainloop()

	def print_rec(self):
		en = Tkinter.Tk()
		en.title("enter")
		en.geometry("300x100+150+150")
		ff = Tkinter.Frame(en)
		Tkinter.Label(ff, text = "year").grid(row = 0 ,column = 0)
		Tkinter.Label(ff, text = "month").grid(row = 1 ,column = 0)
		self.qqq = Tkinter.Entry(ff )
		self.ccc = Tkinter.Entry(ff )
		bbb = Tkinter.Button(ff,text = "OK" ,command = self.print_he )
		bbb2 = Tkinter.Button(ff,text = "finish" ,command = en.destroy )
		self.qqq.grid(row = 0 ,column = 1)
		self.ccc.grid(row = 1 ,column = 1)
		bbb.grid(row = 2 ,column = 0)
		bbb2.grid(row = 2 ,column = 1)
		ff.pack()
		en.mainloop()

	def print_he(self ):
		record = self.tomato.user.get_record( self.qqq.get() , self.ccc.get())
		pp = Tkinter.Tk()
		titl = "record list of %s.%s"%(self.qqq.get() , self.ccc.get())
		pp.title(titl)
		i = 1
		le = 25
		while(i != 32):
			if record.has_key(str(i)):
				j = "%d : %s " % (i , record[str(i)])
				Tkinter.Label(pp , text = j).pack()
				le += 25
			i+= 1
		st = "600x%s+100+100"%le
		pp.geometry(st)
		Tkinter.Button(pp , text = "OK" ,command = pp.destroy ).pack()
		pp.mainloop()




