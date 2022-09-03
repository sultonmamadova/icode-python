# simple function
def call_me():
    print("Ура. Я вызван!")

# call it
call_me()

# function with return
def some_function():
    return None


# function with attribute
def with_attr(attribute):
    print(attribute)

with_attr("Я атрибут")


# function with attribute and returning attribute
def i_will_return_it(attribute):
    return attribute


# function with action
def plus(attribute, attribute2):
    return attribute + attribute2

plus(2, 2)
# 4

# another action with attrs
def times(first, second):
    return first * second
