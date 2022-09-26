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
        if type(self.age) == int:
            return True
        elif not self.age < 18:
            return True

        return False

    def is_valid(self):
        error = [self.validate_age()]
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
    

    # print(form)

main()
