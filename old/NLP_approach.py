# predicates_and_quantifiers_general.py

# Reserved keywords dictionary for logical operators
LOGICAL_OPERATORS = {
    "and": "∧",
    "or": "∨",
    "not": "¬",
    "some": "∃",
    "all": "∀"
}

def get_user_statement():
    """
    Prompts the user to enter a quantified statement.
    """
    print("Enter a quantified statement (e.g., 'All students in this class love football'):")
    statement = input("> ")
    return statement

def parse_statement(statement):
    """
    Parses the statement by identifying quantifiers, logical operators, subjects, and predicates.
    For now, this uses a simple string search approach, but it can be expanded with NLP.
    """
    words = statement.lower().split()
    parsed_tokens = []
    for word in words:
        if word in LOGICAL_OPERATORS:
            parsed_tokens.append((word, LOGICAL_OPERATORS[word]))
        else:
            parsed_tokens.append((word, None))
    
    # Example parsing output (placeholder): 
    # Identify quantifiers, subjects, predicates, etc.
    quantifier = None
    subject = None
    predicate = None
    
    # Simplified parsing logic to identify components (expandable)
    if "all" in words:
        quantifier = "all"
        subject_index = words.index("all") + 1
        subject = words[subject_index] if subject_index < len(words) else "unknown subject"
        predicate = " ".join(words[subject_index+1:])

    elif "some" in words:
        quantifier = "some"
        subject_index = words.index("some") + 1
        subject = words[subject_index] if subject_index < len(words) else "unknown subject"
        predicate = " ".join(words[subject_index+1:])

    return {
        "quantifier": quantifier,
        "subject": subject,
        "predicate": predicate,
        "tokens": parsed_tokens
    }

def translate_to_logical_expression(parsed_statement):
    """
    Translates the parsed statement into a logical expression.
    """
    quantifier = parsed_statement["quantifier"]
    subject = parsed_statement["subject"]
    predicate = parsed_statement["predicate"]

    if quantifier == "all":
        return f"∀x (Student(x) → ({predicate}))"
    elif quantifier == "some":
        return f"∃x (Student(x) ∧ ({predicate}))"
    else:
        return "Unknown logical form"

def main():
    example_statement = "Some students in this class are from Australia"
    print(f"Example Input: {example_statement}")
    
    # Parsing example statement
    parsed_example = parse_statement(example_statement)
    print(f"Parsed Output: {parsed_example}")
    
    # Translating to logical expression
    logical_expression = translate_to_logical_expression(parsed_example)
    print(f"Logical Expression: {logical_expression}")

    # User input loop
    while True:
        statement = get_user_statement()
        if statement.lower() in ["exit", "quit"]:
            print("Exiting program.")
            break
        parsed_statement = parse_statement(statement)
        logical_expression = translate_to_logical_expression(parsed_statement)
        
        print("\nLogical Expressions:")
        print(f"Parsed Output: {parsed_statement}")
        print(f"Logical Expression: {logical_expression}\n")

if __name__ == "__main__":
    main()
