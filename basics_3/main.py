# Create a function , and calculated using the formula:

# Final Price(FP) = (Product Price of of X )/(Product Price of Y)^2.

# Write python code which can accept the price X and price of Y of a Product and calculate the FP.

# Note: Make sure to use a function which accepts the X and Y values and returns the FP value.

def final_price(x, y):
	return x / (y ** 2)

x = float(input("Enter product price of x: "))
y = float(input("Enter product price of y: "))
print("Final Price:", final_price(x, y))
