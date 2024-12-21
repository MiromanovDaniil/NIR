import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from tkinter import filedialog

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI Interface")
        self.geometry("800x600")

        self.create_widgets()

        # Placeholder for FileSystemManager
        self.file_manager = FileSystemManager()

    def create_widgets(self):
        # Left Frame - Display Area
        self.left_frame = tk.Frame(self, width=400, height=600, bg="white")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text_area = scrolledtext.ScrolledText(self.left_frame, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Right Frame - Controls
        self.right_frame = tk.Frame(self, width=400, height=600)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # File Path Entry
        self.filepath_label = tk.Label(self.right_frame, text="File Path:")
        self.filepath_label.pack(pady=(20, 5))
        self.filepath_entry = tk.Entry(self.right_frame, width=40)
        self.filepath_entry.pack(pady=5)

        # Text Entry
        self.text_label = tk.Label(self.right_frame, text="Text (for writing):")
        self.text_label.pack(pady=(20, 5))
        self.text_entry = tk.Entry(self.right_frame, width=40)
        self.text_entry.pack(pady=5)

        # Flag Selection
        self.flag_label = tk.Label(self.right_frame, text="Flag (r/w):")
        self.flag_label.pack(pady=(20, 5))
        self.flag_combobox = ttk.Combobox(self.right_frame, values=["r", "w"], state="readonly")
        self.flag_combobox.pack(pady=5)
        self.flag_combobox.set("r")

        # Action Buttons
        self.open_button = tk.Button(self.right_frame, text="Open File", command=self.open_file_action)
        self.open_button.pack(pady=10)

        self.clear_button = tk.Button(self.right_frame, text="Clear Display", command=self.clear_display)
        self.clear_button.pack(pady=10)

        self.quit_button = tk.Button(self.right_frame, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

    def open_file_action(self):
        filepath = self.filepath_entry.get()
        text = self.text_entry.get()
        flag = self.flag_combobox.get()

        if not filepath:
            messagebox.showerror("Error", "File path is required.")
            return

        if flag == "w" and not text:
            messagebox.showerror("Error", "Text is required for writing.")
            return

        try:
            result = self.file_manager.open_file(text, filepath, flag)
            if flag == "r":
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, result)
            elif flag == "w":
                messagebox.showinfo("Success", f"Text written to {filepath}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_display(self):
        self.text_area.delete(1.0, tk.END)

class FileSystemManager:
    def __init__(self):
        pass

    def open_file(self, text, filepath, flag):
        try:
            if flag == 'r':
                with open(filepath, 'r') as f:
                    return f.read()
            elif flag == 'w':
                with open(filepath, 'w') as f:
                    f.write(text)
            else:
                raise ValueError("Unsupported flag. Use 'r' for read or 'w' for write.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File {filepath} not found.")
        except IOError as e:
            raise IOError(f"Error accessing file {filepath}: {e}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
