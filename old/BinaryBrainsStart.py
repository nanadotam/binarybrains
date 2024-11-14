# Working on quantified statements
# since a key can have multiple values and can have different logical operators, we will create the list for and
logical_operators = {"∧": ["and", "but"], "∨": "or", "¬": "not"}

# doing the same for quantifiers
existential_quantifier = "∃"
universal_quantifier = "∀"
quantifiers = {"∃": ["some", "any"], "∀": ["all", "every"]}

# creating our domains: students in the class & all people
initial_domain = "Students in the class"
general_domain = "All people"

# allowing user to input their statement using .lower() to make it case insensitive
user_input = input('Enter any quantified statement: ').lower()

# function to check quantified statements using for loops, returning the symbols and alerting user to enter quantified statement
def quantified_statement(user_input):
    for quantifier, translators in quantifiers.items():
        for x in translators:
            if x in user_input:
                return quantifier
    return "Invalid input, no quantified statement detected"

# function to extract predicates from the user input
def predicates(user_input):
    predicates_list = []
    words = user_input.split()
    for word in words:
        if word not in quantifiers and word not in logical_operators:
            predicates_list.append(word)
    return predicates_list

# Main function to convert English statements into predicates and quantifiers
def convert_to_predicates_and_quantifiers(user_input):
    quantifier = quantified_statement(user_input)
    if quantifier == "Invalid input, no quantified statement detected":
        return quantifier
    else:
        predicate_list = predicates(user_input)
        return f"{quantifier} {', '.join(predicate_list)}"

# Example usage
result = convert_to_predicates_and_quantifiers(user_input)
print(result)