dictionary = {"key1": "value1", "key2": "value2"}

print(dictionary)

# Aufgabe 3a

def printValue(key):
    print(dictionary[key])

printValue("key1")

# Aufgabe 3b

def valueIsEqual(key, value):
    return dictionary[key] == value

print(valueIsEqual("key1", "value1"))

