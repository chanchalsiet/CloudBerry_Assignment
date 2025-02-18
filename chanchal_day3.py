
"""
1. Write a function sum_of_squares that calculates the sum of squares of numbers from 1 to a given positive
 integer. Handle invalid or negative inputs gracefully"""
def sum_of_square(num):
    try:
        num = int(num)
        if num < 0:
            raise ValueError("Input must be a positive integer ")
        total = 0
        for i in range(1,num+1):
            total += (i**2)
        return total
    except (ValueError, TypeError):
        return "Invalid input. Please enter a positive integer."

num = input("Please enter the number : ")
sum_of_square = sum_of_square(num)
if sum_of_square:
    print("Sum of square is :", sum_of_square)


"""
2.Write a function reverse_string that takes a string as input and returns the string reversed. Ensure the
function handles empty strings and non-string inputs gracefully."""
def reverse_string(string):
    try:
        if not string :
            raise ValueError("String is empty")
        if string.isnumeric():
            raise ValueError("String is numeric")
        if string.isspace():
            raise ValueError("String not be blank")
        return string[::-1]
    except ValueError as e:
        print("Error:", e)

string = input("Enter a string: ")
reversed_string = reverse_string(string)
if reversed_string:
    print("Reversed string:", reversed_string)

"""
3.Research two real-world scenarios where error handling is crucial (e.g., payment processing, file uploads).
"""
"""A. payment processing"""

def process_payment(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient amount for payment")
    return balance - amount
try :
    user_balance = 2000
    payment_amount = 2500
    new_balance = process_payment(payment_amount, user_balance)
    print("Payment successful. Balance : ", new_balance)
except ValueError as ve:
    print("Payment Failed: ", ve )



