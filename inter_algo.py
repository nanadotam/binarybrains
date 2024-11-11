"""
Changes to be made:
- Universal uses -> (the implied), existential uses ∧ (and)
- Add a menu interface (e.g. Press 1. to do something, Press 2. to do something else)

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

    general_logical_expression = f"{quantifier_symbol} {domain_variable} ∧ {predicate_variable}, where {domain_variable} = '{domain}' and {predicate_variable} = '{predicate}'"

    return general_logical_expression

def main():
    LOGICAL_OPERATORS = {
        "and": "∧",
        "or": "∨",
        "not": "¬",
        "some": "∃",
        "all": "∀"
    }

    statement = input("Enter a quantified statement: ")
    domain = input("Enter the domain of the statement: ")

    print("\n### Domain Specific Solution ###")
    print(f"Domain: {domain}")
    domain_specific_translation = translate_to_logic(statement, domain)
    print(f"Logical Expression: {domain_specific_translation}")

    print("\n### General Solution ###")
    general_translation = translate_to_general_logic(statement, domain)
    print(f"Logical Expression: {general_translation}")

if __name__ == "__main__":
    main()
