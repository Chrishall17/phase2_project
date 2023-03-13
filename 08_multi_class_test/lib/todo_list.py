# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._todolist = []

    def add(self, todo):
        self._todolist.append(todo)

    def incomplete(self):
        return [i for i in self._todolist if getattr(i, i.task) == False]

    def complete(self):
        return [i for i in self._todolist if getattr(i, i.task) == True]

    def give_up(self):
        for i in self._todolist:
            setattr(i, i.task, True)

