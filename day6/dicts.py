# Создание словарей

# пустой словарь
d = {}
print("d = {} ->", d)

d = dict()
print("d = dict() ->", d)


# заполненый словарь
d = dict(key="value", key2="value2")
print("d = dict(key=\"value\", key2=\"value2\") ->", d)

d = {
    "key": "value",
    "key2": "value2",
}

print("""d = {
        "key": "value",
        "key2": "value2",
    } -> """, d)


# получение значения в словаре по ключу
d["key"] # raises exception
d.get("key") # do not raise exception

print(d["key"])


peremennaya = d["key"]
print(peremennaya)
