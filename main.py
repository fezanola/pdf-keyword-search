# --------- Section 1: Imports and Libraries ---------
import os
import fitz  # PyMuPDF
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText


# --------- Section 2: PDF Text Extraction Function ---------
# Extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        document = fitz.open(pdf_path)
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text("text")  # Extract text in a format suitable for processing
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text


# --------- Section 3: Keyword Search Function ---------
# Find paragraphs containing the keyword
def find_paragraphs_with_keyword(text, keyword):
    # Split text into paragraphs by newlines (considering single or double newlines)
    paragraphs = re.split(r'\n\s*\n', text.strip())
    matching_paragraphs = [para for para in paragraphs if keyword.lower() in para.lower()]
    return matching_paragraphs


# --------- Section 4: Main Search Function ---------
# Main function to process multiple PDFs
def search_keyword_in_pdfs(directory, keyword):
    results = {}
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(pdf_path)
            matching_paragraphs = find_paragraphs_with_keyword(text, keyword)
            if matching_paragraphs:
                results[filename] = matching_paragraphs
    return results


# --------- Section 5: GUI Class Definition ---------
# GUI application
class PDFSearchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Keyword Search")
        self.geometry("800x600")

        self.label1 = tk.Label(self, text="PDF Directory:")
        self.label1.pack(pady=5)

        self.entry1 = tk.Entry(self, width=70)
        self.entry1.pack(pady=5)

        self.button1 = tk.Button(self, text="Browse", command=self.browse_directory)
        self.button1.pack(pady=5)

        self.label2 = tk.Label(self, text="Keyword:")
        self.label2.pack(pady=5)

        self.entry2 = tk.Entry(self, width=70)
        self.entry2.pack(pady=5)

        self.label3 = tk.Label(self, text="Save Results Directory (Optional):")
        self.label3.pack(pady=5)

        self.entry3 = tk.Entry(self, width=70)
        self.entry3.pack(pady=5)

        self.button3 = tk.Button(self, text="Browse", command=self.browse_save_directory)
        self.button3.pack(pady=5)

        self.button2 = tk.Button(self, text="Search", command=self.search)
        self.button2.pack(pady=5)

        self.text = ScrolledText(self, wrap=tk.WORD)
        self.text.pack(pady=5, fill=tk.BOTH, expand=True)

    # --------- Section 6: GUI Helper Functions ---------
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, directory)

    def browse_save_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.entry3.delete(0, tk.END)
            self.entry3.insert(0, directory)

    # --------- Section 7: Search Exectuion ---------
    # --------- Section 7.1: Input Validation ---------
    def search(self):
        pdf_directory = self.entry1.get().strip()
        search_keyword = self.entry2.get().strip()
        save_directory = self.entry3.get().strip()

        if not pdf_directory or not search_keyword:
            messagebox.showwarning("Input Error", "Please provide both directory and keyword.")
            return

        if not os.path.isdir(pdf_directory):
            messagebox.showerror("Directory Error", "The specified PDF directory does not exist.")
            return

        # --------- Section 7.2: PDF File Check ---------
        pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
        if not pdf_files:
            messagebox.showerror("Directory Error", "No PDF files found in the specified directory.")
            return

        # --------- Section 7.3: Keyword Search and Results Display ---------
        results = search_keyword_in_pdfs(pdf_directory, search_keyword)

        self.text.delete(1.0, tk.END)
        for pdf, paragraphs in results.items():
            self.text.insert(tk.END, f"\nPDF: {pdf}\n", "pdf")
            for para in paragraphs:
                start_idx = self.text.index(tk.END)
                self.text.insert(tk.END, f"\n{para}\n")
                end_idx = self.text.index(tk.END)
                # Highlight the keyword within the paragraph
                self.highlight_keyword(start_idx, end_idx, search_keyword)

        # Highlight the PDF file names
        self.text.tag_config("pdf", background="yellow", foreground="black")
        # Highlight the keyword
        self.text.tag_config("highlight", background="lightgreen", foreground="black")

        # --------- Section 7.4: Optional Results Saving ---------
        # Optional: Save results to a text file if a directory is provided
        if save_directory:
            if not os.path.isdir(save_directory):
                messagebox.showerror("Save Directory Error", "The specified save directory does not exist.")
                return

            save_path = os.path.join(save_directory, 'search_results.txt')
            try:
                with open(save_path, 'w') as f:
                    for pdf, paragraphs in results.items():
                        f.write(f"\nPDF: {pdf}\n")
                        for para in paragraphs:
                            f.write(f"\n{para}\n")
                messagebox.showinfo("Save Results", f"Results saved to {save_path}")
            except Exception as e:
                messagebox.showerror("Save Error", f"An error occurred while saving the file: {e}")

    # --------- Section 8: Keyword Highlighting Function ---------
    def highlight_keyword(self, start_idx, end_idx, keyword):
        text = self.text.get(start_idx, end_idx)
        start = text.lower().find(keyword.lower())
        while start != -1:
            start_pos = f"{start_idx}+{start}c"
            end_pos = f"{start_pos}+{len(keyword)}c"
            self.text.tag_add("highlight", start_pos, end_pos)
            start = text.lower().find(keyword.lower(), start + len(keyword))


# --------- Section 9: Application Execution --------- 
# Run the application
if __name__ == "__main__":
    app = PDFSearchApp()
    app.mainloop()
