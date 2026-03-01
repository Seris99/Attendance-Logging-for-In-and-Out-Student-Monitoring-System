import sqlite3

class DatabaseManager:
    """Handles database operations for attendance logs."""
    def __init__(self, db_name="attendance.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id TEXT,
                name TEXT,
                status TEXT,
                timestamp TEXT
            )
        """)
        self.conn.commit()

    def save(self, record):
        self.cursor.execute("INSERT INTO attendance VALUES (?, ?, ?, ?)",
                            (record["id"], record["name"], record["status"], record["time"]))
        self.conn.commit()

    def get_logs(self):
        self.cursor.execute("SELECT * FROM attendance")
        return self.cursor.fetchall()