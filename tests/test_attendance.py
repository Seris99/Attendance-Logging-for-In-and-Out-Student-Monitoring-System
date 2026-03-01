import pytest
from src.student import Student
from src.attendance_logger import AttendanceLogger
from src.database_manager import DatabaseManager

@pytest.fixture
def db_manager(tmp_path):
    # Use a temporary database file for testing
    return DatabaseManager(str(tmp_path / "test_attendance.db"))

def test_log_event_blackbox(db_manager):
    """Black-box: Check output message correctness."""
    logger = AttendanceLogger(db_manager)
    student = Student("123", "Alice")
    result = logger.log_event(student, "IN")
    assert "Logged Alice as IN" in result

def test_log_event_whitebox(db_manager):
    """White-box: Verify database entry is created."""
    logger = AttendanceLogger(db_manager)
    student = Student("456", "Bob")
    logger.log_event(student, "OUT")
    logs = db_manager.get_logs()
    assert any(log[0] == "456" and log[2] == "OUT" for log in logs)

def test_student_creation_tdd():
    """TDD cycle example: Student creation."""
    student = Student("789", "Charlie")
    assert student.student_id == "789"
    assert student.name == "Charlie"