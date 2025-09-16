# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string 


class calculator:
    def __init__(self,a:float,b:float,operation:str):
        self.a = a
        self.b = b
        self.operation=operation.lower()
    def calculate(self):
        if self.operation=="add" or self.operation=="addition":
            return self.a + self.b
        elif self.operation=="subtract" or self.operation == "subtraction":
            return self.a - self.b
        elif self.operation=="multiply" or self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "divide" or self.operation== "division":
            if self.b!=0:
                return self.a/self.b
            else:
                return "zero division error"
        else:
            return "invalid operation!"

a = float(input())
b = float(input())
operation = input()        
cal = calculator(a,b,operation)
res = cal.calculate()
print(res)        



