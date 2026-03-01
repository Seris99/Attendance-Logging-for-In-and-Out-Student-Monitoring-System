from datetime import datetime

class AttendanceLogger:
    """Logs student IN/OUT events with timestamps."""
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def log_event(self, student, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "id": student.student_id,
            "name": student.name,
            "status": status,
            "time": timestamp
        }
        self.db_manager.save(record)
        return f"Logged {student.name} as {status} at {timestamp}"