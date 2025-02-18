def main():
1.Calculate the factorial of a number using both a for loop and a while loop.
result = 1
# Factorial for loop
num = int(input("Enter a number to find the factorial of: "))
if num <= 0:
        print("Number must be greater than 0!\n")
else:
    for i in range(1,num+1):
        result = result*i
    print(result)

Factorial while loop
num = int(input("Enter a number to find the factorial of: "))
if num <= 0:
        print("Number must be greater than 0!\n")
else:
    while num > 0:
        result = result*num
        num -=1
    print(result)

#2.Find the sum of all numbers in a user-provided range using a loop.
result = 0
num = int(input("Enter a number to find the sum of number: "))
if num <= 0:
        print("Number must be greater than 0!\n")
else:
    for i in range(1,num+1):
        result = result+i
    print(result)

#Bonus challenge: "Can you write a program to generate the first 10 numbers in the Fibonacci sequence?"
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)

if __name__ == "__main__":
    main()