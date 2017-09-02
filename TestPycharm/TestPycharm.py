import string

class Father:
    def getname(self):
        print ("father: ",self)
    def getage(self):
        print ("father: 40")

class Child(Father):
    def getname(self):
        print ("child: ", self)

    def getfathername(self):
        print(Father.getname(Father))


child = Child()
child.getname()
child.getage()
child.getfathername()