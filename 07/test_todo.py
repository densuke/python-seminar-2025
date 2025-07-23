import pytest
from unittest.mock import patch
import todo
import storage
from task import Task

@pytest.fixture(autouse=True)
def mock_storage(monkeypatch):
    """storageのload/saveをモックし、テストごとに独立したタスクリストを管理する"""
    tasks = []

    def mock_load_tasks():
        return [Task(**t) for t in tasks]

    def mock_save_tasks(tasks_to_save):
        nonlocal tasks
        tasks = [t.__dict__ for t in tasks_to_save]

    monkeypatch.setattr(storage, 'load_tasks', mock_load_tasks)
    monkeypatch.setattr(storage, 'save_tasks', mock_save_tasks)

def test_add_command(capsys):
    """addコマンドのテスト"""
    with patch('sys.argv', ['todo.py', 'add', '新しいタスク']):
        todo.main()
    captured = capsys.readouterr()
    assert "タスクを追加しました: 新しいタスク" in captured.out

    tasks = storage.load_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "新しいタスク"
    assert tasks[0].completed is False

def test_list_command(capsys):
    """listコマンドのテスト"""
    # タスクがない場合
    with patch('sys.argv', ['todo.py', 'list']):
        todo.main()
    captured = capsys.readouterr()
    assert "タスクはありません。" in captured.out

    # タスクを追加してからリスト表示
    storage.save_tasks([Task(id=1, title="リスト表示テスト", completed=False)])
    with patch('sys.argv', ['todo.py', 'list']):
        todo.main()
    captured = capsys.readouterr()
    assert "[1] リスト表示テスト (未完了)" in captured.out

def test_done_command(capsys):
    """doneコマンドのテスト"""
    storage.save_tasks([Task(id=1, title="完了テスト", completed=False)])
    with patch('sys.argv', ['todo.py', 'done', '1']):
        todo.main()
    captured = capsys.readouterr()
    assert "タスクを完了しました: 完了テスト" in captured.out

    tasks = storage.load_tasks()
    assert tasks[0].completed is True

    # 存在しないIDを指定
    with patch('sys.argv', ['todo.py', 'done', '99']):
        todo.main()
    captured = capsys.readouterr()
    assert "ID 99 のタスクが見つかりません。" in captured.out

def test_delete_command(capsys):
    """deleteコマンドのテスト"""
    storage.save_tasks([Task(id=1, title="削除テスト", completed=False)])
    with patch('sys.argv', ['todo.py', 'delete', '1']):
        todo.main()
    captured = capsys.readouterr()
    assert "タスクを削除しました。" in captured.out
    assert len(storage.load_tasks()) == 0
