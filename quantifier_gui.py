import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from main_simplified import translate_statement, validate_statement
import sys
import urllib.request
import io

class WelcomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Brains Quantified Statement Translator")
        self.root.geometry("800x600")
        self.root.configure(bg='#E6F3FF')  # Light blue background
        
        # Center frame for welcome content
        welcome_frame = tk.Frame(root, bg='#E6F3FF')
        welcome_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Welcome title
        title = tk.Label(
            welcome_frame,
            text="Welcome to Binary Brains\nQuantified Statement Translator",
            font=('Arial', 36, 'bold'),
            bg='#E6F3FF',
            fg='#2C3E50'  # Dark blue text
        )
        title.pack(pady=20)
        
        # Description
        description = tk.Label(
            welcome_frame,
            text="Transform quantified statements into logical expressions\nwith predicates and quantifiers",
            font=('Arial', 24),
            bg='#E6F3FF',
            fg='#34495E'
        )
        description.pack(pady=10)
        
        # Start button
        start_button = tk.Button(
            welcome_frame,
            text="Start Translating",
            command=self.start_main_app,
            font=('Arial', 12, 'bold'),
            bg='#004080',  # Blue button
            fg='black',
            padx=20,
            pady=10,
            relief='flat'
        )
        start_button.pack(pady=30)
        
    def start_main_app(self):
        self.root.withdraw()  # Hide welcome window
        main_window = tk.Toplevel()
        app = QuantifierGUI(main_window)
        main_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(main_window))
        
    def on_closing(self, main_window):
        self.root.destroy()  # Close both windows
        main_window.destroy()

class QuantifierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Brains Quantified Statement Translator")
        self.root.geometry("800x900")
        self.root.configure(bg='#E6F3FF')  # Light blue background
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('Title.TLabel', font=('Arial', 24, 'bold'), background='#E6F3FF')
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'), background='#E6F3FF')
        self.style.configure('Error.TLabel', foreground='red', background='#E6F3FF')
        self.style.configure('TFrame', background='#E6F3FF')
        self.style.configure('TLabelframe', background='#E6F3FF')
        self.style.configure('TLabelframe.Label', background='#E6F3FF')
        
        # Add menu bar
        self.create_menu()
        
        self.create_widgets()
        
        # Add this near the top of __init__ after other imports
        self.quit_button = tk.Button(
            self.root,
            text="Quit",
            command=self.quit_app,
            bg='#E74C3C',  # Red button
            fg='red',
            font=('Arial', 16, 'bold'),
            relief='flat',
            padx=10,
            pady=5
        )
        self.quit_button.pack(side='bottom', pady=10)
        
    def create_widgets(self):
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Title
        title = ttk.Label(
            main_container, 
            text="Quantified Statement Translator",
            style='Title.TLabel'
        )
        title.pack(pady=20)
        
        # Input frame
        input_frame = ttk.Frame(main_container)
        input_frame.pack(fill='x')
        
        # Input label
        input_label = ttk.Label(
            input_frame,
            text="Enter a quantified statement:",
            style='Header.TLabel'
        )
        input_label.pack(anchor='w')
        
        # Input entry with white background
        self.input_entry = ttk.Entry(input_frame, width=60)
        self.input_entry.pack(fill='x', pady=5)
        self.input_entry.bind('<Return>', lambda e: self.translate())
        
        # Translate button
        translate_button = tk.Button(
            input_frame,
            text="Translate",
            command=self.translate,
            bg='#3498DB',
            fg='black',
            font=('Arial', 24, 'bold'),
            relief='flat',
            padx=20,
            pady=5
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
        
        # Results frame with white background
        results_frame = ttk.Frame(main_container)
        results_frame.pack(fill='both', expand=True, pady=10)
        
        # Results text area with white background
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            height=15,
            font=('Courier', 24),
            bg='white'
        )
        self.results_text.pack(fill='both', expand=True)
        
        # Example frame
        example_frame = ttk.LabelFrame(
            main_container,
            text="Examples",
            padding=10
        )
        example_frame.pack(fill='x', pady=10)
        
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
        # Create a custom dialog
        quit_dialog = tk.Toplevel(self.root)
        quit_dialog.title("Goodbye!")
        quit_dialog.geometry("400x500")
        quit_dialog.configure(bg='#E6F3FF')
        
        # Center the dialog
        quit_dialog.transient(self.root)
        quit_dialog.grab_set()
        
        # Load and display the image
        try:
            # Assuming your image is in the same directory as the script
            image = tk.PhotoImage(file="goodbye_image.png")  # or .gif
            image_label = tk.Label(
                quit_dialog,
                image=image,
                bg='#E6F3FF'
            )
            image_label.image = image  # Keep a reference to prevent garbage collection
            image_label.pack(pady=20)
        except:
            # Fallback to placeholder if image loading fails
            image_placeholder = tk.Label(
                quit_dialog,
                text="[Image Placeholder]",
                width=20,
                height=10,
                bg='white',
                relief='solid'
            )
            image_placeholder.pack(pady=20)
        
        # Thank you message
        thank_you = tk.Label(
            quit_dialog,
            text="Thank you for using\nBinary Brains Translator!",
            font=('Arial', 16, 'bold'),
            bg='#E6F3FF'
        )
        thank_you.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(quit_dialog, bg='#E6F3FF')
        button_frame.pack(pady=20)
        
        # Yes/No buttons
        yes_button = tk.Button(
            button_frame,
            text="Yes, quit",
            command=lambda: self.confirm_quit(quit_dialog),
            bg='#E74C3C',
            fg='red',
            font=('Arial', 12),
            relief='flat',
            padx=20,
            pady=5
        )
        yes_button.pack(side='left', padx=10)
        
        no_button = tk.Button(
            button_frame,
            text="No, stay",
            command=quit_dialog.destroy,
            bg='#2ECC71',
            fg='black',
            font=('Arial', 12),
            relief='flat',
            padx=20,
            pady=5
        )
        no_button.pack(side='left', padx=10)

    def confirm_quit(self, dialog):
        dialog.destroy()
        self.root.quit()
        sys.exit()
    
    def show_about(self):
        about_text = """
Welcome to Binary Brains Quantifier Statement Translator

This program translates quantified statements 
into logical expressions using predicates and quantifiers.

Version: 1.0
"""
        messagebox.showinfo("About", about_text)

def main():
    root = tk.Tk()
    welcome = WelcomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main() 