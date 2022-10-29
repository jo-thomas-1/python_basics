# Create a function to print month name based on integer value provided
def month(x):
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	return months[x - 1]

value = int(input("Enter the month value [1 - 12]: "))
print("Month:", month(value))

# Create a function to calculate simple interest
def simple_interest(p, n, r):
	# p - principal amount
	# n - number of years
	# r - rate of interest
	return (p*n*r)/100

principal = int(input("Enter the principal amount: "))
years = int(input("Enter the duration in years: "))
interest = int(input("Enter the rate of interest: "))
print("Simple Interest:", simple_interest(principal, years, interest))
