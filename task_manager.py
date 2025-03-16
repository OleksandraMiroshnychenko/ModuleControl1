import tkinter as tk  # Імпортуємо модуль tkinter для створення графічного інтерфейсу.
from tkinter import simpledialog  # Імпортуємо simpledialog для вводу користувачем тексту в діалоговому вікні.

class TaskManager:
    def __init__(self, root):
        # Ініціалізація класу TaskManager з основним вікном root.
        self.root = root
        self.root.title("Менеджер задач")  # Встановлюємо заголовок вікна.

        # Створюємо початкові списки задач.
        self.lists = {
            "To Do": [],
            "In Progress": [],
            "Done": []
        }

        # Словники для збереження фреймів і списків завдань.
        self.frames = {}
        self.listboxes = {}

        # Створення фреймів і списків для кожної категорії задач.
        for idx, (list_name, tasks) in enumerate(self.lists.items()):
            # Створюємо фрейм для кожної категорії задач.
            frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
            frame.grid(row=0, column=idx, padx=10, pady=10, sticky="n")  # Розміщуємо фрейм в сітці.
            tk.Label(frame, text=list_name, font=("Arial", 12, "bold")).pack(pady=5)  # Додаємо назву списку.

            # Створюємо Listbox для відображення задач.
            task_listbox = tk.Listbox(frame, width=30, height=10)
            task_listbox.pack(padx=5, pady=5)  
            task_listbox.bind("<Double-Button-1>", self.edit_task)  # Подвійний клік для редагування задачі.
            task_listbox.bind("<ButtonPress-1>", self.start_drag)  # Натискання для початку перетягування.
            task_listbox.bind("<ButtonRelease-1>", self.drop_task)  # Відпускання для переміщення задачі.

            # Кнопка для додавання нової задачі в поточний список.
            tk.Button(frame, text="Додати задачу", command=lambda l=list_name: self.add_task(l)).pack(pady=5)

            # Зберігаємо фрейм та Listbox для кожного списку задач.
            self.frames[list_name] = frame
            self.listboxes[list_name] = task_listbox

        # Змінні для збереження задачі, яку перетягуємо, та джерела перетягування.
        self.dragging_task = None
        self.source_listbox = None

    def add_task(self, list_name):
        
        task = simpledialog.askstring("Нова задача", "Введіть назву задачі:") 
        if task:  # Якщо введено назву задачі.
            self.lists[list_name].append(task)  # Додаємо задачу в список.
            self.listboxes[list_name].insert(tk.END, task)  # Вставляємо задачу в Listbox.

    def edit_task(self, event):
        # Редагує вибрану задачу.
        listbox = event.widget  # Отримуємо Listbox, на якому стався клік.
        try:
            index = listbox.curselection()[0]  # Отримуємо індекс вибраної задачі.
            old_task = listbox.get(index)  # Отримуємо стару задачу.
            new_task = simpledialog.askstring("Редагування", "Редагуйте задачу:", initialvalue=old_task)  # Запитуємо нову задачу.
            if new_task:  # Якщо введена нова назва.
                listbox.delete(index)  # Видаляємо стару задачу.
                listbox.insert(index, new_task)  # Вставляємо нову задачу.
                for list_name, tasks in self.lists.items():
                    if old_task in tasks:  # Шукаємо стару задачу в списку.
                        tasks[tasks.index(old_task)] = new_task  # Замінюємо стару задачу на нову.
        except IndexError:
            pass  # Якщо не було вибрано жодної задачі.

    def start_drag(self, event):
        """Запам’ятовуємо задачу для перетягування."""
        listbox = event.widget  # Отримуємо Listbox, з якого перетягується задача.
        try:
            index = listbox.curselection()[0]  # Отримуємо індекс вибраної задачі.
            self.dragging_task = listbox.get(index)  # Зберігаємо задачу для перетягування.
            self.source_listbox = listbox  # Запам’ятовуємо джерело перетягування.
        except IndexError:
            self.dragging_task = None  # Якщо задача не вибрана.

    def drop_task(self, event):
        """Переміщуємо задачу в інший список при відпусканні."""
        target_listbox = event.widget  # Отримуємо Listbox, в який перетягується задача.
        if self.dragging_task and self.source_listbox != target_listbox:  # Якщо задача вибрана і перетягується в інший список.
            for list_name, listbox in self.listboxes.items():
                if listbox == self.source_listbox:  # Якщо це джерело перетягування.
                    self.lists[list_name].remove(self.dragging_task)  # Видаляємо задачу з джерела.
                    self.source_listbox.delete(tk.ANCHOR)  # Видаляємо задачу з Listbox.
                if listbox == target_listbox:  # Якщо це цільовий список.
                    self.lists[list_name].append(self.dragging_task)  # Додаємо задачу в новий список.
                    target_listbox.insert(tk.END, self.dragging_task)  # Вставляємо задачу в Listbox.

        self.dragging_task = None  # Скидаємо вибрану задачу.
        self.source_listbox = None  # Скидаємо джерело перетягування.

if __name__ == "__main__":
    root = tk.Tk()  # Створюємо головне вікно.
    app = TaskManager(root)  # Ініціалізуємо менеджер задач.
    root.mainloop()  # Запускаємо головний цикл для взаємодії з користувачем.