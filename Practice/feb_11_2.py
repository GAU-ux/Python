class A:
    def __init__(self,i):
        self.var = i;
    def printvar(self):
        print(self.var);

a = A(10)
# a.printvar()
a = A(20)
a.printvar()