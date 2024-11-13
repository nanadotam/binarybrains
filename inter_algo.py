import argparse

"""
Changes to be made:
- Add a menu interface (e.g. Press 1. to do something, Press 2. to do something else)
- Translate the statement from not to "not all students" to "∃ P(x) where P(x) = 'not all students'"
e.g. "none of the students like school" = "∃ P(x) where P(x) = 'none of the students like school" = "all students do not like school" 
"""



def identify_quantifier(statement):
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
    if domain in statement:
        parts = statement.split(domain)
        quantifier = parts[0].strip()
        predicate = parts[1].strip()
        return quantifier, predicate
    else:
        return None, None

def translate_to_logic(statement, domain):
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

def main():
    print("Welcome to the Binary Brain Quantified Statement Translator!")
    def menu():
        print("Menu:")
        print("1. Translate to domain-specific logic")
        print("2. Translate to general logic")
        print("3. Exit")

    def handle_choice(choice, statement, domain):
        if choice == '1':
            print("\nDomain Specific Solution")
            print(f"Domain: {domain}")
            domain_specific_translation = translate_to_logic(statement, domain)
            print(f"Logical Expression: {domain_specific_translation}")
        elif choice == '2':
            print("\nGeneral Solution")
            general_translation = translate_to_general_logic(statement, domain)
            print(f"Logical Expression: {general_translation}")
        elif choice == '3':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

    parser = argparse.ArgumentParser(description="Binary Brain Quantified Statement Translator")
    parser.add_argument('-s', '--statement', type=str, help='Quantified statement to translate')
    parser.add_argument('-d', '--domain', type=str, help='Domain of the statement')
    args = parser.parse_args()

    if args.statement and args.domain:
        statement = args.statement
        domain = args.domain
        print("\nDomain Specific Solution")
        print("*" * 50)
        print(f"Domain: {domain}")
        domain_specific_translation = translate_to_logic(statement, domain)
        print(f"Logical Expression: {domain_specific_translation}")

        print("\nGeneral Solution")
        print("*" * 50)
        general_translation = translate_to_general_logic(statement, domain)
        print(f"Logical Expression: {general_translation}")
    else:
        while True:
            menu()
            choice = input("Enter your choice: ")
            statement = input("Enter a quantified statement: ")
            domain = input("Enter the domain of the statement: ")
            handle_choice(choice, statement, domain)


    LOGICAL_OPERATORS = {
        "and": "∧",
        "or": "∨",
        "not": "¬",
        "some": "∃",
        "all": "∀",
        "implies": "→"
    }

    # different ways of expressing implication (→)
    # "q unless p" is equivalent to "p → q"
    # "q if p" is equivalent to "p → q"
    # "p only if q" is equivalent to "p → q"
    # "p implies q" is equivalent to "p → q"
    # "if p then q" is equivalent to "p → q"
    # "p is sufficient for q" is equivalent to "p → q"
    # "q is necessary for p" is equivalent to "p → q"
    # "p is a sufficient condition for q" is equivalent to "p → q"
    # "q is a necessary condition for p" is equivalent to "p → q"



if __name__ == "__main__":
    main()
