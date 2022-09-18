def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def division(x, y):
    return x / y

def multiply(x, y):
    return x * y

def get_function(operation):
    if operation == "+":
        function = plus
    elif operation == "-":
        function = minus
    elif operation == "*":
        function = division
    elif operation == "/":
        function = multiply
    else:
        function = None

    return function

def main():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    operation = input("Введите операцию. Доступны +*-/: ")
    function = get_function(operation=operation)
    result = function(x, y)
    print(f"{x} {operation} {y} = {result}") # 1 + 2 = 3

main()
