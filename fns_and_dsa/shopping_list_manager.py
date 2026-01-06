from re import I


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add = input("Enter the item to add: " )
            shopping_list.append(add)
           # print(f"'{add}', Item added to list")
           # print(shopping_list)
            pass
        elif choice == '2':
            remove = input("Enter the item to remove: ")
            shopping_list.remove(remove)
            #print(f"'{remove}' item has been removed")
            #print(shopping_list)
            pass
        elif choice == '3':
            1
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()