class parent1:
    "Patent class"
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def print1(self):
        print(self.firstname,self.lastname)
    def print3(self):
        print("This is print 3",self.firstname,self.lastname)
class child (parent1):
    "Child class"
    def __init__(self,fname,lname):
        super().__init__(fname, lname)
    def print1(self):
        print("This is over rided",self.firstname,self.lastname)
    def print2(self,age=None):
        if age is not None:
            print(self.firstname,self.lastname,"age is ",age)
        else:
            print(self.firstname,self.lastname)
#    def print2(self,age):
#        print(self.firstname,self.lastname,"age",age)

ob=child('naman','desai')
ob.print1()
ob.print2()
ob.print2(19)
ob.print3()
#ob.print2(19)