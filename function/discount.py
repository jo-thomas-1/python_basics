# build two functions for discounting price
# Function number 1 is for student discount - 10%
# Function number 2 is for additional discount for regular buyers - 5%

def student_discount(amount):
    return amount - (amount * 0.1)

def regular_discount(amount):
    return amount - (amount * 0.05)

price = 300
print("Product price:", price)
print("Discounted price:", regular_discount(student_discount(price)))
