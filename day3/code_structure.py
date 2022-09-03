import jsonschema
from jsonschema.exceptions import best_match


class JSONSchemaValidator:
    """Validate JSON schema."""
    
    def compare(self, input, schema):
        best_error = best_match(jsonschema.Draft7Validator(schema).iter_errors(input))

        if best_error:
            raise ValueError(best_error.message)



def validate_with_no_special_char(value):
    if not value.isalnum():
        raise ValueError("This field must not include special value")


def validate_with_no_special_char_except_dot(value: str):
    if not value.replace(".", "").isalnum():
        raise ValueError("This field must not include special value")


if True:
    var = 1

    if var == 1:
        var = 2

        if var == 0:
            var = 0

        elif var > 1:
            var = 3

        else:
            var = 1

    print(var)

# if <expr>:
#     <statement>
#     <statement>
#     ...
#     <statement>

# <following_statement>