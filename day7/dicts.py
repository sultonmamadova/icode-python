# Создание словарей


# создание пустого словаря
d = {}      # v1
d = dict()  # v2

# создание заполненного словаря
d = dict(key="value", key2="value2") # v1
d = {                                # v2
    "key": "value",
    "key2": "value2",
}


# получение значения в словаре по ключу
d["key"] # raises exception
d.get("key") # do not raise exception

print('d["key"] =', d["key"])

peremennaya = d["key"] # запись значения ключа key в переменную
print("peremennaya =", peremennaya)


# добавление нового ключа в словарь
car = {
    "brand": "Tesla",
    "model": "S",
    "speed": 250,
}
car["color"] = "white" # добавление нового ключа color со значением white в словарь car

print("car =", car)


# изменение существующего ключа в словаре
tesla = {
    "model": "S",
    "speed": 250,
    "color": "white",
}

tesla["speed"] = 340  # теперь равен 340
tesla["model"] = "Y"  # теперь model стало 


print("tesla = ", tesla)

# в качестве ключей в словаре могут быть только хешируемые объекты, но пока ограничемся только int, str
# в качестве значений в словаре может быть практически все что угодно


# разные ключи
different_keys = {
    "string_key": "какое-то значение", # здесь ключ str
    1: "а мой ключ это int", # здесь ключ int
}
print('db["string_key"] = ', different_keys["string_key"])
print('db[1] = ', different_keys[1])


# разные значения
db = {
    "a": 1, # значение int
    "b": "some str", # значение str
    "c": ["i'm", "a", "list", 1, 5, 8], # значение list
    "d": { # значение другой dict
        "key": "value",
        "another_key": "another value",
    },
    "e": ("i'm", "a", "tuple", 1, 5, 8), # значение tuple
}
print('db["string_key"] = ', db["string_key"])
print('db[1] = ', db[1])


# пример вложенного словаря

persons = {
    "shodmon@email.com": {
        "first_name": "Shodmon",
        "last_name": "Ravshanov",
        "age": 27
    },
    "zarina@email.com": {
        "first_name": "Zarina",
        "last_name": "Kadamova",
        "age": 18
    },
    "marjona@email.com": {
        "first_name": "Marjona",
        "last_name": "Khusnieva",
        "age": 33
    },
    "nigina@email.com": {
        "first_name": "Shodmon",
        "last_name": "Ravshanov",
        "age": 27
    }
}

print(persons["shodmon@email.com"]["first_name"]) # пример получения значения из вложенного словаря


# пример списка словарей
users = [
    {
        "email": "shodmon@email.com",
        "first_name": "Shodmon",
        "last_name": "Ravshanov",
        "age": 27
    },
    {
        "email": "zarina@email.com",
        "first_name": "Zarina",
        "last_name": "Kadamova",
        "age": 18
    },
    {
        "email": "marjona@email.com",
        "first_name": "Marjona",
        "last_name": "Khusnieva",
        "age": 33
    },
    {
        "email": "nigina@email.com",
        "first_name": "Nigina",
        "last_name": "Alambaeve",
        "age": 27
    }
]

print(users[0]["first_name"]) # пример получения значения из вложенного словаря
