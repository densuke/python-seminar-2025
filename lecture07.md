---
marp: true
theme: style
size: 16:9
paginate: true
---

# Pythonセミナー 第7回

## ミニプロジェクト: コマンドラインToDoアプリ

---

## この時間に学ぶこと

- これまでに学んだ知識を総動員して、一つのアプリケーションを作成する
- `dataclasses`: データ構造をシンプルに定義する
- `argparse`: コマンドラインの引数をスマートに処理する
- `json`: Pythonのオブジェクトをファイルに保存・復元する
- 複数のモジュールを連携させて、プログラムを組み立てる感覚を掴む

---

## プロジェクトの概要

コマンドラインからタスクの追加、一覧表示、完了、削除ができるシンプルなToDoアプリケーションを作成します。

**完成イメージ:**
```powershell
# タスクを追加
uv run 07/todo.py add "Pythonの課題をやる"

# タスクを一覧表示
uv run 07/todo.py list
[1] Pythonの課題をやる (未完了)

# タスクを完了
uv run 07/todo.py done 1
```

---

## 設計と方針

ボリュームがあるため、今回は**完成版のコードを先に配布**します。

授業では、コードの各部分がどの役割を担っているのかを解説し、実際に動かしながら理解を深めていきます。
最後に、少しだけ機能を追加する演習を行います。

**主なファイル構成:**
- `07/todo.py`: メインの実行ファイル
- `07/task.py`: タスクのデータ構造を定義
- `07/storage.py`: データの読み書きを担当
- `tasks.json`: タスクデータを保存するファイル

---

## 1. データ構造の定義: `dataclasses`

`task.py`
```python
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
```
- `@dataclasses.dataclass`デコレータを付けるだけで、`__init__`や`__repr__`などが自動で定義されます。
- クラスの属性（フィールド）を型ヒント付きで宣言するだけで済み、非常に簡潔です。

---

## 2. データの永続化: `json`

`storage.py`
```python
import json
from typing import List
from task import Task

FILENAME = "tasks.json"

def save_tasks(tasks: List[Task]):
    # dataclassesを辞書のリストに変換
    task_dicts = [dataclasses.asdict(t) for t in tasks]
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(task_dicts, f, ensure_ascii=False, indent=2)

def load_tasks() -> List[Task]:
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            task_dicts = json.load(f)
            # 辞書のリストをTaskオブジェクトのリストに変換
            return [Task(**d) for d in task_dicts]
    except FileNotFoundError:
        return []
```

---

## 3. コマンドライン処理: `argparse`

## 3. コマンドライン処理: `argparse`

**コード例: `07/todo.py`**
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="シンプルなToDoアプリ")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'add' コマンド
    parser_add = subparsers.add_parser("add", help="新しいタスクを追加")
    # ...

    args = parser.parse_args()
    # ... (args.commandに応じて処理を分岐)
```

---

## 演習: アプリを動かしてみよう

1.  配布されたコード (`todo.py`, `task.py`, `storage.py`) を同じディレクトリに配置します。
2.  コマンドラインで、実際にタスクを追加、一覧表示、完了させてみましょう。

    ```powershell
    python todo.py add "セミナーの復習をする"
    python todo.py list
    python todo.py done 1
    python todo.py list
    ```
3.  `tasks.json`ファイルが作成され、中身が更新されることを確認しましょう。

---

## (発展) 演習: 機能を追加してみよう

現在の`list`コマンドは、すべてのタスクを表示します。
ここに、**未完了のタスクのみを表示する** `--pending` オプションを追加してみましょう。

**ヒント:**
1.  `todo.py`の`list`コマンドのパーサーに、`add_argument`で`--pending`を追加します。アクションは`store_true`が便利です。
2.  `list`コマンドの処理部分で、`args.pending`が`True`かどうかを判定します。
3.  `True`なら、タスクリストから`completed`が`False`のものだけをフィルタリングして表示します。

---

## 7時間目のまとめ

- `dataclasses`でデータ構造を簡潔に定義した
- `json`モジュールで、Pythonオブジェクトとテキストファイル（JSON）を相互に変換し、データを保存した
- `argparse`で、サブコマンドを持つ本格的なコマンドラインインターフェースを構築した
- これらを組み合わせることで、一つのアプリケーションが完成することを体験した

**学んだ知識を組み合わせることで、作れるものの幅は大きく広がります！**
