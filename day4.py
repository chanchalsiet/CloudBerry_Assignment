"""Exercise 1: List Manipulation
"Create a list of numbers. Write code to add, remove, and sort the elements."
Exercise 2: Dictionary Lookup
"Build a contact book using a dictionary. Allow users to look up and add phone numbers."
Exercise 3: Set Operations
"Compare two datasets using sets. Find common and unique values."
"""
"""1. List Manipulation
"Create a list of numbers. Write code to add, remove, and sort the elements"""
number_list = [2,5,7,4,10]
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


def list_operation():
    print("\t\t List operation: ")
    print("\t\t A. Insert the Number in List")
    print("\t\t B. Remove the Number from List ")
    print("\t\t C. Short the List")
    print("\t\t D. Exit ")
    choice = input("Choose an option: ").strip()
    if choice == 'A':
        insert_list()
    elif choice == 'B':
        remove_number_from_list()
    elif choice == 'C':
        sort_list()
    elif choice == 'D':
        print("Exiting. Goodbye")
    else:
        print("Invalid Choice . Please Enter valid option.")

def contact_book():
    print("\t\t Contact Book Menu : ")
    print("\t\t 1. Add Contact Number ")
    print("\t\t 2. Search Contact ")
    print("\t\t 3. Display Contacts")
    print("\t\t 4. Exit ")
    choice = input("Choose an option: ").strip()
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_one_contact()
    elif choice == '3':
        display_contact_list()
    elif choice == '4':
        print("Exiting Contact Book. Goodbye")
    else:
        print("Invalid Choice . Please Enter valid option.")

def main():
    dataset1 = {1, 2, 3, 4, 5}
    dataset2 = {4, 5, 6, 7, 8}
    number_list = [2, 3, 4, 5, 6, 10, 12, 13]
    while True:
        print("\n\n\t\t What Option You want to perform  : ")
        print("\t\t Enter 'Set' for commpairing set ")
        print("\t\t Enter 'List' for perform list operation ")
        print("\t\t Enter 'Contact Book' for perform Contact Book operation ")
        print("\t\t 'Exit' You want to exit ")

        choice = input("Choose an option: ").strip()
        if choice == 'Set':
            compare_dataset(dataset1,dataset2)
        elif choice == 'List':
            list_operation()
        elif choice == 'Contact Book':
            contact_book()
        elif choice == 'Exit':
            print("Exiting. Goodbye")
            break
        else:
            print("Invalid Choice . Please Enter valid option.")


if __name__ == "__main__":
    main()

import random as r


# (Would be best if these were classes)

### Exercise 1: List Manipulation ###

def create_list():
    while True:
        try:
            user_input = int(
                input('\n\tHow many numbers would you like in the list: ')
            )
            if user_input <= 0:
                raise ValueError
            rand_list = [r.randrange(150) for _ in range(user_input)]
            print(f"\tCreated: {rand_list}\n")
            return rand_list
        except ValueError:
            print('\tPlease enter a positive non-zero integer.')


def add_to_list(list_x):
    while True:
        try:
            print(f"\n\t{list_x}")
            user_input = int(
                input("\tWhat number would you like to add to the list: ")
            )
            list_x.append(user_input)
            print(f"\tAdded to List: {list_x}\n")
            return None
        except ValueError:
            print("\tPlease enter a number.")


def remove_from_list(list_x):
    while True:
        try:
            print(f"\n\t{list_x}")
            user_input = int(
                input("\tWhat number would you like removed: ")
            )
            if user_input not in list_x:
                print(f"\t{user_input} is not in the list!")
                continue
            list_x.remove(user_input)
            print(f"\tRemoved from List: {list_x}\n")
            return None
        except ValueError:
            print("\tThat is not a number...")


def sort_list(list_x):
    list_x.sort()
    print(f"\n\tSorted List: {list_x}\n")
    return None


def list_manipulation():
    print("\t\tList Manipulation!")
    user_list = create_list()
    while True:
        print("\t1 - Add a Number, 2 - Remove a Number, 3 - Sort")
        user_input = input("\t(Press Enter to Quit): ")
        if user_input == '1':
            add_to_list(user_list)
        elif user_input == '2':
            remove_from_list(user_list)
        elif user_input == '3':
            sort_list(user_list)
        elif not user_input:
            print('\tGoodbye!\n')
            break
        else:
            print("\tPlease enter a valid option.\n")
    return None


### Exercise 2: Dictionary Lookup ###

def add_contact(c_book):
    while True:
        try:
            name = input("\n\tNew Contact Name: ")
            number = input("\tNew Contact Number: ")
            if number in c_book.keys():
                print("\tThis number is already in your contacts.")
                continue
            elif not name or not number:
                print("\tPlease dont leave any fields blank.")
                continue
            c_book[number] = name
            return None
        except Exception:
            print("\tHmm Something went wrong. Try again.\n")
    return None


def look_up_contact(c_book):
    while True:
        try:
            name = input("\n\tWho are you looking for: ")
            print()
            id_list = [
                key for key, value in c_book.items() if name.lower() in value.lower()
            ]
            if not id_list:
                print("\tNo Contacts by that name.")
                break
            for id in id_list:
                print(f"\tName: {c_book[id]}, Phone Number: {id}")
            return None
        except Exception:
            print("\tHmm Something went wrong. Try again.")
    return None


def dictionary_lookup():
    print("\t\tDictionary Lookup!")
    user_dict = {}
    while True:
        if not user_dict:
            print("\n\tLooks like you have no contacts, add someone!")
            add_contact(user_dict)
            continue
        print("\n\t1 - Add a Contact, 2 - Lookup a Contact")
        user_input = input("\t(Press Enter to Quit): ")
        if user_input == '1':
            add_contact(user_dict)
        elif user_input == '2':
            look_up_contact(user_dict)
        elif not user_input:
            print('\tGoodbye!\n')
            break
        else:
            print("\tPlease enter a valid option.\n")
    return None


### Exercise 3: Set Operations ###

def generate_sets():
    set1 = {r.randrange(1, 11) for _ in range(10)}
    set2 = {r.randrange(3, 14) for _ in range(10)}
    print("\n\tYour two sets are:")
    print(f"\t{set1}")
    print(f"\t{set2}")
    return set1, set2


def set_intersection(set1, set2):
    print("\n\tThe common values (intersection) of")
    print(f"\tSet1: {set1}\n\tSet2: {set2}")
    print(f"\tAre: {set1 & set2}")
    return None


def set_difference(set1, set2):
    print("\n\tThe unique values (difference) of each set")
    print(f"\tSet1: {set1}\n\tSet2: {set2}")
    print(f"\tAre: Set1 : {set1 - set2} and Set2 : {set2 - set1}")
    return None


def set_operations():
    print("\t\tSet Operations!")
    set1, set2 = generate_sets()
    while True:
        print("\n\t1 - See Intersection, 2 - See Difference")
        user_input = input("\t(Press Enter to Quit): ")
        if user_input == '1':
            set_intersection(set1, set2)
        elif user_input == '2':
            set_difference(set1, set2)
        elif not user_input:
            print('\tGoodbye!')
            break
        else:
            print("\tPlease enter a valid option.\n")


def main():
    list_manipulation()
    dictionary_lookup()
    set_operations()


if __name__ == '__main__':
    main()