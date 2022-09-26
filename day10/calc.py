class Calculator:

    def plus(self, x, y):
        return x + y

    def minus(self, x, y):
        return x - y

    def division(self, x, y):
        return x / y

    def multiply(self, x, y):
        return x * y

    def calculate(self, x, y, operation):
        if operation == "+":
            result = self.plus(x, y)
        elif operation == "-":
            result = self.minus(x, y)
        elif operation == "*":
            result = self.division(x, y)
        elif operation == "/":
            result = self.multiply(x, y)
        else:
            result = None
        return result

def get_data():
    # v1 
    # x = int(input("Введите первое число: "))
    # y = int(input("Введите второе число: "))
    # operation = input("Введите операцию. Доступны +*-/: ")
    
    # v2
    # x = 1
    # y= 2
    # operation = "+"
    
    return (1, 2, "+")

def main():
    calculator = Calculator()
    x, y, operation = get_data()
    result = calculator.calculate(x, y, operation)
    print(f"{x} {operation} {y} = {result}")

main()
