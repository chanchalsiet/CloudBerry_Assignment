def _get_user_num():
    try:
        num = int(input("\tPlease enter a number: "))
    except ValueError:
        print("\tThat's NOT a Number!\n")
        return _get_user_num()
    if num <= 0:
        print("Number must be greater than 0!\n")
        return _get_user_num()
    print()
    return num


def _get_user_choice():
    try:
        choice = int(input(
            """Pick a Mathematical Thing:\n
    Press 1: Factorial
    Press 2: Inclusive Sum
    Press 3: Fibonacci
    Press 4: Quit\n
Which would you like: """))
    except ValueError:
        print("Please Enter a Number!\n")
        return _get_user_choice()
    if not 0 < choice < 5:
        print("Please pick a valid option!\n")
        return _get_user_choice()
    return choice


def factorial():
    print("\tFind a Factorial!\n")
    num = _get_user_num()
    # While Loop

    w, w_total = num, 1
    while w > 0:
        w_total *= w
        w -= 1
    print(f"\tWhile Loop: !{num} = {w_total}")

    # For Loop
    f_total = 1
    for f in range(1, num + 1):
        f_total *= f
    print(f"\tFor Loop: !{num} = {f_total}")


def factorial_recur(num):
    # Limit 996 due to python recurssion limit
    if num > 1:
        return (num * factorial_recur(num - 1))
    return num


def inclusive_sum():
    print("\tGet the Natural Sum!\n")
    num = _get_user_num()
    # total = sum(range(1, num+1))
    total = 0
    for x in range(1, num + 1):
        total += x
    print(f"\tInclusive Sum of {num} = {total}")


def fibonacci():
    print('\tFind Fibonacci Numbers!\n')
    num = _get_user_num()
    fib = [0, 1]
    if num == 1:
        print(f"\tFibonacci Number {num}: {fib[0]}")
        return None
    for _ in range(2, num):
        fib.append(sum(fib[-2:]))
    for x in range(len(fib)):
        print(f"\tFibonacci Number {x + 1}: {fib[x]}")


def main():
    maths = {1: factorial,
             2: inclusive_sum,
             3: fibonacci,
             }
    while True:
        choice = _get_user_choice()
        print()
        if choice == 4:
            print("Goodbye!")
            break
        maths[choice]()
        input("\n\tPress any key to continue.")
        print()
        continue


if __name__ == '__main__':
    main()


    def function_name(parameters):


    # # Function body
    #     return value

    # return the greeting
    # def greet(name="James"):
    #     output = f"Hello {name}"
    #     return output

    # print(greet("Alice"))
    # print (greet())

    # def add_numbers(a, b):
    #     sum = a + b
    #     return sum

    # print(add_numbers(5,6))

    # def calculate_area(length, width):
    #     area = length * width
    #     return area

    # print (calculate_area(5,10))
    # try:
    #     num = int(input("Enter a number: "))
    #     print (f"You entered {num}")
    # except ValueError:
    #     print("Thats not a valid number!")

    # def divide_numbers(a,b):
    #     try:
    #         quotient = a/b
    #         return quotient
    #     except ZeroDivisionError:
    #         return "Cannot divide by zero!"
    # print (divide_numbers(10,0))

    # try:
    #     file = open("example.txt","r")
    #     content = file.read()
    # except FileNotFoundError:
    #     print ("File not found")
    # else:
    #     print("File read successfully")
    # finally:
    #     print("Closing the file")

    # def personalized_greet():
    #     name = input("What is your name? ").strip()
    #     if not name:
    #         print ("Hello stranger!")
    #     else:
    #         print (f"Hello {name}!")

    # personalized_greet()

    def calculator():
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /)")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                raise ValueError("Invalid operation!")
            return result
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")


    result = calculator()
    print(f"Result: {result}")

    """
    Homework:
    Write a function sum_of_squares that calculates the sum of squares of numbers
    from 1 to a given positive integer. Handle invalid or negative inputs gracefully.

    Write a function reverse_string that takes a string as input and returns the
    string reversed. Ensure the function handles empty strings and non-string inputs
    gracefully.

    Research two real-world scenarios where error handling is crucial (e.g., payment
    processing, file uploads)
        1) As cars are mainly software controlled (Electric in specific) improper
        error handling could mean issues within the electronics of the car to potentially
        causing an accident.
        2) On a less serious note, a website that doesnt handle errors properly
        will drive traffic away from the site which would impact any business/owner

    """


    def sum_of_squares():
        """Returns the sum of the squares of numbers in a list of [1, user_input],
        If a ValueError is raised, the function is recalled for correct input

        Raises:
            ValueError: If the user_input is 0 or less OR a str ValueError Raised

        Returns:
            None: prints the value and ends
        """

        print("\n\t\tSum of the Squares!")
        try:
            num = int(input("\tPlease Enter a Number: "))
            if num <= 0:
                raise ValueError
            print(
                f"\n\t\tThe sum of squares is: {sum([x ** 2 for x in range(1, num + 1)])}\n"
            )
            input("\t\tPress Enter to Continue")
            return None
        except ValueError:
            # Will catch both str errors and 0,-numbers
            print("\tPlease enter a valid positive number!")
            return sum_of_squares()


    def reverse_string():
        """Prints the requested string commands, returns None"""

        def _rev_word_inplace():
            """Leaves the words of the original string in place and reversed them

            Returns:
                str: The string reversed in place
            """
            split_str_rev = user_str.split(" ")
            word_rev = [word[::-1] for word in split_str_rev]
            return f"\t\t\tWords Reversed In Place: {' '.join(word_rev)}"

        def _rev_word_unchanged():
            """Reverses the str with words unchanged

            Returns:
                str: Reversed String
            """
            split_str_rev = user_str.split(" ")[::-1]
            return f"\t\t\tWords Reversed Intact: {' '.join(split_str_rev)}"

        print(("\n\t\tReverse a String!"))
        try:
            user_str = input(
                "\tWhat string would you like reversed?\n\tEnter Text and/or Numbers: "
            ).strip()
            if not user_str:
                raise ValueError("\tHmm, Looks like you didnt enter anything...")
            print(f"\n\t\tString Reversed: {user_str[::-1]}")
            extra = input("\t\tType 'Extra' to see more otherwise press Enter.\n\t\t")
            if extra.lower() == "extra":
                print(f"{_rev_word_inplace()}\n{_rev_word_unchanged()}\n")
                input("\t\t\tPress Enter to Continue")
            return None
        except ValueError as ve:
            print(ve)
            return reverse_string()


    def main():
        """Main function to handle program logic"""

        def _intro_():
            """User choice for type of command

            Raises:
                ValueError: If requested command does not exist

            Returns:
                user_choice:int|str: Command for function call
            """
            print("\n\tWhat are we dealing with?")
            print("\t\t'A' for Strings")
            print("\t\t'1' for Integers")
            print("\t\t(Press Enter to Exit)")
            try:
                user_choice = input("\tWhats your choice: ")
                if not user_choice:
                    return user_choice
                elif user_choice.lower() not in ["a", "1"]:
                    raise ValueError("\n\tPlease Select a valid option!")
                return user_choice
            except ValueError as ve:
                print(ve)
                return _intro_()

        while True:
            user_choice = _intro_()
            if not user_choice:
                print("\t\tGoodbye!")
                break
            try:
                int(user_choice)
                sum_of_squares()
            except ValueError:
                reverse_string()


    if __name__ == "__main__":
        main()