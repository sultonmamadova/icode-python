# простая функция
def call_me():
    print("Ура. Я вызван!")

# вызов функции
call_me()

# функция с return
def some_function():
    return None


# функция с аргументом
def with_attr(argument):
    print(argument)

with_attr("Я атрибут")


# функция принимающая аргументом и возвращающая этот аргумент
def i_will_return_it(argument):
    return argument


# функция с каким-то действием (здесь, сложение двух аргументов)
def plus(argument, argument2):
    return argument + argument2

plus(2, 2)
# 4

# другая функция с каким-то действием (здесь, умножение двух аргументов)
def times(first, second):
    return first * second


# пример функции с каким-либо действием
def ya_vernu_resultat(perviy, vtoroy, tretiy):
    resultat = f"{perviy} {vtoroy} {tretiy}"
    return resultat

peremennaya = ya_vernu_resultat(1, 2, 3)
print(peremennaya)


# при вызове можно явно указать к какому аргументу относится значение
ya_vernu_resultat(1, 2, 3)  # вызов без указания к какому аргументу относятся значения
ya_vernu_resultat(vtoroy=2, perviy=1, tretiy=3)  # здесь мы явно указваем  к какому аргументу относятся значения
ya_vernu_resultat(1, 2, tretiy=3)  # смешаный вызов и явное указание и не явное указание одновременно
