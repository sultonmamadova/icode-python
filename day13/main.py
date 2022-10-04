# import db
# print(db.db)

from db import db
from db import db as db_data

from forms.person_form import PersonForm


print(db)
print(db_data)

form = PersonForm(name="Shodmon", surname="Ravshanov", age=19)
print(form.to_dict())
