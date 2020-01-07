from main import person
from main import logo
from jobs import job

class careseeker(person,job):
    def __init__(self,name=None,uname=None,pwd=None,utype=None,age=None,location=None,phone=None,desc=None,salary=None,duration=None):
        person.__init__(self,name,uname,pwd,utype,age,location,phone)
        job.__init__(self,desc,salary,duration)

if __name__=='__main__':
    s1=careseeker(name="pillow",uname="pp",pwd="pp",utype=1,salary=2000)
    print(s1.utype)
    s1.create(s1.utype)
    logo()
    #o1=careseeker("Amal Salvin","amsvn","appu",2)