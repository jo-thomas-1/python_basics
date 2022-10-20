# Using while loop print values from 20 to 25 except 22

i = 20
while i <= 25:
	if i == 22:
		i = i + 1
		continue
	else:
		print(i)
		i = i + 1

# Using while loop print values from 20 to 30 but must stop on 28

i = 20
while i <= 30:
	if i == 28:
		break
	else:
		print(i)
		i = i + 1