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

# Aufgabe 3c

def deleteItem(key):
    del dictionary[key]

deleteItem("key1")
print(dictionary)

# Aufgabe 3d

def printKeys():
    for key in dictionary.keys():
        print(key)

printKeys()

