# binarybrains
Discrete Project


```
#Working on quantified statements
#since a key can have multiple values and can have different logical operators, we will create the list for and
logical_operators=  {"∧": ["and", "but"], "∨":"or", "¬": "not",} 

#doing the same for quantifiers
existential_quantifier=  "∃"
universal_quantifier= "∀"
quantifiers= { "∃":["some", "any"], "∀":["all","every"]}

#creating our domains: students in the class & all people
initial_domain= "Students in the class"
general_domain= "All people"

#allowing user to input their statement using .lower() to make it case insensitive
user_input= input('Enter any quantified statement: ').lower()

#function to check quantified statements using for loops, returning the symbols and alerting user to enter quantified  statement
def quantified_statement(user_input):
    for quantifier,translators in quantifiers.items():
        for x in translators:
            if quantifier in user_input:
                return quantifier
    else:
        return "Invalid input, no quantified statement detected"

#function to work on predicates 
def predicates(user_input):
    

```
