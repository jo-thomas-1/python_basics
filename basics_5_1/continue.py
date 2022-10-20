# Using while loop print values from 20 to 25 except 22

i = 20
while i <= 25:
	if i == 22:
		i = i + 1
		continue
	print(i)
	i = i + 1
