def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def division(x, y):
    return x / y

def multiply(x, y):
    return x * y

def get_action(operation, x, y):
    if operation == "+":
        result = plus(x, y)
    elif operation == "-":
        result = minus(x, y)
    elif operation == "*":
        result = division(x, y)
    elif operation == "/":
        result = multiply(x, y)
    else:
        result = None
    return result

def main():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    operation = input("Введите операцию. Доступны +*-/: ")
    result = get_action(operation, x, y)
    print(f"{x} {operation} {y} = {result}") # 1 + 2 = 3

main()
