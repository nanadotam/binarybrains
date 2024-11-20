import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from main_simplified import translate_statement, validate_statement
import sys

class QuantifierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantified Statement Translator")
        self.root.geometry("800x600")
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('Error.TLabel', foreground='red')
        
        # Add menu bar
        self.create_menu()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title = ttk.Label(
            self.root, 
            text="Quantified Statement Translator",
            style='Title.TLabel'
        )
        title.pack(pady=20)
        
        # Input frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(fill='x', padx=20)
        
        # Input label
        input_label = ttk.Label(
            input_frame,
            text="Enter a quantified statement:",
            style='Header.TLabel'
        )
        input_label.pack(anchor='w')
        
        # Input entry
        self.input_entry = ttk.Entry(input_frame, width=60)
        self.input_entry.pack(fill='x', pady=5)
        self.input_entry.bind('<Return>', lambda e: self.translate())
        
        # Translate button
        translate_button = ttk.Button(
            input_frame,
            text="Translate",
            command=self.translate
        )
        translate_button.pack(pady=10)
        
        # Error label
        self.error_label = ttk.Label(
            input_frame,
            text="",
            style='Error.TLabel',
            wraplength=700
        )
        self.error_label.pack()
        
        # Results frame
        results_frame = ttk.Frame(self.root)
        results_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            height=15,
            font=('Courier', 10)
        )
        self.results_text.pack(fill='both', expand=True)
        
        # Example frame
        example_frame = ttk.LabelFrame(
            self.root,
            text="Examples",
            padding=10
        )
        example_frame.pack(fill='x', padx=20, pady=10)
        
        # Example text
        examples = (
            "Examples:\n"
            "- All students like math\n"
            "- Some people are tall\n"
            "- None of the students like homework"
        )
        example_label = ttk.Label(example_frame, text=examples)
        example_label.pack()
        
    def translate(self):
        # Clear previous results and errors
        self.error_label.config(text="")
        self.results_text.delete(1.0, tk.END)
        
        # Get input
        statement = self.input_entry.get().strip()
        
        # Validate input
        is_valid, error_message = validate_statement(statement)
        if not is_valid:
            self.error_label.config(text=error_message)
            return
            
        # Translate statement
        people_result, students_result = translate_statement(statement)
        
        # Check for errors
        if isinstance(people_result, str) and people_result.startswith("Error"):
            self.error_label.config(text=people_result)
            return
            
        # Display results
        results = (
            "Results:\n\n"
            f"Domain: All People\n"
            f"Logical Expression: {people_result}\n\n"
            f"Domain: Students in this class\n"
            f"Logical Expression: {students_result}"
        )
        self.results_text.insert(1.0, results)
        
    def clear(self):
        self.input_entry.delete(0, tk.END)
        self.results_text.delete(1.0, tk.END)
        self.error_label.config(text="")
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear", command=self.clear)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_app)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def quit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.quit()
            sys.exit()
    
    def show_about(self):
        about_text = """
Quantified Statement Translator

This program translates natural language statements 
into logical expressions using predicates and quantifiers.

Version: 1.0
"""
        messagebox.showinfo("About", about_text)

def main():
    root = tk.Tk()
    app = QuantifierGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 