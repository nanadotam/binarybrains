# Binary Brains Quantified Statement Translator

This is a command-line interface (CLI) tool designed to translate quantified statements into logical expressions using predicates, quantifiers, and logical connectives. The tool supports translations for domain-specific and general logical expressions with an easy-to-use menu interface.

---

## Features

- **Translation Capabilities**: Transform quantified natural language statements into logical expressions.
- **Domain-Specific and General Logic**: Translate within a specified domain or generalize to broader logic.
- **Interactive Menu**: User-friendly CLI menu with ASCII art for an engaging experience.
- **Help and Documentation**: Built-in help menu for detailed usage guidance.
- **Error Handling**: Graceful handling of invalid inputs with appropriate messages.

---

## Installation

### Prerequisites

- Python 3.6 or higher

### Cloning the Repository

To get started, clone the repository using the following command:

```bash
git clone https://github.com/nanadotam/binarybrains.git
cd binarybrains
```

---

## Usage

### Running the Program

To run the program, execute the following command:

```bash
python main.py
```

### Main Menu Options

Upon running the program, you will be presented with a main menu. Here are the available options:

1. **Translate to Domain-Specific Logic**  
   Enter a quantified statement (e.g., "All students love math") and specify a domain (e.g., "students"). The program will generate a logical expression tailored to the given domain.

2. **Translate to General Logic**  
   Similar to option 1, but the translation applies to a broader domain without focusing on a specific group.

3. **Help**  
   Displays a comprehensive help guide with usage instructions and examples.

4. **Exit**  
   Exits the program gracefully.

### Example Usage

**Example Input:**

```
Enter your choice: 1
Enter a quantified statement: Some students love ice cream
Enter the domain of the statement: students
```

**Example Output (Domain-Specific):**

```
Domain Specific Solution
Domain: students
Logical Expression: ∃ P(x) where P(x) = 'x love ice cream'
```

**Example Output (General Logic):**

```
General Solution
Logical Expression: ∃ Q(x) ∧ P(x), where Q(x) = 'students' and P(x) = 'x love ice cream'
```

---

## Program Flow

1. **Startup**: Displays a welcome banner with the main menu.
2. **User Selection**: User selects an option from the main menu (e.g., translating logic, accessing help, etc.).
3. **Translation Process**: Based on user input, the tool translates the quantified statement.
4. **Prompt for Next Steps**: After completing a translation, users are prompted with:
   ```
   Enter '1' to return to the main menu, '2' to exit.
   ```
5. **Return or Exit**: Users can return to the main menu or exit the program based on their input.

---

## Requirements

- **Python 3.6 or higher**
- No external dependencies required as of now.
---

## Help Menu

The built-in help menu provides the following:

- Descriptions and examples of each main menu option.
- Instructions on entering quantified statements and specifying domains.

