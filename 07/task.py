import dataclasses
from typing import Optional

@dataclasses.dataclass
class Task:
    id: int
    title: str
    completed: bool = False

    def __str__(self):
        status = "完了" if self.completed else "未完了"
        return f"[{self.id}] {self.title} ({status})"
