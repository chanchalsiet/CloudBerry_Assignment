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
def sum_of_square():
    print("\n\t\t Sum of square!")
    try:
        num = int(input("Please Enter a Number : "))
        if num<=0:
            raise ValueError
        print(
        f"\n\t\t The sum of square is {sum([x**2 for x in range(1,num+1)])}\n "
        )
        input("Please Enter to continue: ")
        return None
    except  ValueError:
        print("\n Please enter the positive value")
        return sum_of_square()


def reverse_string():
    def reverse_word_in_place()
        split_str_rev = user_str.split(" ")
        word_rev = [word[::-1] for word in split_str_rev ]
        return f"\t\t\t Words Reverse in place :"{' '.join(word_rev)}

    def reverse_word_unchanged()
        split_str_rev = user_str.split(" ")[::-1]
        return f"\t\t\t Words Reverse unchanged :" { ' '.join(split_str_rev)}
    print("\n\t\t Reverse a string! ")

    try:
        user_str = input("\n What string you would like to reversed \n\t  Enter the text or Number : ").strip()
        if not user_str:
            raise ValueError("\t Hmm, Looks like you did't enter anything ...")
        print(f"\n\t\t String Reversed !: {user_str[::-1]} ")
        extra  = input("\t\t Type 'Extra' to see more other Press Enter \n\t\t")
        if extra.lower() == "extra"
            print(f"{_rev_word_inplace()}\n{_rev_word_unchanged()}\n")
            input("\t\t\tPress Enter to Continue")
        return None
    except ValueError as ve:
        print(ve)
        return reverse_string()

def main():
    def _intro_()
        print("\n\t\t What we are dealing with?")
        print("\t\t 'A' for String")
        print("\t\t '1' for Integer ")
        print("\t\t( Press Enter to Exit) ")
        try:
            user_choice = input("\t Whats your choice:")
            if not user_choice:
                return user_choice
            elif user_choice.lower() not in  ['A','1']:
                raise ValueError("\n\t Please Enter Valid Option!")
            return user_choice
        except ValueError as ve:
            print(ve)
            return _intro_()


        while True:
            






