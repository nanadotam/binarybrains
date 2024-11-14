import time

def main():
    print_welcome_banner()
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice in ['1', '2']:
            statement = input("Enter a quantified statement: ").strip()
            domain = input("Enter the domain of the statement: ").strip()
            if statement and domain:
                handle_choice(choice, statement, domain)
            else:
                print("Statement and domain cannot be empty. Please try again.")
        elif choice in ['3', '4']:
            handle_choice(choice, '', '')
        else:
            print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()