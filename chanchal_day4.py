"""Exercise 1: List Manipulation
"Create a list of numbers. Write code to add, remove, and sort the elements."
Exercise 2: Dictionary Lookup
"Build a contact book using a dictionary. Allow users to look up and add phone numbers."
Exercise 3: Set Operations
"Compare two datasets using sets. Find common and unique values."
"""
"""1. List Manipulation
"Create a list of numbers. Write code to add, remove, and sort the elements"""
def main():
    dataset1 = {1, 2, 3, 4, 5}
    dataset2 = {4, 5, 6, 7, 8}
    number_list = [2, 3, 4, 5, 6, 10, 12, 13]
    def insert_list():

        num = int(input("\t\t Enter Number:  "))
        index = int(input("\t\t Enter Index: "))
        number_list.insert(index,num)
        print(number_list)

    def remove_number_from_list():
        num = int(input("\t\t Enter Number:  "))
        number_list.remove(num)
        print(number_list)

    def sort_list():
        number_list.sort()
        print(number_list)

    """2: Dictionary Lookup
    "Build a contact book using a dictionary. Allow users to look up and add phone numbers"""
    contact_book = {}
    def add_contact():
        name = input("\t\t Enter Contact Name:  ").strip()
        phone = input("\t\t Enter Phone Number: ").strip()
        if name in contact_book:
            print("\t\t Contact Already exists! Update Number ")
        contact_book[name] = phone
        print( f"Contact {name} Updated succesfully")
    def search_one_contact():
        name = input("\t\t Enter the name to search!").strip()
        if name in contact_book:
            print(f"{name}'s phone number is :{ contact_book[name]} ")
        else:
            print("\t\t Contact not found")

    def display_contact_list():
        if contact_book:
            print("\t\t Contact List : ")
            for name, phone in contact_book.items():
                print(f"{name} : {phone}")
        else:
            print("\t Contact Book is Empty")

    """3.Set Operations
    "Compare two datasets using sets. Find common and unique values"""
    def compare_dataset(set1,set2):
        common_value = set1.intersection(set2)
        unique_set1 = set1-set2
        unique_set2 = set2-set1

        print(f"\t Common value: {common_value}")
        print(f"\t Unique value of set1 : {unique_set1}")
        print(f"\t Unique value of set2 : {unique_set2}")

    if __name__ == "__main__":
        main()


