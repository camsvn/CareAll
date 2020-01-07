import sqlite3 as sql

class job:
    def __init__(self,desc=None,salary=None,duration=None):
        #self.utype=utype
        self.desc=desc
        self.salary=salary
        self.duration=duration
        
    #CARE SEEKER SPECIFIC
    def create(self,utype):
        if utype==1:
            print("You Have Access to Create",self.salary)
        else:
            print("You Dont HAVE ACCSESS CREATE")
    def accept(self):
        if self.utype==1:
            print("You Have Access ACCEPt")
        else:
            print("You Dont HAVE ACCSESS ACCEPT")
    def close(self):
        if self.utype==1:
            print("You Have Access CLOSE")
        else:
            print("You Dont HAVE ACCSESS CLOSE")
   
    
    #CARE TAKER SPECIFIC
    def view(self):
        if self.utype==2:
            print("You Have Access VIEW")
        else:
            print("You Dont HAVE ACCSESS VIEW")
    def confirm(self):
        if self.utype==2:
            print("You Have Access CONFIRM")
        else:
            print("You Dont HAVE ACCSESS CONFIRM")
            

j1=job(1,salary=2000)
j2=job(2)
j3=job(1,salary=3000)

