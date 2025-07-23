import pytest
from task import Task

def test_task_str_representation():
    """Taskオブジェクトが正しい文字列表現を返すかテストする"""
    task_incomplete = Task(id=1, title="未完了のタスク", completed=False)
    assert str(task_incomplete) == "[1] 未完了のタスク (未完了)"

    task_complete = Task(id=2, title="完了したタスク", completed=True)
    assert str(task_complete) == "[2] 完了したタスク (完了)"
