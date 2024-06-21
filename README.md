📚 Section 1: Imports and Libraries
import os: This line imports the os module, which provides operating system functionality, such as file and directory manipulation, and environment variable access.
import fitz # PyMuPDF: Here, we're importing the fitz module (also known as PyMuPDF). It's used for working with PDF files, allowing you to read, write, and manipulate PDF content.
import re: This statement imports the re module, which is used for working with regular expressions. Regular expressions are patterns for searching and replacing text within strings.
import tkinter as tk: Here, we're importing the tkinter module and renaming it as tk. tkinter is a graphical library for creating graphical user interfaces (GUIs) in Python.
from tkinter import filedialog, messagebox: This line imports the filedialog and messagebox functions from the tkinter module. filedialog allows the user to select files or directories through dialog boxes, while messagebox displays warning, informational, or error messages in dialog boxes.
from tkinter.scrolledtext import ScrolledText: Here, we're importing the ScrolledText class from the tkinter module. This class creates a text area with scrollbars, useful for displaying and editing long text in a GUI.
📑 Section 2: PDF Text Extraction Function
The extract_text_from_pdf function is responsible for extracting text from a PDF file.
def extract_text_from_pdf(pdf_path): Defines the function, which takes the path to the PDF file (pdf_path) as an argument.
text = "": Initializes a text variable as an empty string, which will store the extracted text from the PDF.
try:: Begins a try block to handle potential exceptions during PDF file reading.
document = fitz.open(pdf_path): Opens the PDF file using the fitz.open function and stores the document object in the document variable.
for page_num in range(len(document)): Iterates over each page in the PDF document, using the range function to generate a sequence of numbers corresponding to the page indices.
page = document.load_page(page_num): Loads the current page of the document into the page variable.
text += page.get_text("text"): Extracts the text from the current page using the page.get_text("text") function and appends the text to the text variable.
except Exception as e:: except block to catch any exception that occurs within the try block.
print(f"Error reading {pdf_path}: {e}"): Prints an error message to the console indicating the PDF file path and the exception that occurred.
return text: Returns the extracted text from the PDF file.
🔎 Section 3: Keyword Search Function
The find_paragraphs_with_keyword function searches for paragraphs within a text that contain a specific keyword.
def find_paragraphs_with_keyword(text, keyword): Defines the function, which takes the text and the keyword as arguments.
paragraphs = re.split(r'\n\s*\n', text.strip()): Splits the text into paragraphs using a regular expression. The regular expression r'\n\s*\n' finds a newline followed by zero or more whitespace characters and another newline, which typically separates paragraphs.
matching_paragraphs = [para for para in paragraphs if keyword.lower() in para.lower()]: Creates a matching_paragraphs list containing all the paragraphs that contain the keyword, converting both the keyword and paragraphs to lowercase for comparison.
return matching_paragraphs: Returns the list of matching paragraphs.
🗃️ Section 4: Main Search Function
The search_keyword_in_pdfs function is the main function for searching for a keyword in multiple PDF files.
def search_keyword_in_pdfs(directory, keyword): Defines the function, which takes the directory containing the PDF files and the keyword as arguments.
results = {}: Initializes a results dictionary to store the search results.
for filename in os.listdir(directory): Iterates over the files in the specified directory.
if filename.endswith('.pdf'): Checks if the current file is a PDF file.
pdf_path = os.path.join(directory, filename): Constructs the full path to the PDF file.
text = extract_text_from_pdf(pdf_path): Extracts the text from the PDF file using the extract_text_from_pdf function.
matching_paragraphs = find_paragraphs_with_keyword(text, keyword): Searches for paragraphs containing the keyword in the extracted text.
if matching_paragraphs: If there are matching paragraphs, adds the PDF filename and the list of matching paragraphs to the results dictionary.
return results: Returns the results dictionary with the search results.
🖥️ Section 5: GUI Class Definition
The PDFSearchApp class defines the GUI (Graphical User Interface) application for the keyword search in PDFs.
class PDFSearchApp(tk.Tk): Defines the class, which inherits from the tk.Tk class (the main class in tkinter).
def __init__(self): Constructor method of the class, which is called when a new instance of the class is created.
super().__init__(): Calls the constructor of the parent class tk.Tk to initialize the main window of the application.
self.title("PDF Keyword Search"): Sets the title of the application window.
self.geometry("800x600"): Sets the dimensions of the application window (width x height).
self.label1 = tk.Label(self, text="PDF Directory:"): Creates a label (tk.Label) to indicate the input field for the PDF directory.
self.label1.pack(pady=5): Arranges the label in the window using the pack layout manager, adding vertical spacing (pady).
self.entry1 = tk.Entry(self, width=70): Creates an entry box (tk.Entry) for the user to enter the PDF directory path.
self.entry1.pack(pady=5): Arranges the entry box in the window, adding vertical spacing.
self.button1 = tk.Button(self, text="Browse", command=self.browse_directory): Creates a button (tk.Button) for the user to browse and select the PDF directory, associating the browse_directory function with the button click event.
self.button1.pack(pady=5): Arranges the button in the window, adding vertical spacing.
self.label2 = tk.Label(self, text="Keyword:"): Creates a label to indicate the input field for the keyword.
self.label2.pack(pady=5): Arranges the label in the window.
self.entry2 = tk.Entry(self, width=70): Creates an entry box for the user to enter the keyword.
self.entry2.pack(pady=5): Arranges the entry box in the window.
self.label3 = tk.Label(self, text="Save Results Directory (Optional):"): Creates a label to indicate the input field for the optional directory to save the results.
self.label3.pack(pady=5): Arranges the label in the window.
self.entry3 = tk.Entry(self, width=70): Creates an entry box for the user to enter the path to the results save directory (optional).
self.entry3.pack(pady=5): Arranges the entry box in the window.
self.button3 = tk.Button(self, text="Browse", command=self.browse_save_directory): Creates a button to browse and select the results save directory, associating the browse_save_directory function with the click event.
self.button3.pack(pady=5): Arranges the button in the window.
self.button2 = tk.Button(self, text="Search", command=self.search): Creates a button to start the search, associating the search function with the click event.
self.button2.pack(pady=5): Arranges the button in the window.
self.text = ScrolledText(self, wrap=tk.WORD): Creates a text area (ScrolledText) with scrollbars to display the search results.
self.text.pack(pady=5, fill=tk.BOTH, expand=True): Arranges the text area in the window, filling all the available space.
📁 Section 6: GUI Helper Functions
The browse_directory and browse_save_directory functions are helper functions for the GUI to allow the user to browse and select directories.
def browse_directory(self): Function called when the "Browse" button for the PDF directory is clicked.
directory = filedialog.askdirectory(): Opens a directory selection dialog box (filedialog.askdirectory()) and stores the path of the selected directory in the directory variable.
if directory:: Checks if the user selected a directory.
self.entry1.delete(0, tk.END): Clears the content of the PDF directory entry box.
self.entry1.insert(0, directory): Inserts the path of the selected directory into the entry box.
def browse_save_directory(self): Function called when the "Browse" button for the results save directory is clicked.
directory = filedialog.askdirectory(): Opens a directory selection dialog box.
if directory:: Checks if the user selected a directory.
self.entry3.delete(0, tk.END): Clears the content of the results save directory entry box.
self.entry3.insert(0, directory): Inserts the path of the selected directory into the entry box.
🔍 Section 7: Search Execution
The search function is the main function that performs the keyword search on the PDF files and displays the results.
7.1 Input Validation
def search(self): Defines the function.
pdf_directory = self.entry1.get().strip(), search_keyword = self.entry2.get().strip(), save_directory = self.entry3.get().strip(): Retrieves the values from the entry boxes and removes whitespace.
if not pdf_directory or not search_keyword:: Checks if the user provided the PDF directory and the keyword.
messagebox.showwarning("Input Error", "Please provide both directory and keyword."): Displays a warning message if either field is empty.
return: Exits the function.
if not os.path.isdir(pdf_directory): Checks if the provided PDF directory exists.
messagebox.showerror("Directory Error", "The specified PDF directory does not exist."): Displays an error message if the directory does not exist.
return: Exits the function.
7.2 PDF File Check
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]: Creates a pdf_files list containing the names of the PDF files in the specified directory.
if not pdf_files: Checks if any PDF files were found in the directory.
messagebox.showerror("Directory Error", "No PDF files found in the specified directory."): Displays an error message if no PDF files are found.
return: Exits the function.
7.3 Keyword Search and Results Display
results = search_keyword_in_pdfs(pdf_directory, search_keyword): Calls the search_keyword_in_pdfs function to perform the keyword search on the PDF files.
self.text.delete(1.0, tk.END): Clears the content of the results text area.
for pdf, paragraphs in results.items(): Iterates over the search results, accessing the PDF filename and the list of matching paragraphs.
self.text.insert(tk.END, f"\nPDF: {pdf}\n", "pdf"): Inserts the PDF filename into the text area, applying the "pdf" tag to highlight the filename.
for para in paragraphs: Iterates over the matching paragraphs.
start_idx = self.text.index(tk.END): Gets the current index of the end of the text area.
self.text.insert(tk.END, f"\n{para}\n"): Inserts the current paragraph into the text area.
end_idx = self.text.index(tk.END): Gets the current index of the end of the text area after inserting the paragraph.
self.highlight_keyword(start_idx, end_idx, search_keyword): Calls the highlight_keyword function to highlight the keyword in the paragraph.
self.text.tag_config("pdf", background="yellow", foreground="black"): Sets the configuration of the "pdf" tag to highlight filenames in yellow with black text.
self.text.tag_config("highlight", background="lightgreen", foreground="black"): Sets the configuration of the "highlight" tag to highlight keywords in light green with black text.
7.4 Optional Results Saving
if save_directory: Checks if the user provided a directory to save the results.
if not os.path.isdir(save_directory): Checks if the results save directory exists.
messagebox.showerror("Save Directory Error", "The specified save directory does not exist."): Displays an error message if the directory does not exist.
return: Exits the function.
save_path = os.path.join(save_directory, 'search_results.txt'): Constructs the full path to the results file.
try:: Begins a try block to handle potential exceptions during writing to the file.
with open(save_path, 'w') as f:: Opens the results file for writing ('w').
for pdf, paragraphs in results.items(): Iterates over the search results.
f.write(f"\nPDF: {pdf}\n"): Writes the PDF filename to the results file.
for para in paragraphs: Iterates over the matching paragraphs.
f.write(f"\n{para}\n"): Writes the current paragraph to the results file.
messagebox.showinfo("Save Results", f"Results saved to {save_path}"): Displays an informational message indicating that the results have been saved.
except Exception as e:: except block to catch any exception that occurs during writing to the file.
messagebox.showerror("Save Error", f"An error occurred while saving the file: {e}"): Displays an error message if any problem occurs during saving.
🖍️ Section 8: Keyword Highlighting Function
The highlight_keyword function highlights the keywords found in the text.
def highlight_keyword(self, start_idx, end_idx, keyword): Defines the function, which takes the starting index, the ending index, and the keyword as arguments.
text = self.text.get(start_idx, end_idx): Gets the text from the text area between the provided indices.
start = text.lower().find(keyword.lower()): Searches for the first occurrence of the keyword in the text, converting both to lowercase for comparison.
while start != -1: Iterates while occurrences of the keyword are found.
start_pos = f"{start_idx}+{start}c": Calculates the starting position of the keyword in the text area.
end_pos = f"{start_pos}+{len(keyword)}c": Calculates the ending position of the keyword.
self.text.tag_add("highlight", start_pos, end_pos): Adds the "highlight" tag to the text between the starting and ending positions, highlighting the keyword.
start = text.lower().find(keyword.lower(), start + len(keyword)): Searches for the next occurrence of the keyword, starting from the position after the last found occurrence.
🏁 Section 9: Application Execution
if __name__ == "__main__":: Checks if the script is being run as a main program.
app = PDFSearchApp(): Creates an instance of the PDFSearchApp class.
app.mainloop(): Starts the main loop of the GUI application, which processes interface events and keeps the window open until the user closes it.
