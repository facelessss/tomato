import json
import os

global home
home = os.getcwd() + '/content/'

class DealJson:
    def __init__(self):
        pass
        
    def add_user(self,username,password):
        if os.path.exists(home+username+".json"):   #check duplication
            return False
        else:
            file = open(home+username+".json", 'w') #create new nsers
            userfile={'password':password}
            userfile["issue"]=["","","","","",""]
            file.write(json.dumps(userfile))
            file.close()
            return True

    def check(self,username,password):
        if os.path.exists(home+username+".json") == False: #check if the user has exited
            return False
        file = open(home+username+".json", 'r')
        userJs=json.load(file)
        file.close()
        if userJs["password"]==password:  #check password
            return True
        else:
            return False

    def add_issue(self,username,issue_name):
        i=0
        file = open(home+username+".json", 'r')
        userJs=json.load(file)
        file.close()
        while i< len(userJs["issue"]):  #no more than 6 issues
            if  userJs["issue"][i] == "":
                userJs["issue"][i]=issue_name
                file = open(home+username+".json", 'w')
                file.write(json.dumps(userJs))
                file.close()
                return True       
            i=i+1
        return False

    def delete_issue(self,username,issue_name):
        i=0
        file = open(home+username+".json", 'r')
        userJs=json.load(file)
        file.close()
        tmp=userJs["issue"]
        while i< len(userJs["issue"]):
            if  userJs["issue"][i] == issue_name: #find and replace with ""
                userJs["issue"][i]=""
            i=i+1
        file = open(home+username+".json", 'w')
        file.write(json.dumps(userJs))
        file.close()
        return True
               
    def get_issue(self,username):
        file = open(home+username+".json", 'r')
        userJs=json.load(file)
        file.close()
        return userJs["issue"] #return all issues

    def record(self,username,record_name,year,month,day):
        file = open(home+username+".json", 'r')
        userJs=json.load(file)
        file.close()
        if userJs.has_key("record")==False: #create if  no that key
            userJs["record"]={}
        if userJs["record"].has_key(year)==False:
            userJs["record"][year]={}
        if userJs["record"][year].has_key(month)==False:
            userJs["record"][year][month]={}
        if userJs["record"][year][month].has_key(day)==False:
            userJs["record"][year][month][day]=""
        userJs["record"][year][month][day]=userJs["record"][year][month][day]+record_name+" "#use a string to  satisfy ui.py
        file = open(home+username+".json", 'w')
        file.write(json.dumps(userJs))
        file.close()

    def get_record(self,username,year,month):
        file = open(home+username+".json", 'r')
        userJs=json.load(file)
        file.close()
        return userJs["record"][year][month] #get a month's record

