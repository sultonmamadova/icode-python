import pprint
 
stroku = "hello world"
# print(isinstance(stroku, int))

# l = [True, False, True, False]
# print(all(l))


print(hasattr(stroku, "startswith"))
print(getattr(stroku, "startswith"))

stroku_startswith = getattr(stroku, "startswith")
print(stroku_startswith("hello"))

# setattr
# getattr