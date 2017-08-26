from tools import Tools

class User:
	def __init__(self, name = None ):
		self.name = name
		self.filename = str(name)+".json"
		self.tools = Tools()
		self.issue = ["" , "" , "" , "" , "" , "" ]
		if self.name != None: 
			self.issue = self.tools.get_issue(name)

	def add_issue(self , name):
		if self.issue.count(name):
			return False
		else:	
			if self.tools.add_issue( self.name,name) == True:
				self.issue = self.tools.get_issue(self.name)
				return True
			else:
				return False
 	
	def delete_issue(self , name):
		if self.issue.count(name):
			if self.tools.delete_issue(self.name,name) == True:
				self.issue = self.tools.get_issue(self.name)
				return True
			else:
				return False
		else:
                   		return False
                        

	def record(self , record_name,year,month,day):
                self.tools.record(self.name ,record_name,year,month,day)
		

	def get_record(self , year,exc = 'all'):
                return self.tools.get_record( self.name,year,exc)
		

