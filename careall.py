#from prettytable import PrettyTable
class Person:
    seeker=[]
    taker={}
    accept={} #Keeps track of dict{caretaker:[careseeker]} 
    association={} #Keeps track of dict{careseeker:caretaker}
    salarydict={} #Keeps track of dict{caretaker:[associatedcareseeker.salary]}
    relationdict={}
    assodict={}
    MAX=4
    
    def __init__(self,name=None,uname=None,password=None,utype=None):
        self.name=name
        self.uname=uname
        self.password=password
        self.utype=utype
        
    def dis(self):
        print(self.name)
        print(self.utype)
        print(self.uname)
        print(self.password)
        
    def review(self,about,rating,review):
        self.by=self.name
        self.about=about.name
        self.rating = rating
        self.review = review
        #print("Give Rating and Review about ",self.about)
        #print("Rating:")
        #print(" >10 - Very Good")
        #print(" >0 - Very Bad")
        #try:
        #    self.rating=int(input("Rating: "))
        #    if self.rating>0 and self.rating<10:
        #        pass
        #    else:
        #        print("Invalid Rating")
        #except:
        #    print("Expecting Integer Values")
        #self.review = input("Review: ")
        #menu=PrettyTable()
        #menu.field_names=['ReviewedBy','ReviewedAbout','Rating','Review']
        #menu.add_row([self.by,self.about,self.rating,self.review])
        
        print('ReviewedBy: {}'.format(self.by))
        print('ReviewedAbout:',self.about)
        print('Rating:',self.rating)
        print('Review: {}\n'.format(self.review))
        
    def report():
        print("Showing who is taking care of older couple:")
        print("-"*50)
        for k,v in Person.assodict.items():
            print(' >{} is taking care of {} : ({},{})'.format(v,k,v,k))
        
        print("\nShowing who all a young chap is currently taking care:")
        print("-"*50)
        for k,v in Person.relationdict.items():
            print(' >{} is currently taking care of {}'.format(k,v))        
        
class careseeker(Person):   
    
    def __init__(self,name=None,uname=None,password=None):
        self.utype=1
        Person.__init__(self,name,uname,password,self.utype)
        self.jobactive=False
    
    def jobcreate(self,payment,desc=None,duration=1):
        if not self.jobactive:
            self.desc=desc
            self.payment=payment
            self.duration=duration
            self.jobactive=True
            print("Job Created by {} is ACTIVE".format(self.name))
            Person.seeker.append(self)
        else:
            print("{} Cant Create New job since a job is Currently Active!".format(self.name))
    
    def viewapplication(self):
        print("Applicant\'s for {}\'s job are:".format(self.name))
        optioncounter = 0
        for k,v in Person.taker.items():
            if k is self:
                for i,x in enumerate(v): #for printing list inside dict
                    print(i+1,x.name)
    
    def jobaccept(self,option):
        if Person.accept.get(Person.taker[self][option-1]) == None:
            Person.accept[Person.taker[self][option-1]]=[]
            Person.accept[Person.taker[self][option-1]].append(self)
            Person.relationdict[Person.taker[self][option-1].name]=[]
            Person.relationdict[Person.taker[self][option-1].name].append(self.name)            
            
            if Person.association.get(self) is None:
                Person.association[self]=Person.taker[self][option-1]
                Person.assodict[self.name]=Person.taker[self][option-1].name
                print("{} Accepted {}".format(self.name,Person.association[self].name))
                
                if Person.salarydict.get(Person.taker[self][option-1]) == None:
                    Person.salarydict[Person.taker[self][option-1]]=[]
                    Person.salarydict[Person.taker[self][option-1]].append(self.payment)
                else:
                    Person.salarydict[Person.taker[self][option-1]].append(self.payment)
            else:
                print("You Cannot Accept New Applicant. You are on a contract with {}".format(Person.association[self].name))
                del Person.accept[Person.taker[self][option-1]]
                del Person.relationdict[Person.taker[self][option-1].name]
        
        else:
            
            if(len(Person.accept[Person.taker[self][option-1]])>=Person.MAX):                
                print('{}\'s Maximum Limit had Reached'.format(Person.taker[self][option-1].name))
            else:
                Person.accept[Person.taker[self][option-1]].append(self)
                Person.relationdict[Person.taker[self][option-1].name].append(self.name)
                
                if Person.association.get(self) is None:
                    Person.association[self]=Person.taker[self][option-1]
                    
                    Person.assodict[self.name]=Person.taker[self][option-1].name
                    print("{} Accepted {}".format(self.name,Person.association[self].name))
                    
                    if Person.salarydict.get(Person.taker[self][option-1]) == None:
                        Person.salarydict[Person.taker[self][option-1]]=[]
                        Person.salarydict[Person.taker[self][option-1]].append(self.payment)
                    else:
                        Person.salarydict[Person.taker[self][option-1]].append(self.payment)
                else:
                    print("You Cannot Accept New Applicant. You are on a contract with {}".format(Person.association[self].name))
        
        
    def jobclose(self):
        self.jobactive=False

class caretaker(Person):
    
    def __init__(self,name=None,uname=None,password=None):
        self.utype=2
        self.applied=[]
        Person.__init__(self,name,uname,password,self.utype)
            
    def jobview(self):
        print("JOB list for {}".format(self.name))
        for i,x in enumerate(Person.seeker):
            self.joboption=i+1
            print(self.joboption,x.name,x.payment)
    
    def apply(self,option):
        if Person.taker.get(Person.seeker[option-1]) == None:
            Person.taker[Person.seeker[option-1]]=[]
            Person.taker[Person.seeker[option-1]].append(self)
        else:
            Person.taker[Person.seeker[option-1]].append(self)
        print("{} Applied for {}".format(self.name,Person.seeker[option-1].name))
    
    def salary(self):
        sum=0
        for i in Person.salarydict[self]:
            sum=sum+i
        print(sum)
