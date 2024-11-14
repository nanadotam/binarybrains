import argparse


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


"""
Changes to be made:
- Add a menu interface (e.g. Press 1. to do something, Press 2. to do something else)
- Translate the statement from not to "not all students" to "∃ P(x) where P(x) = 'not all students'"
e.g. "none of the students like school" = "∃ P(x) where P(x) = 'none of the students like school" = "all students do not like school" 
"""



def identify_quantifier(statement):
    """
    Identifies and returns the logical quantifier symbol from a given statement.

    Args:
        statement (str): The input statement containing a quantifier.

    Returns:
        str: The logical quantifier symbol ('∀' for universal quantifiers, '∃' for existential quantifiers).
            Returns None if no quantifier is found.
    """
    quantifiers = {
        "all": "∀", 
        "everyone": "∀", 
        "some": "∃", 
        "at least one": "∃", 
        "there is one": "∃", 
        "there exists": "∃", 
        "someone": "∃", 
        "any": "∃"
    }
    for word in statement.split():
        if word.lower() in quantifiers:
            return quantifiers[word.lower()]
    return None


def extract_domain_and_predicate(statement, domain):
    """
    Extracts the quantifier and predicate from a given statement based on the specified domain.

    Args:
        statement (str): The statement containing the domain.
        domain (str): The domain to search for within the statement.

    Returns:
        tuple: A tuple containing the quantifier and predicate as strings if the domain is found,
            otherwise (None, None).
    """
    if domain in statement:
        parts = statement.split(domain)
        quantifier = parts[0].strip()
        predicate = parts[1].strip()
        return quantifier, predicate
    else:
        return None, None


def translate_to_logic(statement, domain):
    """
    Translates a natural language statement with a quantifier into a logical expression.

    Args:
        statement (str): The natural language statement containing a quantifier.
        domain (str): The domain of discourse for the statement.

    Returns:
        str: The logical expression representing the statement, or an error message if the quantifier or predicate cannot be identified.
    """
    quantifier_symbol = identify_quantifier(statement)
    if not quantifier_symbol:
        return "Quantifier not recognized. Please include a valid quantifier."

    quantifier, predicate = extract_domain_and_predicate(statement, domain)
    if not quantifier or not predicate:
        return "Unable to extract quantifier or predicate. Ensure the domain is correctly specified in the statement."

    # Representing predicate as P(x)
    predicate_variable = "P(x)"
    logical_expression = f"{quantifier_symbol} {predicate_variable} where {predicate_variable} = '{predicate}'"

    return logical_expression


def translate_to_general_logic(statement, domain):
    """
    Translates a given statement with a quantifier into a general logical expression.

    Args:
        statement (str): The statement containing a quantifier and a predicate.
        domain (str): The domain over which the quantifier operates.

    Returns:
        str: The general logical expression or an error message if the quantifier or predicate is not recognized.
    """
    quantifier_symbol = identify_quantifier(statement)
    if not quantifier_symbol:
        return "Quantifier not recognized. Please include a valid quantifier."

    _, predicate = extract_domain_and_predicate(statement, domain)
    if not predicate:
        return "Unable to extract predicate. Ensure the domain is correctly specified in the statement."

    # Representing predicates as P(x) and Q(x)
    predicate_variable = "P(x)"
    domain_variable = "Q(x)"

    if quantifier_symbol == "∀":
        general_logical_expression = f"{quantifier_symbol} {domain_variable} → {predicate_variable}, where {domain_variable} = '{domain}' and {predicate_variable} = 'x {predicate}'"
    elif quantifier_symbol == "∃":
        general_logical_expression = f"{quantifier_symbol} {domain_variable} ∧ {predicate_variable}, where {domain_variable} = '{domain}' and {predicate_variable} = 'x {predicate}'"


    return general_logical_expression

def print_menu():
    """
    Displays a menu with options for translating statements to different types of logic.
    """
    print("\n=== Binary Brain Quantified Statement Translator ===")
    print("1. Translate to domain-specific logic")
    print("2. Translate to general logic")
    print("3. Exit")


def handle_choice(choice, statement, domain):
    """
    Handles the user's choice and performs the corresponding action.

    Parameters:
    choice (str): The user's choice, which determines the action to be taken.
    statement (str): The logical statement to be processed.
    domain (str): The domain to be used for processing the logical statement.

    Returns:
    None
    """
    if choice == '1':
        print("\nDomain Specific Solution")
        print(f"Domain: {domain}")
        print(f"Logical Expression: {translate_to_logic(statement, domain)}")
    elif choice == '2':
        print("\nGeneral Solution")
        print(f"Logical Expression: {translate_to_general_logic(statement, domain)}")
    elif choice == '3':
        print("Exiting... Goodbye!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    parser = argparse.ArgumentParser(description="Binary Brain Quantified Statement Translator")
    parser.add_argument('-s', '--statement', type=str, help='Quantified statement to translate')
    parser.add_argument('-d', '--domain', type=str, help='Domain of the statement')
    args = parser.parse_args()

    if args.statement and args.domain:
        print("\nDomain Specific Solution")
        print(f"Domain: {args.domain}")
        print(f"Logical Expression: {translate_to_logic(args.statement, args.domain)}")
        print("\nGeneral Solution")
        print(f"Logical Expression: {translate_to_general_logic(args.statement, args.domain)}")
    else:
        while True:
            print_menu()
            choice = input("Enter your choice: ").strip()
            statement = input("Enter a quantified statement: ").strip()
            domain = input("Enter the domain of the statement: ").strip()
            if statement and domain:
                handle_choice(choice, statement, domain)
            else:
                print("Statement and domain cannot be empty. Please try again.")

if __name__ == "__main__":
    main()