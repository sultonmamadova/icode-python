x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
operation = input("Введите операцию. Доступны +*-/: ")

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def division(x, y):
    return x / y

def multiply(x, y):
    return x * y

if operation == "+":
    result = plus(x, y)
elif operation == "-":
    result = minus(x, y)
elif operation == "*":
    result = division(x, y)
elif operation == "/":
    result = multiply(x, y)
else:
    print("Мы не поддерживаем такую операцию.")

print(f"{x} {operation} {y} = {result}") # 1 + 2 = 3
