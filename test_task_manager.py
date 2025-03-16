import pytest
from unittest.mock import MagicMock
from task_manager import TaskManager  # або ваш шлях до файлу

def test_add_task():
    mock_root = MagicMock()  # Створюємо мок-об'єкт для root
    manager = TaskManager(mock_root)  # Тепер передаємо мок в конструктор

    # Викликаємо метод add_task і перевіряємо його результат
    manager.add_task("New Task")
    
    # Отримуємо задачі зі списку "To Do"
    tasks = manager.lists["To Do"]
    
    # Очікуємо, що задача буде додана в список "To Do"
    assert "New Task" in tasks  # Перевіряємо, чи є "New Task" в списку задач
