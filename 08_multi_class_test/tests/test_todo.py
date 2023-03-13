from lib.todo import Todo

"""
Given a task
It has a property of false for incomplete
"""
def test_task_given_incomplete_returns_property_false():
    todo = Todo("Wash up")
    assert getattr(todo, todo.task) == False

"""
Given a task and marking complete
It has a property of true for complete
"""
def test_task_marked_as_complete_returns_property_true():
    todo = Todo("Wash up")
    todo.mark_complete()
    assert getattr(todo, todo.task) == True
