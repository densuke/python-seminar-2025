import pytest
import json
import os
from task import Task
import storage

@pytest.fixture
def temp_json_file(tmp_path):
    """一時的なJSONファイルを提供するフィクスチャ"""
    file_path = tmp_path / "test_tasks.json"
    # storageモジュールのFILENAMEを一時ファイルのパスに差し替える
    original_filename = storage.FILENAME
    storage.FILENAME = file_path
    yield file_path
    # テスト終了後に後片付け
    storage.FILENAME = original_filename
    if os.path.exists(file_path):
        os.remove(file_path)

def test_save_and_load_tasks(temp_json_file):
    """タスクの保存と読み込みが正しく行えるかテストする"""
    # 1. 空の状態でロードすると空のリストが返るか
    assert storage.load_tasks() == []

    # 2. タスクを保存して、正しく読み込めるか
    tasks_to_save = [
        Task(id=1, title="テストタスク1", completed=False),
        Task(id=2, title="テストタスク2", completed=True),
    ]
    storage.save_tasks(tasks_to_save)

    loaded_tasks = storage.load_tasks()
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].title == "テストタスク1"
    assert loaded_tasks[1].completed is True

    # 3. 空のリストを保存できるか
    storage.save_tasks([])
    assert storage.load_tasks() == []
