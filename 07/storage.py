import json
import dataclasses
from typing import List
from task import Task

FILENAME = "tasks.json"

def save_tasks(tasks: List[Task]):
    task_dicts = [dataclasses.asdict(t) for t in tasks]
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(task_dicts, f, ensure_ascii=False, indent=2)

def load_tasks() -> List[Task]:
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            task_dicts = json.load(f)
            return [Task(**d) for d in task_dicts]
    except FileNotFoundError:
        return []
