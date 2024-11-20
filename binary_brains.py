import argparse
import time

''' QUESTION | Predicates and Quantifiers
Write a program that:
- Allows the user to enter quantified statements about students in this class 
(e.g., "Some students in this class are from Australia", 
"All students in this class love football", 
"Everyone in this class has been on TV").

- Translates the statements into logical expressions using predicates, quantifiers, and logical connectives.
You will provide two solutions:
    1. Let the domain consist of the students in your class.
    2. Let it consist of all people.
'''

def identify_quantifier(statement):
    """
    Identifies and returns the logical quantifier symbol from a given statement.
    """
    # Convert statement to lowercase for better matching
    statement = statement.lower().strip()
    
    quantifiers = {
        "all": "∀x", 
        "everyone": "∀x", 
        "every": "∀x", 
        "everybody": "∀x",  # Added this
        "some": "∃x", 
        "at least one": "∃x", 
        "there is one": "∃x", 
        "there exists": "∃x", 
        "someone": "∃x", 
        "any": "∃x",
        "none": "¬∃x"  # Added negation quantifier
    }
    
    # Check for multi-word quantifiers first
    for phrase in ["at least one", "there is one", "there exists"]:
        if phrase in statement:
            return quantifiers[phrase]
    
    # Then check single words
    for word in statement.split():
        if word in quantifiers:
            return quantifiers[word]
    
    return None

def detect_domain(statement):
    """
    Detects whether the statement is about students or people in general.
    """
    statement = statement.lower().strip()
    
    # Expanded indicators for better detection
    student_indicators = ['student', 'students', 'class', 'classmate', 'classmates']
    people_indicators = ['people', 'everyone', 'everybody', 'person', 'persons', 'human']
    
    # Check for student indicators first
    for indicator in student_indicators:
        if indicator in statement:
            return 'students'
            
    # Then check for people indicators
    for indicator in people_indicators:
        if indicator in statement:
            return 'people'
            
    # Default to students if no specific domain is detected
    return 'students'

def plural_to_singular(predicate):
    """
    Converts plural forms to singular in the predicate.
    """
    # Common plural-to-singular mappings
    plural_mappings = {
        'are': 'is',
        'were': 'was',
        'have': 'has',
        'do': 'does',
        'like': 'likes',
        'love': 'loves',
        'hate': 'hates',
        'want': 'wants',
        'need': 'needs',
        'make': 'makes',
        'take': 'takes',
        'go': 'goes',
        'study': 'studies',
        'watch': 'watches',
        'play': 'plays'
    }
    
    words = predicate.split()
    for i, word in enumerate(words):
        if word in plural_mappings:
            words[i] = plural_mappings[word]
    
    return ' '.join(words)

def validate_statement(statement):
    """
    Validates the input statement and provides guidance if needed.
    
    Args:
        statement (str): The input statement to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not statement or not statement.strip():
        return False, "Error: Empty statement provided."
        
    # Convert to lowercase for checking
    statement = statement.lower().strip()
    
    # Check for statements starting with 'not'
    if statement.startswith('not'):
        return False, """Error: Please don't start statements with 'not'. 
                Instead of 'Not all students...', use 'None of the students...'
                Example: 
                - Instead of: 'Not all students like math'
                - Use: 'None of the students like math'"""
                    
    return True, None

def translate_statement(statement):
    """
    Translates a quantified statement into logical expressions for both domains,
    showing both forms of negation when applicable.
    """
    if not statement or not statement.strip():
        return "Error: Empty statement provided.", "Error: Empty statement provided."

    # Validate the statement first
    is_valid, error_message = validate_statement(statement)
    if not is_valid:
        return error_message, error_message

    # Get the quantifier symbol
    quantifier_symbol = identify_quantifier(statement)
    if not quantifier_symbol:
        error_msg = "Error: Quantifier not recognized. Please include a valid quantifier (e.g., all, some, none)."
        return error_msg, error_msg

    try:
        # Clean up the statement and extract predicate
        words_to_remove = [
            'students', 'student', 'people', 'person', 'everyone', 'everybody',
            'in', 'this', 'class', 'classmate', 'classmates', 'human', 'humans',
            'none', 'of', 'the'  # Added these words to remove
        ]
        
        # Split the statement and filter out words to remove
        words = statement.lower().split()
        predicate = ' '.join(word for word in words 
                           if word.lower() not in words_to_remove)
        
        # Remove quantifier words
        quantifier_words = [
            "all", "everyone", "every", "some", "at least one", 
            "there is one", "there exists", "someone", "any", "none of the",
            "none", "no"  # Added these quantifier words
        ]
        for quant in quantifier_words:
            predicate = predicate.replace(quant, "").strip()
        
        # Clean up any extra spaces and punctuation
        predicate = ' '.join(predicate.split())
        predicate = predicate.strip('.,!?')
        
        if not predicate:
            return "Error: Unable to extract predicate from statement.", "Error: Unable to extract predicate from statement."

        # Convert plural forms to singular
        predicate = plural_to_singular(predicate)

        # Generate expressions for both domains
        predicate_variable = "P(x)"
        domain_variable = "Q(x)"

        # For All People domain
        if "¬" in quantifier_symbol:  # For "none" statements
            # First form using ¬∃
            people_expression_1 = f"¬∃x ({domain_variable} ∧ {predicate_variable})"
            # Second form using ∀¬ (De Morgan's Law)
            people_expression_2 = f"∀x ¬({domain_variable} ∧ {predicate_variable})"
            people_expression = f"{people_expression_1}\n   = {people_expression_2}, where {domain_variable} = 'x is a person' and {predicate_variable} = 'x {predicate}'"
        elif quantifier_symbol == "∀x":  # For "all" statements
            people_expression = f"{quantifier_symbol} ({domain_variable} → {predicate_variable}), where {domain_variable} = 'x is a person' and {predicate_variable} = 'x {predicate}'"
        else:  # For "some" statements (∃x)
            people_expression = f"{quantifier_symbol} ({domain_variable} ∧ {predicate_variable}), where {domain_variable} = 'x is a person' and {predicate_variable} = 'x {predicate}'"

        # For Students domain
        if "¬" in quantifier_symbol:  # For "none" or "not all" statements
            # First form using ¬∃
            students_expression_1 = f"¬∃x ({predicate_variable})"
            # Second form using ∀¬ (De Morgan's Law)
            students_expression_2 = f"∀x ¬({predicate_variable})"
            students_expression = f"{students_expression_1}\n   = {students_expression_2}, where {predicate_variable} = 'x {predicate}'"
        else:
            students_expression = f"{quantifier_symbol} ({predicate_variable}) where {predicate_variable} = 'x {predicate}'"
            
        return people_expression, students_expression
            
    except Exception as e:
        error_msg = f"Error: An unexpected error occurred while processing the statement: {str(e)}"
        return error_msg, error_msg

def print_welcome_banner():
    banner = """
    =========================================
    |       WELCOME TO THE BINARY BRAINS    |
    |      QUANTIFIED STATEMENT TRANSLATOR  |
    =========================================
    """
    print(banner)

def print_menu():
    print("\n========== Main Menu ==========")
    print("1. Translate to a quantified logic")
    print("2. Help")
    print("3. Exit")
    print("=================================")

def print_help():
    help_text = """
    ================== HELP MENU ===================
    1. Translate to a quantified logic:
        - Enter a quantified statement (e.g., "All students love math")
        - Provide a domain (e.g., "students")
    

    3. Help:
        - Displays this help menu.

    4. Exit:
        - Exits the program.

    Example Statement: "Some students love ice cream"
    Example Domain: "students"
    ================================================
    """
    print(help_text)

def handle_choice(choice, statement, _):
    """
    Handles user menu choices and statement translation.
    """
    if choice == '1':
        if not statement or not statement.strip():
            print("\nError: Please enter a valid statement.")
            return
            
        people_result, students_result = translate_statement(statement)
        if people_result.startswith("Error"):
            print(f"\n{people_result}")
        else:
            print("\nResults:")
            print(f"\nDomain: All People")
            print(f"Logical Expression: {people_result}")
            print(f"\nDomain: Students in this class")
            print(f"Logical Expression: {students_result}")
    elif choice == '2':
        print_help()
    elif choice == '3':
        print("Exiting...")
        time.sleep(1)
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    parser = argparse.ArgumentParser(description="Binary Brain Quantified Statement Translator")
    parser.add_argument('statement', nargs='?', type=str, 
                       help='Quantified statement to translate (e.g., "All students love math")')
    args = parser.parse_args()

    # Check if command-line argument is provided
    if args.statement:
        print_welcome_banner()
        people_result, students_result = translate_statement(args.statement)
        print("\nResults:")
        print(f"\nDomain: All People")
        print(f"Logical Expression: {people_result}")
        print(f"\nDomain: Students in this class")
        print(f"Logical Expression: {students_result}")
    else:
        # Enter interactive mode
        print_welcome_banner()
        while True:
            print_menu()
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                # Loop for entering a statement
                while True:
                    statement = input("Enter a quantified statement: ").strip()
                    if statement:
                        handle_choice(choice, statement, '')
                        # Prompt for entering another statement or returning to the main menu
                        next_step = input("\nEnter '1' to enter another statement, '2' to return to the main menu: ").strip()
                        if next_step == '1':
                            continue  # Allow the user to enter another statement
                        elif next_step == '2':
                            break  # Break and go back to the main menu
                        else:
                            print("Invalid input. Please enter '1' to enter another statement or '2' to return to the main menu.")
                    else:
                        print("Statement cannot be empty.")
            elif choice == '2':
                handle_choice(choice, '', '')
            elif choice == '3':
                handle_choice(choice, '', '')
            else:
                print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()