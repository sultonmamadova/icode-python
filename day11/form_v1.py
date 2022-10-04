class Form:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return f"Form{self.name, self.surname, self.age}"

    def to_dict(self):
        if self.is_valid():
            return {
                "name": self.name,
                "surname": self.surname,
                "age": int(self.age)
            }

        raise ValueError("Form must be valid.")

    def validate_age(self):
        try:
            age = int(self.age)
        except TypeError:
            return False
        except ValueError:
            return False

        if age < 18:
            return False

        return True

    def validate_name(self):
        if type(self.name) != str:
            return False
        return True

    def validate_surname(self):
        if type(self.surname) != str:
            return False
        return True

    def is_valid(self):
        error = [self.validate_age(), self.validate_surname(), self.validate_name()]
        for x in error:
            if not x:
                return False

        return True

def get_user_input():
    name = input("name: ")
    surname = input("surname: ")
    age = input("age: ")

    return {
        "name": name,
        "surname": surname,
        "age": age,
    }

def app_fill_data():
    stop = "y"
    data = []
    while stop == "y":
        user_data = get_user_input()
        form = Form(user_data["name"], user_data["surname"], user_data["age"])
        
        if form.is_valid():
            data.append(form.to_dict())
            stop = input("Успешно. Хотите ввести еще (y/n)? ")
        else:
            stop = input("Неверные данные. Хотите ввести еще (y/n)? ")
    
    return data

def main():
    data = app_fill_data()
    print(data)

main()
