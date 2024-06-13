# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'Sydney'

}

# access the values by using keys
print(my_dict['name'])

# adding a new key-pair value
my_dict['email address'] = 'alice@example.com'

print(my_dict)

# change value of existing key overwrites the original value
my_dict['city'] = 'melbourne'

print(my_dict)

# removing a key value pair
del my_dict['age']
print(my_dict)
# Alternatively, you can use .pop()
my_dict.pop("email address")
print(my_dict)

# Check if specific key existence
print("name" in my_dict)

list_of_keys = my_dict.keys()
list_of_values = my_dict.values()

print(list_of_values)
print(list_of_keys)
print("-----")

# Iterate through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")


# nested_dictionaries
nested_dict = {
    'person_1: {______}',
    'person_2:{______}',
}