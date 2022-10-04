class Form:

    def __repr__(self):
        return f"Form{self.name, self.surname, self.age}"

    def get_validation_attrs(self):
        return [x for x in dir(self) if x.startswith("validate_")]

    def run_validations(self):
        l = []
        for attr in self.get_validation_attrs():
            if hasattr(self, attr):
                fn = getattr(self, attr)
                l.append(fn())
        return l

    def is_valid(self):
        error = self.run_validations()
        breakpoint()
        for x in error:
            if not x:
                return False

        return True

    def to_dict(self):
        if self.is_valid():
            return {
                "name": self.name,
                "surname": self.surname,
                "age": int(self.age)
            }

        raise ValueError("Form must be valid.")


class PersonForm(Form):

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

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
        if not isinstance(self.name, str):
            return False
        return True

    def validate_surname(self):
        if not isinstance(self.surname, str):
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
        form = PersonForm(user_data["name"], user_data["surname"], user_data["age"])
        
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
