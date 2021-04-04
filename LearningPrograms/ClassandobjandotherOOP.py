class vehicle:
    def __init__(self,no):
        self.number=no
    def print1(self):
        print("This is a vehicle. Having number ", self.number)
    class car:
        def print2(self):
            print("You are in a car.")
    @staticmethod
    def print3():
        print("Called via class")

ob1=vehicle('MH031111')
ob2=vehicle('MH031112')
ob1.print1()
ob2.print1()

ob11=ob1.car()
ob11.print2()

ob1.print3()
ob2.print3()
vehicle.print3()