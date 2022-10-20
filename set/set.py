# create a set
fruits_1 = {"banana", "orange"}
fruits_2 = {"apple", "banana"}

print("fruits set 1:", fruits_1)

# add an element
fruits_1.add("papaya")
print("after adding:", fruits_1)

# remove an element
fruits_1.remove("papaya")
print("after removing:", fruits_1)

# find difference of set
print("items unique to set 2:", fruits_2 - fruits_1)
