import pytest
from unittest.mock import MagicMock, patch
from task_manager import TaskManager  # Шлях до вашого класу TaskManager

@pytest.fixture
def setup_tkinter():
    # Створюємо кореневе вікно для тестів
    root = MagicMock()  # Мок кореневого вікна, не потребує реальної ініціалізації Tk()
    yield root  # Повертаємо root для використання в тестах

def test_add_task(setup_tkinter):
    mock_root = setup_tkinter  # Використовуємо мок для root
    manager = TaskManager(mock_root)  # Передаємо мок в конструктор

    # Ініціалізація словника зі списками задач, якщо це потрібно
    manager.lists = {"To Do": []}  # Додати порожній список для "To Do"
    
    # Мокання виклику simpledialog.askstring
    with patch("tkinter.simpledialog.askstring", return_value="New Task"):
        # Викликаємо метод add_task і перевіряємо результат
        manager.add_task("To Do")  # Передаємо правильне ім'я списку

    # Отримуємо задачі зі списку "To Do"
    tasks = manager.lists["To Do"]

    # Очікуємо, що задача буде додана в список "To Do"
    assert "New Task" in tasks  # Перевіряємо, чи є "New Task" в списку задач
