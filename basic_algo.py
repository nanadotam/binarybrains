# pseudocode


# We have our domain
# so we can take user input for what the domain is
# domain = input("Enter the domain of the statement: ")

# We identify our predicate logic

# so we can identify the predicates in the statement by representing them as variables
# variables like P(x), Q(x), R(x), etc.


# Identifying the quantifiers
# so depending on the statement
# it can be "some", "all", "everyone", "at least one", "there is one", "there exists", "someone" etc.

# so in the statement we can identify the quantifier by looking for the words that indicate the quantifier
# so we can loop through the words in the statement and check if the word is in the quantifiers list

# however before we get the quantifier, we can use the domain to separate the statements with a delimiter sort of like a split
# so we can save the domain as a list of words to a variable
# eg: statement:  "All students in the school are happy"
# domain: "students in the school"
# words: ["all", "students", "in", "the", "school", "are", "happy"]

# so now that we have what the domain is as a variable, we can use it to split the statement into half
# that way now we know whatever comes before the domain is the quantifier
# and whatever comes after the domain is the predicate

# so now what comes before the domain in  "All students in the school are happy" is "All" (the quantifier)
# and what comes after the domain is "are happy" (the predicate)
# so we can represent the predicate as a variable too and change it to:
# predicate = "x are happy"
# now the predicate can be represented as a predicate logic variable like P(x), Q(x), R(x), etc.
# so predicate logic var = {P(x): predicate}

# if there is a case where there is more than one predicate, we can represent them as variables too
# e.g: predicate_2 = "x are sad"

# or something like that


# then now we can represent the quantifier as a variable too and change it to:
# quantifier = "∀"


# for the quantifiers, we can represent them using keys and values
# e.g: {"some": "∃", "all": "∀", "everyone": "∀", "at least one": "∃", "there is one": "∃", "there exists": "∃", "someone": "∃", "any": "∃"}
# so we can loop through the words in the statement and check if the word is in the quantifiers list
# if it is, we replace it with the value of the quantifier
# so in the statement "All students in the school are happy"
# the word "All" is in the quantifiers list
# so we replace it with "∀"
# so now the statement is "∀ P(x)"
# since we make "P(x)" = "x are happy"

# the same logic applies to another quantifier like "some"
# e.g: statement: "Some students in the school are happy"
# quantifier = "some"
# quantifier_value = "∃"
# predicate = "x are happy"
# so now the statement is "∃ P(x)"



# so we can take user input for what the predicate logic is
# predicate_logic = input("Enter the predicate logic of the statement: ")



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

def main():
    statement = input("Enter a quantified statement: ")
    domain = input("Enter the domain of the statement: ")
    print("\n### Domain Specific Solution ###")
    print(f"Domain: {domain}")
    domain_specific_translation = translate_to_logic(statement, domain)
    print(f"Logical Expression: {domain_specific_translation}")

    print("\n### General Solution ###")
    general_translation = translate_to_logic(statement, "people")
    print(f"Logical Expression: {general_translation}")

if __name__ == "__main__":
    main()
# Example usage
# statement = "All students in the school are happy"
# domain = "class"
# print(translate_to_logic(statement, domain))