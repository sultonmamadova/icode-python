from forms.form import Form


class PersonForm(Form):
    
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return f"PersonForm{self.name, self.surname, self.age}"
    
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
        if not isinstance(self.name, str):
            return False
        return True

    def validate_surname(self):
        if not isinstance(self.surname, str):
            return False

        return True 
