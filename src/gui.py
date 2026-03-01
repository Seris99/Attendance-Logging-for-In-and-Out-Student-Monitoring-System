import tkinter as tk
from student import Student
from database_manager import DatabaseManager
from attendance_logger import AttendanceLogger

class AttendanceApp:
    """Tkinter GUI for Attendance Logging Subsystem."""
    def __init__(self, root):
        self.db = DatabaseManager()
        self.logger = AttendanceLogger(self.db)

        root.title("Attendance Logging System")

        # Student ID input
        tk.Label(root, text="Student ID:").grid(row=0, column=0)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1)

        # Student Name input
        tk.Label(root, text="Name:").grid(row=1, column=0)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=1, column=1)

        # Buttons for IN/OUT
        tk.Button(root, text="Log IN", command=self.log_in).grid(row=2, column=0)
        tk.Button(root, text="Log OUT", command=self.log_out).grid(row=2, column=1)

        # Output label
        self.output = tk.Label(root, text="")
        self.output.grid(row=3, columnspan=2)

    def log_in(self):
        student = Student(self.entry_id.get(), self.entry_name.get())
        msg = self.logger.log_event(student, "IN")
        self.output.config(text=msg)

    def log_out(self):
        student = Student(self.entry_id.get(), self.entry_name.get())
        msg = self.logger.log_event(student, "OUT")
        self.output.config(text=msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()