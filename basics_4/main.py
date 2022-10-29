# Write a function which would divide two numbers
# design the function in a manner that it handles the divide by zero exception

def divide(x, y):
	try:
		return x/y
	except:
		return "Division by 0 is not possible"

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
print("Result:", divide(a, b))
