my_list = [1, 2, 3, 'apple', 'banana']

print(my_list)
print(my_list[0])

my_list.append(4)
print(my_list)
my_lenght=len(my_list)
print(my_lenght)
my_list.remove('apple')  # Removes 'apple' from the list

print(my_list)
new_list = my_list + [5, 6]  # Concatenates my_list with [5, 6]
print(new_list)
print(my_list)

another_list=my_list[0:4]
print(another_list)

test_list=[2,5,4,8,1]
test_list.sort()  # Sorts the list in ascending order
print(test_list)

# [1, 2, 3, 'apple', 'banana']
# 1
# [1, 2, 3, 'apple', 'banana', 4]
# 6
# [1, 2, 3, 'banana', 4]
# [1, 2, 3, 'banana', 4, 5, 6]
# [1, 2, 3, 'banana', 4]
# [1, 2, 3, 'banana']
# [1, 2, 4, 5, 8]
