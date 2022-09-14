def get_action(operation):
    actions = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    return actions.get(operation)

def main():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    operation = input("Введите операцию. Доступны +*-/: ")
    action = get_action(operation=operation)
    result = action(x, y)
    print(f"{x} {operation} {y} = {result}") # 1 + 2 = 3

main()
