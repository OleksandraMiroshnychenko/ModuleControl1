import pytest
from unittest.mock import MagicMock
from tkinter import Tk
from task_manager import TaskManager  # або ваш шлях до файлу

@pytest.fixture
def setup_tkinter():
    # Створюємо кореневе вікно для тестів
    root = Tk()
    yield root  # Повертаємо root, щоб він був доступний у тестах
    root.quit()  # Закриваємо кореневе вікно після тесту

def test_add_task(setup_tkinter):
    mock_root = MagicMock()  # Створюємо мок-об'єкт для root
    manager = TaskManager(mock_root)  # Тепер передаємо мок в конструктор

    # Викликаємо метод add_task і перевіряємо його результат
    manager.add_task("New Task")
    
    # Отримуємо задачі зі списку "To Do"
    tasks = manager.lists["To Do"]
    
    # Очікуємо, що задача буде додана в список "To Do"
    assert "New Task" in tasks  # Перевіряємо, чи є "New Task" в списку задач