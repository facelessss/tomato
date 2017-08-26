
import os
from tools import Tools 
from users import User

class Tomato:
	def __init__(self):
		self.username = None
		self.password = None
		self.login_succ = False
		self.mins = 25
		self.secs = 0
		self.tools = Tools()
		self.user = User()
		self.now_issue = None
		self.now_time = None

	def add_user(self , uname , upassword):
		return self.tools.add_user(uname, upassword)

	def log_in(self , uname , upassword):
		self.username = uname
		self.password = upassword
		if self.tools.check( self.username , self.password ) == True:
			self.login_succ = True
			self.user = User(self.username)
			return True
		else:
			self.login_succ = False
			return False



