
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


def main():
    while True:
        try:
            return int(input("enter age: "))
        except ValueError:
            print("wrong value")

print(main())
