# create a tuple and insert and append new values
# find the index of the 2nd last element

fruits = ("apple", "pineapple", "jackfruit", "coconut", "banana")
print("Tuple:", fruits)

temp = list(fruits)
temp.insert(2, "orange")
temp.append("mango")
fruits = tuple(temp)

print("Updates tuple:", fruits)

print("2nd last element:", fruits[-2])
