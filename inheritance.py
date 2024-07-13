class Add_sub:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
  
class Mul_div(Add_sub):
    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self,num1,num2):
        return num1/num2
cal1=Add_sub()
cal2=Mul_div()

print("Addition",cal1.add(10,20))
print("Subtraction",cal1.subtract(20,30))
print("Multiplication",cal2.multiply(10,10))
print("division",cal2.divide(100,10))

