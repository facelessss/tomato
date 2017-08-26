import time
import sys
import json
from dealjson import DealJson
#from users import Uers

class Tools:
	def __init__(self):
		self.sound_name = 'dida.wav'
		self.tool=DealJson()

	def remind_sound(self):
		if sys.platform[:5] == 'linux2' or sys.platform == 'darwin':
			import os
			os.popen(self.sound_name)
		else:
			import winsound
			winsound.PlaySound(self.sound_name , winsound.SND_FILENAME)


	def check(self , name , password):
		return self.tool.check( name , password)

	#no return , build a file of user 
	def add_user(self, username , password):
                return self.tool.add_user( username ,password)
                
	#get issues from a user file , return a list of issue name
	def get_issue(self,name):
		return self.tool.get_issue(name)

	def add_issue(self , user_name ,issue_name):
		return self.tool.add_issue(user_name ,issue_name)

	def delete_issue(self,username,issue_name):
                return self.tool.delete_issue(username,issue_name)

	#write a record into a user's file 
	def record(self,username,record_name,year,month,day):
                self.tool.record(username,record_name,year,month,day)
                
		

	#read records from a user's file ; exc means which month you need to read     ex: get_record("zhang_wen_hao" , "2015.11")
	def get_record(self , name ,year, exc):
		return self.tool.get_record(name,year,exc)

