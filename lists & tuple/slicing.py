# create a new list from an existing list
# create a list and print from 2nd index to 6th index

fruits = ["apple", "orange", "pineapple", "jackfruit", "coconut", "banana", "mango"]
new_list = fruits[:]
print("New list: {0}, {1}, {2}, {3}, {4}, {5}, {6}".format(*new_list))
print("2nd to 6th index: {1}, {2}, {3}, {4}, {5}".format(*new_list))
