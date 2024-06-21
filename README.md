### 📚 Section 1: Imports and Libraries 

1. **`import os`**: This line imports the `os` module, which provides operating system functionality, such as file and directory manipulation, and environment variable access.

2. **`import fitz  # PyMuPDF`**: Here, we're importing the `fitz` module (also known as PyMuPDF). It's used for working with PDF files, allowing you to read, write, and manipulate PDF content.

3. **`import re`**: This statement imports the `re` module, which is used for working with regular expressions. Regular expressions are patterns for searching and replacing text within strings.

4. **`import tkinter as tk`**: Here, we're importing the `tkinter` module and renaming it as `tk`. `tkinter` is a graphical library for creating graphical user interfaces (GUIs) in Python.

5. **`from tkinter import filedialog, messagebox`**: This line imports the `filedialog` and `messagebox` functions from the `tkinter` module. `filedialog` allows the user to select files or directories through dialog boxes, while `messagebox` displays warning, informational, or error messages in dialog boxes.

6. **`from tkinter.scrolledtext import ScrolledText`**: Here, we're importing the `ScrolledText` class from the `tkinter` module. This class creates a text area with scrollbars, useful for displaying and editing long text in a GUI.


### 📑 Section 2: PDF Text Extraction Function

The `extract_text_from_pdf` function is responsible for extracting text from a PDF file.

1. **`def extract_text_from_pdf(pdf_path)`**: Defines the function, which takes the path to the PDF file (`pdf_path`) as an argument.

2. **`text = ""`**: Initializes a `text` variable as an empty string, which will store the extracted text from the PDF.

3. **`try:`**: Begins a `try` block to handle potential exceptions during PDF file reading.

4. **`document = fitz.open(pdf_path)`**: Opens the PDF file using the `fitz.open` function and stores the document object in the `document` variable.

5. **`for page_num in range(len(document))`**: Iterates over each page in the PDF document, using the `range` function to generate a sequence of numbers corresponding to the page indices.

6. **`page = document.load_page(page_num)`**: Loads the current page of the document into the `page` variable.

7. **`text += page.get_text("text")`**: Extracts the text from the current page using the `page.get_text("text")` function and appends the text to the `text` variable.

8. **`except Exception as e:`**: `except` block to catch any exception that occurs within the `try` block.

9. **`print(f"Error reading {pdf_path}: {e}")`**: Prints an error message to the console indicating the PDF file path and the exception that occurred.

10. **`return text`**: Returns the extracted text from the PDF file.

### 🔎 Section 3: Keyword Search Function

The `find_paragraphs_with_keyword` function searches for paragraphs within a text that contain a specific keyword.

1. **`def find_paragraphs_with_keyword(text, keyword)`**: Defines the function, which takes the text and the keyword as arguments.

2. **`paragraphs = re.split(r'\n\s*\n', text.strip())`**: Splits the text into paragraphs using a regular expression. The regular expression `r'\n\s*\n'` finds a newline followed by zero or more whitespace characters and another newline, which typically separates paragraphs.

3. **`matching_paragraphs = [para for para in paragraphs if keyword.lower() in para.lower()]`**: Creates a `matching_paragraphs` list containing all the paragraphs that contain the keyword, converting both the keyword and paragraphs to lowercase for comparison.

4. **`return matching_paragraphs`**: Returns the list of matching paragraphs.

### 🗃️ Section 4: Main Search Function

The `search_keyword_in_pdfs` function is the main function for searching for a keyword in multiple PDF files.

1. **`def search_keyword_in_pdfs(directory, keyword)`**: Defines the function, which takes the directory containing the PDF files and the keyword as arguments.

2. **`results = {}`**: Initializes a `results` dictionary to store the search results.

3. **`for filename in os.listdir(directory)`**: Iterates over the files in the specified directory.

4. **`if filename.endswith('.pdf')`**: Checks if the current file is a PDF file.

5. **`pdf_path = os.path.join(directory, filename)`**: Constructs the full path to the PDF file.

6. **`text = extract_text_from_pdf(pdf_path)`**: Extracts the text from the PDF file using the `extract_text_from_pdf` function.

7. **`matching_paragraphs = find_paragraphs_with_keyword(text, keyword)`**: Searches for paragraphs containing the keyword in the extracted text.

8. **`if matching_paragraphs`**: If there are matching paragraphs, adds the PDF filename and the list of matching paragraphs to the `results` dictionary.

9. **`return results`**: Returns the `results` dictionary with the search results.


### 🖥️ Section 5: GUI Class Definition

The `PDFSearchApp` class defines the GUI (Graphical User Interface) application for the keyword search in PDFs.

1. **`class PDFSearchApp(tk.Tk)`**: Defines the class, which inherits from the `tk.Tk` class (the main class in `tkinter`).

2. **`def __init__(self)`**: Constructor method of the class, which is called when a new instance of the class is created.

3. **`super().__init__()`**: Calls the constructor of the parent class `tk.Tk` to initialize the main window of the application.

4. **`self.title("PDF Keyword Search")`**: Sets the title of the application window.

5. **`self.geometry("800x600")`**: Sets the dimensions of the application window (width x height).

6. **`self.label1 = tk.Label(self, text="PDF Directory:")`**: Creates a label (`tk.Label`) to indicate the input field for the PDF directory.

7. **`self.label1.pack(pady=5)`**: Arranges the label in the window using the `pack` layout manager, adding vertical spacing (`pady`).

8. **`self.entry1 = tk.Entry(self, width=70)`**: Creates an entry box (`tk.Entry`) for the user to enter the PDF directory path.

9. **`self.entry1.pack(pady=5)`**: Arranges the entry box in the window, adding vertical spacing.

10. **`self.button1 = tk.Button(self, text="Browse", command=self.browse_directory)`**: Creates a button (`tk.Button`) for the user to browse and select the PDF directory, associating the `browse_directory` function with the button click event.

11. **`self.button1.pack(pady=5)`**: Arranges the button in the window, adding vertical spacing.

12. **`self.label2 = tk.Label(self, text="Keyword:")`**: Creates a label to indicate the input field for the keyword.

13. **`self.label2.pack(pady=5)`**: Arranges the label in the window.

14. **`self.entry2 = tk.Entry(self, width=70)`**: Creates an entry box for the user to enter the keyword.

15. **`self.entry2.pack(pady=5)`**: Arranges the entry box in the window.

16. **`self.label3 = tk.Label(self, text="Save Results Directory (Optional):")`**: Creates a label to indicate the input field for the optional directory to save the results.

17. **`self.label3.pack(pady=5)`**: Arranges the label in the window.

18. **`self.entry3 = tk.Entry(self, width=70)`**: Creates an entry box for the user to enter the path to the results save directory (optional).

19. **`self.entry3.pack(pady=5)`**: Arranges the entry box in the window.

20. **`self.button3 = tk.Button(self, text="Browse", command=self.browse_save_directory)`**: Creates a button to browse and select the results save directory, associating the `browse_save_directory` function with the click event.

21. **`self.button3.pack(pady=5)`**: Arranges the button in the window.

22. **`self.button2 = tk.Button(self, text="Search", command=self.search)`**: Creates a button to start the search, associating the `search` function with the click event.

23. **`self.button2.pack(pady=5)`**: Arranges the button in the window.

24. **`self.text = ScrolledText(self, wrap=tk.WORD)`**: Creates a text area (`ScrolledText`) with scrollbars to display the search results.

25. **`self.text.pack(pady=5, fill=tk.BOTH, expand=True)`**: Arranges the text area in the window, filling all the available space.


### 📁 Section 6: GUI Helper Functions

The `browse_directory` and `browse_save_directory` functions are helper functions for the GUI to allow the user to browse and select directories.

1. **`def browse_directory(self)`**: Function called when the "Browse" button for the PDF directory is clicked.

2. **`directory = filedialog.askdirectory()`**: Opens a directory selection dialog box (`filedialog.askdirectory()`) and stores the path of the selected directory in the `directory` variable.

3. **`if directory:`**: Checks if the user selected a directory.

4. **`self.entry1.delete(0, tk.END)`**: Clears the content of the PDF directory entry box.

5. **`self.entry1.insert(0, directory)`**: Inserts the path of the selected directory into the entry box.

6. **`def browse_save_directory(self)`**: Function called when the "Browse" button for the results save directory is clicked.

7. **`directory = filedialog.askdirectory()`**: Opens a directory selection dialog box.

8. **`if directory:`**: Checks if the user selected a directory.

9. **`self.entry3.delete(0, tk.END)`**: Clears the content of the results save directory entry box.

10. **`self.entry3.insert(0, directory)`**: Inserts the path of the selected directory into the entry box.

### 🔍 Section 7: Search Execution

The `search` function is the main function that performs the keyword search on the PDF files and displays the results.

#### 7.1 Input Validation

1. **`def search(self)`**: Defines the function.

2. **`pdf_directory = self.entry1.get().strip()`, `search_keyword = self.entry2.get().strip()`, `save_directory = self.entry3.get().strip()`**: Retrieves the values from the entry boxes and removes whitespace.

3. **`if not pdf_directory or not search_keyword:`**: Checks if the user provided the PDF directory and the keyword.

4. **`messagebox.showwarning("Input Error", "Please provide both directory and keyword.")`**: Displays a warning message if either field is empty.

5. **`return`**: Exits the function.

6. **`if not os.path.isdir(pdf_directory)`**: Checks if the provided PDF directory exists.

7. **`messagebox.showerror("Directory Error", "The specified PDF directory does not exist.")`**: Displays an error message if the directory does not exist.

8. **`return`**: Exits the function.

#### 7.2 PDF File Check

1. **`pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]`**: Creates a `pdf_files` list containing the names of the PDF files in the specified directory.

2. **`if not pdf_files`**: Checks if any PDF files were found in the directory.

3. **`messagebox.showerror("Directory Error", "No PDF files found in the specified directory.")`**: Displays an error message if no PDF files are found.

4. **`return`**: Exits the function.

#### 7.3 Keyword Search and Results Display

1. **`results = search_keyword_in_pdfs(pdf_directory, search_keyword)`**: Calls the `search_keyword_in_pdfs` function to perform the keyword search on the PDF files.

2. **`self.text.delete(1.0, tk.END)`**: Clears the content of the results text area.

3. **`for pdf, paragraphs in results.items()`**: Iterates over the search results, accessing the PDF filename and the list of matching paragraphs.

4. **`self.text.insert(tk.END, f"\nPDF: {pdf}\n", "pdf")`**: Inserts the PDF filename into the text area, applying the "pdf" tag to highlight the filename.

5. **`for para in paragraphs`**: Iterates over the matching paragraphs.

6. **`start_idx = self.text.index(tk.END)`**: Gets the current index of the end of the text area.

7. **`self.text.insert(tk.END, f"\n{para}\n")`**: Inserts the current paragraph into the text area.

8. **`end_idx = self.text.index(tk.END)`**: Gets the current index of the end of the text area after inserting the paragraph.

9. **`self.highlight_keyword(start_idx, end_idx, search_keyword)`**: Calls the `highlight_keyword` function to highlight the keyword in the paragraph.

10. **`self.text.tag_config("pdf", background="yellow", foreground="black")`**: Sets the configuration of the "pdf" tag to highlight filenames in yellow with black text.

11. **`self.text.tag_config("highlight", background="lightgreen", foreground="black")`**: Sets the configuration of the "highlight" tag to highlight keywords in light green with black text.

#### 7.4 Optional Results Saving

1. **`if save_directory`**: Checks if the user provided a directory to save the results.

2. **`if not os.path.isdir(save_directory)`**: Checks if the results save directory exists.

3. **`messagebox.showerror("Save Directory Error", "The specified save directory does not exist.")`**: Displays an error message if the directory does not exist.

4. **`return`**: Exits the function.

5. **`save_path = os.path.join(save_directory, 'search_results.txt')`**: Constructs the full path to the results file.

6. **`try:`**: Begins a `try` block to handle potential exceptions during writing to the file.

7. **`with open(save_path, 'w') as f:`**: Opens the results file for writing (`'w'`).

8. **`for pdf, paragraphs in results.items()`**: Iterates over the search results.

9. **`f.write(f"\nPDF: {pdf}\n")`**: Writes the PDF filename to the results file.

10. **`for para in paragraphs`**: Iterates over the matching paragraphs.

11. **`f.write(f"\n{para}\n")`**: Writes the current paragraph to the results file.

12. **`messagebox.showinfo("Save Results", f"Results saved to {save_path}")`**: Displays an informational message indicating that the results have been saved.

13. **`except Exception as e:`**: `except` block to catch any exception that occurs during writing to the file.

14. **`messagebox.showerror("Save Error", f"An error occurred while saving the file: {e}")`**: Displays an error message if any problem occurs during saving.

### 🖍️ Section 8: Keyword Highlighting Function

The `highlight_keyword` function highlights the keywords found in the text.

1. **`def highlight_keyword(self, start_idx, end_idx, keyword)`**: Defines the function, which takes the starting index, the ending index, and the keyword as arguments.

2. **`text = self.text.get(start_idx, end_idx)`**: Gets the text from the text area between the provided indices.

3. **`start = text.lower().find(keyword.lower())`**: Searches for the first occurrence of the keyword in the text, converting both to lowercase for comparison.

4. **`while start != -1`**: Iterates while occurrences of the keyword are found.

5. **`start_pos = f"{start_idx}+{start}c"`**: Calculates the starting position of the keyword in the text area.

6. **`end_pos = f"{start_pos}+{len(keyword)}c"`**: Calculates the ending position of the keyword.

7. **`self.text.tag_add("highlight", start_pos, end_pos)`**: Adds the "highlight" tag to the text between the starting and ending positions, highlighting the keyword.

8. **`start = text.lower().find(keyword.lower(), start + len(keyword))`**: Searches for the next occurrence of the keyword, starting from the position after the last found occurrence.


### 🏁 Section 9: Application Execution

1. **`if __name__ == "__main__":`**: Checks if the script is being run as a main program.

2. **`app = PDFSearchApp()`**: Creates an instance of the `PDFSearchApp` class.

3. **`app.mainloop()`**: Starts the main loop of the GUI application, which processes interface events and keeps the window open until the user closes it.
