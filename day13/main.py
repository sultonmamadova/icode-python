# import db
# print(db.db)

from db import db
from db import db as db_data

from forms.person_form import PersonForm


if __name__ == "__main__":
    print(db)
    print(db_data)

    form = PersonForm(name="Shodmon", surname="Ravshanov", age=19)
    print(form.to_dict())
