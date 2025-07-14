class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b 
    
    def subtract(self, a, b):
        return a - b 
    
    def multiply(self, a, b):
        return a * b 
    
    def divide(self, a, b):
        if b != 0:
            return
        else:
            return "Cannot divide by zero"
        

my_calculator = Calculator()

sum_result = my_calculator.add(10, 5)
difference_result = my_calculator.subtract(10, 5)
product_retern = my_calculator.multiply(5, 8)
qoutient_retern = my_calculator.divide(12, 4)

print(sum_result)
print(difference_result)
print(product_retern)
print(qoutient_retern) 

         
    
    

