import tkinter as tk
from tkinter import ttk
from student import Student
from database_manager import DatabaseManager
from attendance_logger import AttendanceLogger

class AttendanceApp:
    """Tkinter GUI for Attendance Logging Subsystem with log display."""
    def __init__(self, root):
        self.db = DatabaseManager()
        self.logger = AttendanceLogger(self.db)

        root.title("Attendance Logging System")
        root.geometry("600x400")

        # Input Frame
        input_frame = ttk.Frame(root, padding="10")
        input_frame.pack(fill="x")

        ttk.Label(input_frame, text="Student ID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id = ttk.Entry(input_frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_name = ttk.Entry(input_frame)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        button_frame = ttk.Frame(root, padding="10")
        button_frame.pack(fill="x")

        ttk.Button(button_frame, text="Log IN", command=self.log_in).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Log OUT", command=self.log_out).pack(side="left", padx=10)

        # Output Label
        self.output = ttk.Label(root, text="", foreground="blue")
        self.output.pack(pady=5)

        # Attendance Log Display
        log_frame = ttk.Frame(root, padding="10")
        log_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(log_frame, columns=("ID", "Name", "Status", "Timestamp"), show="headings")
        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.pack(fill="both", expand=True)

        # Load existing logs
        self.load_logs()

    def log_in(self):
        student = Student(self.entry_id.get(), self.entry_name.get())
        msg = self.logger.log_event(student, "IN")
        self.output.config(text=msg)
        self.clear_inputs()
        self.load_logs()

    def log_out(self):
        student = Student(self.entry_id.get(), self.entry_name.get())
        msg = self.logger.log_event(student, "OUT")
        self.output.config(text=msg)
        self.clear_inputs()
        self.load_logs()

    def load_logs(self):
        # Clear current rows
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Load from database
        logs = self.db.get_logs()
        for log in logs:
            self.tree.insert("", "end", values=log)

    def clear_inputs(self):
        """Clears the input fields after logging."""
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()