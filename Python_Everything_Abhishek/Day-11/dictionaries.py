my_dict = {
    
    'name': 'John',
    'age': 25,
    'city': 'New York'
    
    }
print(my_dict['name'])  # Output: John
print(my_dict['age'])
print(my_dict)
my_dict['age']=28
print(my_dict)
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
print(my_dict)
del my_dict['city']  # Removing a key-value pair
print(my_dict)

if 'age' in my_dict:
    print('Age is present in the dictionary')

if 'city' in my_dict:
    print('city is present in the dictionary')
else:
    print('city is not present in the dictionary')
    
for key, value in my_dict.items():
    print(key, value)    