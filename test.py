from careall import Person
from careall import careseeker
from careall import caretaker

jayi=careseeker("Jayi")
salvin=careseeker("Salvin")
vinodh=careseeker("Vinodh")
jaya=careseeker("Jaya")
john=careseeker("John")
jessy=careseeker("Jessy")

amal=caretaker("Amal")
ajith=caretaker("Ajith")
riya=caretaker("Riya")
rini=caretaker("Rini")

jayi.jobcreate(1000)
salvin.jobcreate(500)
vinodh.jobcreate(1500)
jaya.jobcreate(2000)
john.jobcreate(600)
jessy.jobcreate(900)

amal.jobview()

rini.apply(4)
rini.apply(3)
rini.apply(1)
rini.apply(2)
rini.apply(6)
amal.apply(6)
riya.apply(6)

john.viewapplication()

vinodh.viewapplication()
jessy.viewapplication()

jayi.jobaccept(1)
jaya.jobaccept(1)
vinodh.jobaccept(1)
salvin.jobaccept(1)
jessy.jobaccept(1)
jessy.jobaccept(2)
jessy.jobaccept(3)

rini.salary()
amal.salary()

jayi.review(rini,5,"Good Caretaker but not punctual")
amal.review(jessy,8,"Nice Person")

Person.report()

