import time

def print_ascii_banner():
    banner = """
    =========================================
    |          WELCOME TO THE COOL          |
    |      QUANTIFIED STATEMENT TRANSLATOR  |
    =========================================
    """
    print(banner)

def print_menu():
    print("\n========== Main Menu ==========")
    print("1. Translate to domain-specific logic")
    print("2. Translate to general logic")
    print("3. Help")
    print("4. Exit")
    print("=================================")

def print_help():
    help_text = """
    ================== HELP MENU ===================
    1. Translate to domain-specific logic:
        - Enter a quantified statement (e.g., "All students love math")
        - Provide a domain (e.g., "students")
    
    2. Translate to general logic:
        - Similar to option 1, but translates to a more general logical form.

    3. Help:
        - Displays this help menu.

    4. Exit:
        - Exits the program.

    Example Statement: "Some students love ice cream"
    Example Domain: "students"
    ================================================
    """
    print(help_text)

def handle_choice(choice, statement, domain):
    if choice == '1':
        print("\nDomain Specific Solution")
        print(f"Domain: {domain}")
        print(f"Logical Expression: {translate_to_logic(statement, domain)}")
    elif choice == '2':
        print("\nGeneral Solution")
        print(f"Logical Expression: {translate_to_general_logic(statement, domain)}")
    elif choice == '3':
        print_help()
    elif choice == '4':
        print("Exiting... Goodbye!")
        time.sleep(1)
        exit()
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    print_ascii_banner()
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

def translate_to_logic(statement, domain):
    # Placeholder function for demonstration purposes
    return f"Example translation of '{statement}' for domain '{domain}'."

def translate_to_general_logic(statement, domain):
    # Placeholder function for demonstration purposes
    return f"General translation of '{statement}' for domain '{domain}'."

if __name__ == "__main__":
    main()