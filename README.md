# Quantified Statement Translator

This is a command-line interface (CLI) tool for translating quantified statements into logical expressions using predicates, quantifiers, and logical connectives. The program supports translations for domain-specific and general logic expressions.

## Features

- Translate quantified statements with user-defined domains.
- User-friendly menu interface with ASCII art banners.
- Help menu with detailed usage instructions.
- Graceful handling of input errors.

## Usage

Run the program using Python:

```bash
python main.py

Main Menu Options

	1.	Translate to Domain-Specific Logic
Enter a quantified statement (e.g., “All students love math”) and a domain (e.g., “students”). The program will generate a logical expression for the given statement within the specified domain.
	2.	Translate to General Logic
Similar to option 1, but translates the input into a general logical form that works over a broader domain.
	3.	Help
Displays a detailed guide on how to use the program.
	4.	Exit
Exits the program.

Example Input/Output

Example Statement:

"Some students love ice cream"

Example Domain:

"students"

Output (Domain-Specific):

Example translation of 'Some students love ice cream' for domain 'students'.

Output (General Logic):

General translation of 'Some students love ice cream' for domain 'students'.

Requirements

	•	Python 3.6 or higher

Future Enhancements

	•	Support for more complex predicates and quantifiers.
	•	Addition of natural language processing capabilities for better input handling.

Explanation

	•	The README.md provides a comprehensive overview of your project, including usage instructions, examples, and requirements.
	•	The requirements.txt is minimal since there are no external dependencies currently needed. If you add external libraries in the future, you can list them here (e.g., colorama if you reintroduce it).