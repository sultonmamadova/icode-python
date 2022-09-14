def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def division(x, y):
    return x / y

def multiply(x, y):
    return x * y

def get_function(operation):
    functions = {
        "+": plus,
        "-": minus,
        "*": multiply,
        "/": division,
    }
    return functions.get(operation)

def calculator():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    operation = input("Введите операцию. Доступны +*-/: ")
    action = get_function(operation=operation)
    result = action(x, y)
    print(f"{x} {operation} {y} = {result}") # 1 + 2 = 3

def main(first=False):
    while first or input("stop n/y? ") != "y":
        first = False
        calculator()

    print("Bye-bye")

main(first=True)

# recursion
# def stop():
#     return input("stop n/y? ") == "y"

# def main(first=False):
#     if not first and stop():
#         print("Bye-bye")
#         return
#     else:
#         calculator()
        

#     main()

# main(True)
