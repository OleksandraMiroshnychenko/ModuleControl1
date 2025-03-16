import pytest
from task_manager import TaskManager  # Підключіть ваш клас TaskManager

def test_add_task():
    manager = TaskManager()
    manager.add_task("To Do", "Test Task")
    assert "Test Task" in manager.lists["To Do"]

def test_edit_task():
    manager = TaskManager()
    manager.add_task("To Do", "Test Task")
    manager.edit_task("Test Task", "Updated Task")
    assert "Updated Task" in manager.lists["To Do"]