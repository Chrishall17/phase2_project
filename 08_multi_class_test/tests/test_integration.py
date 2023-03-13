from lib.todo_list import TodoList
from lib.todo import Todo

"""
Given two tasks todo
Todo_list returns the tasks presented in a list
"""
def test_add_two_tasks_incomplete_todolist_returns_tasks_in_list():
    todolist = TodoList()
    todo1 = Todo("Wash up")
    todo2 = Todo("Dry up")
    todolist.add(todo1)
    todolist.add(todo2)
    assert todolist._todolist == [todo1, todo2]

"""
Given two incomplete tasks todo
Todo_list returns the tasks presented in a list that are incomplete
"""
def test_add_two_tasks_complete_todolist_returns_tasks_in_list():
    todolist = TodoList()
    todo1 = Todo("Wash up")
    todo2 = Todo("Dry up")
    todolist.add(todo1)
    todolist.add(todo2)
    assert todolist.incomplete() == [todo1, todo2]

"""
Given two complete tasks todo
Todo_list returns the tasks presented in a list that are complete
"""
def test_add_two_tasks_complete_todolist_returns_tasks_in_list():
    todolist = TodoList()
    todo1 = Todo("Wash up")
    todo2 = Todo("Dry up")
    todo1.mark_complete()
    todo2.mark_complete()
    todolist.add(todo1)
    todolist.add(todo2)
    assert todolist.complete() == [todo1, todo2]

"""
Given one complete task and one incomplete task todo
Todo_list returns the tasks presented in a list from calling the correct method
"""
def test_add_two_tasks_one_complete_one_incomplete_todolist_returns_tasks_in_correct_list():
    todolist = TodoList()
    todo1 = Todo("Wash up")
    todo2 = Todo("Dry up")
    todo1.mark_complete()
    todolist.add(todo1)
    todolist.add(todo2)
    assert todolist.complete() == [todo1]
    assert todolist.incomplete() == [todo2]

"""
Given two tasks and calling the give up method
Todo_list returns the tasks presented in a list from calling complete
"""
def test_add_two_tasks_one_complete_one_incomplete_todolist_returns_tasks_in_correct_list():
    todolist = TodoList()
    todo1 = Todo("Wash up")
    todo2 = Todo("Dry up")
    todolist.add(todo1)
    todolist.add(todo2)    
    assert todolist.incomplete() == [todo1, todo2]
    todolist.give_up()
    assert todolist.complete() == [todo1, todo2]