class Calculator:
    def __init__(self , first_num , second_num):
        self.first_num = first_num
        self.second_num = second_num
    
    def Addition(self):
        total = self.first_num + self.second_num
        return total

    def Subtraction(self):
        total = self.first_num + self.second_num
        return total
    
    def Multiplication(self):
        total = self.first_num * self.second_num
        return total
    
    def Division(self):
        total = self.first_num / self.second_num
        return total
decision = str(input("Enter Y if you want to use calculator else N:")).upper()

while decision == "Y":
    Number1 = float(input("Enter your first number:"))
    Number2 = float(input("Enter your Second number:"))
    result = Calculator(Number1 , Number2)
    operator = str(input("Enter your operator from (+ , - , * , /):"))

    if operator == "+":
        print(result.Addition())
    elif operator == "-":
        print(result.Subtraction())
    elif operator == "*":
        print(result.Multiplication())
    elif operator == "/":
        print(result.Division())
    decision = str(input("Enter Y if you want to use calculator else N:")).upper()
