from lib.todo_list import TodoList

"""
Initially we give no tasks and TodoList returns empty list
"""

def test_no_todos_returns_empty_list():
    todolist = TodoList()
    assert todolist._todolist == []