# File: lib/todo.py
class Todo:
    def __init__(self, task):
        self.task = task
        setattr(Todo, self.task, False)

    def mark_complete(self):
        setattr(Todo, self.task, True)