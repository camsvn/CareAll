import time
from prettytable import PrettyTable
from prettytable import from_db_cursor
import base64
import getpass
import codecs
import os
import sys
import sqlite3 as sql

class person:
    #BEGINING OF CONSTRUCTOR
    def __init__(self,name=None,uname=None,pwd=None,utype=None,age=None,location=None,phone=None):
        self.name=name
        self.age=age
        self.location=location
        self.uname=uname
        self.pwd=pwd
        self.phone=phone
        self.utype=utype
        if self.isvalid():
            print("Object is Valid")
            self.userdpdump()
            person.show()
        else:
            print("Object is InValid")
            c=self.signup()
            if c is not None:
                self.userdpdump()
    #END OF CONSTRUCTOR
    
    #BEGINING OF SHOW MODULE
    def show():
        con = sql.connect("caresys.db")
        cur = con.cursor()
        cur.execute("SELECT * from people")
        tableview=from_db_cursor(cur)
        print(tableview)
        con.close()
        '''tableview=PrettyTable()
        tableview.field_names=["Name","Username","Password","User_Type","Age","Location","Phone"]
        tableview.add_row([self.name,self.uname,self.pwd,self.utype,self.age,self.location,self.phone])
        print(tableview)
        return'''
    #END OF SHOW MODULE
    
    #BEGINING OF USERDPDUMP
    def userdpdump(self):
        con = sql.connect("caresys.db")
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS people 
        (id INTEGER PRIMARY KEY,
        name NVARCHAR(50) NOT NULL,
        username NVARCHAR(20) NOT NULL,
        password NVARCHAR(256) NOT NULL,
        usertype INT(1) NOT NULL,
        age INT(3),
        location NVARCHAR(50),
        phone INT(11));''')
        cur.execute("INSERT INTO people (name, username, password, usertype, age, location, phone) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.name,self.uname,self.pwd,self.utype,self.age,self.location,self.phone))
        con.commit()        
        con.close()
        print("User successfully registered! Please login to continue.")
    #END OF USERDPDUMP
    
    #BEGINING OF SIGNUP MODULE
    def isvalid(self):
        #Validate Name
        try:
            if all(x.isalpha() or x.isspace() for x in self.name):
                validname = True
        except:
            validname = False
        '''elif self.name==None:
            validname = False
        else:
            validname = False'''
        
        #Validate Age
        if type(self.age)==int or self.age==None:
            validage = True
        else:
            validage = False
        
        #Validate Location
        try:
            if all(x.isalpha() or x.isspace() for x in self.location):
                validlocation = True
            else:
                validlocation = False                
        except TypeError:
            validlocation = True
            
        '''elif self.location==None:
            validlocation = True
        else:
            validlocation = False'''
        
        #Validate Phone
        try:
            if self.phone.isdigit():
                if len(self.phone) == 10 or (len(self.phone) == 11 and self.phone[0] == '0'):
                    validphone = True
                else:
                    validphone = False
            else:
                validphone = False
        except:
            validphone = True
        '''else:
            if self.phone==None:                
                validphone = True
            else:
                validphone = False'''
        
        #Validate Username
        try:
            if len(self.uname)== 0:
                validuname = False
            else:
                con = sql.connect("caresys.db")
                cur = con.cursor()
                cur.execute("SELECT username FROM people WHERE username=?",(self.uname,))
                row = cur.fetchone()
                if row is None:
                    validuname = True
                else:
                    validuname = False
                    
        except:
            validuname = False
        '''elif self.uname==None:
            validuname = False
        else:
            validuname = True'''
        
        #Validate Password
        try:
            if len(self.pwd)== 0:
                validpwd = False
            else:
                self.pwd=base64.b64encode(self.pwd.encode("utf-8"))
                validpwd = True
        except:
            validpwd = False
        '''elif self.pwd==None:
            validpwd = False
        else:
            self.pwd=base64.b64encode(self.pwd.encode("utf-8"))
            validpwd = True'''
        
        #Validate UserType
        if self.utype == 1 or self.utype == 2:
            validutype = True
        elif self.utype==None:
            validutype = False
        else:
            validutype = False
            
        #Return Validation
        if validname==validage==validlocation==validphone==validuname==validpwd==validutype:
            return True
        else:
            return False       
    #END OF SHOW MODULE
    
    #BEGINING OF SIGNUP MODULE
    def signup(self):
        print("\nEnter Following Details to Continue..")
        #Get Name and Error Checking
        while True:
            self.name=input("\tName: ")
            print(self.name)
            if len(self.name)==0:
                print("Insufficient characters. Please try again...")
            elif all(x.isalpha() or x.isspace() for x in self.name):
                if self.name=="exit":
                    return None
                else:
                    break             
            else:
                print("Expecting only Alphabets. Please try again...")
        
        #Get Age and Error Checking
        try:
            self.age=int(input("\tAge: "))
        except:
            self.age=None
        
        #Get Location and Error Checking
        while True:
            self.location=input("\tLocation: ")
            if len(self.location)== 0:
                self.location=None
                break
            elif all(x.isalpha() or x.isspace() for x in self.location):
                break
            else:
                print("Expecting only Alphabets. Please try again...")
        
        #Get Phone and Error Checking
        while True:       
            self.phone=input("\tContact Number: ")
            if self.phone.isdigit():
                if len(self.phone) == 10 or (len(self.phone) == 11 and self.phone[0] == '0'):
                    break
                else:
                    print("Not a valid phone number. Please try again...")
            else:
                if len(self.phone)==0:
                    self.phone=None
                    break
                else:
                    print("Not a valid phone number. Please try again...")
        
        #Get Username
        while True:
            self.uname=input("\tUserName: ")            
            if len(self.uname)== 0:
                print("Username length too short. Please try again...")
                continue            
            else:
                con = sql.connect("caresys.db")
                cur = con.cursor()
                cur.execute("SELECT username FROM people WHERE username=?",(self.uname,))
                row = cur.fetchone()
                if row is None:
                    con.close
                    break
                else:
                    print("Username Already Exist. Please try again...")
                    continue
        
        #Get Password , Confirm Password , Password Masking and Encryption
        while True:
            pwd=getpass.getpass("\tPassword: ")
            if len(pwd)== 0:
                print("Password length too short. Please try again...")
                continue
            cpwd=getpass.getpass("\tConfirm Password: ")
            if pwd != cpwd:
                print("Passwords don't match. Please try again...")
            else:
                self.pwd=base64.b64encode(pwd.encode("utf-8"))
                break
        
        #Display UserType Options  
        time.sleep(.75)
        tableview=PrettyTable()
        tableview.field_names=["Option","UserType"]
        tableview.add_row([1,'CareSeeker'])
        tableview.add_row([2,'CareTaker'])
        print(tableview)    
        time.sleep(1)
        
        #Get UserType and Error Checking
        while True:
            try:
                self.utype=int(input("\tUserType: "))
                if self.utype == 1 or self.utype == 2:
                    break
                else:
                    print('Enter Valid Option')
                    continue
            except:
                print('Enter Valid Option')
    #END OF SIGNUP MODULE
    
    def login():
        while True:
            print("\nEnter Following Details to Continue..")
            uname=input('\tUsername: ')
            
            con = sql.connect("caresys.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM people WHERE username=?",(uname,))
            row = cur.fetchone()
            if row is None:
                print("This user does not exist. Please register first or try again.")
                time.sleep(2)
                continue
            else:
                pwd=getpass.getpass("\tPassword: ")
                pwd=base64.b64encode(pwd.encode("utf-8"))                
                if pwd == row[3]:
                    print("Verifying...")
                    time.sleep(0.75)
                    print("Login Success! Welcome {}".format(row[1]))
                    break
                else:
                    print("Incorrect Password! Please try again...")
                    time.sleep(2)
                


def logo():
    fhand=codecs.open('ASCII_Art.txt', encoding='utf-8')
    os.system('cls')
    for line in fhand:
        print(line,end='')
        time.sleep(0.2)
    print('\n')
        
def listoption(title,options,submenu):
    menu=PrettyTable()
    menu.field_names=title
    for i in range(len(options)):
        menu.add_row([options[i],submenu[i]])
    return menu

def exitprotocol():
    print("Exiting Program...")
    time.sleep(1)
    print("CareAll Created by Amal Salvin")
    time.sleep(0.5)
    print("Reach Out through:")
    time.sleep(0.5)
    print(" >Email:amalsalvin97@gmail.com")
    time.sleep(0.25)
    print(" >Twitter:amsvn")
    time.sleep(0.25)
    
    
#person.login()
#p1=person("Amal Salvin","amsvn","appu",2)   
'''if __name__=='__main__':
    import art as g
    g.asciiart()
    #p1=person("Amal Salvin","amsvn","appu",2)
    p1=person()
    p1.show()
'''    

if __name__=='__main__':
    maintitle=["Options","SubMenus"]
    mainop=[1,2,3,4]
    mainsub=["New User? REGISTER","Have Account? LOGIN","VIEW REPORT","EXIT"]
    logo()
    while True:
        menu=listoption(maintitle,mainop,mainsub)
        menu.align["SubMenus"] = "r"
        print(menu)
        print("Enter valid option...")
        time.sleep(1)
        try:
            choice=int(input("Choose: "))
            if choice==1:
                 p=person()
            elif choice==2:
                person.login()
            elif choice==3:
                person.show()
            elif choice==4:
                exitprotocol()
                break
            else:
                print("Invalid option! Please try again...")
                continue
        except:
            print("Invalid option! Please try again...")
            continue
        
        

    