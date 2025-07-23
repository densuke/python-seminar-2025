import argparse
import storage
from task import Task

def main():
    parser = argparse.ArgumentParser(description="シンプルなToDoアプリ")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'add' コマンド
    parser_add = subparsers.add_parser("add", help="新しいタスクを追加")
    parser_add.add_argument("title", type=str, help="タスクのタイトル")

    # 'list' コマンド
    parser_list = subparsers.add_parser("list", help="タスクを一覧表示")

    # 'done' コマンド
    parser_done = subparsers.add_parser("done", help="タスクを完了")
    parser_done.add_argument("id", type=int, help="完了するタスクのID")

    # 'delete' コマンド
    parser_delete = subparsers.add_parser("delete", help="タスクを削除")
    parser_delete.add_argument("id", type=int, help="削除するタスクのID")

    args = parser.parse_args()
    tasks = storage.load_tasks()

    if args.command == "add":
        new_id = max([t.id for t in tasks] or [0]) + 1
        new_task = Task(id=new_id, title=args.title)
        tasks.append(new_task)
        storage.save_tasks(tasks)
        print(f"タスクを追加しました: {new_task.title}")

    elif args.command == "list":
        if not tasks:
            print("タスクはありません。")
        for task in tasks:
            print(task)

    elif args.command == "done":
        for task in tasks:
            if task.id == args.id:
                task.completed = True
                storage.save_tasks(tasks)
                print(f"タスクを完了しました: {task.title}")
                return
        print(f"ID {args.id} のタスクが見つかりません。")

    elif args.command == "delete":
        tasks = [t for t in tasks if t.id != args.id]
        storage.save_tasks(tasks)
        print(f"タスクを削除しました。")

if __name__ == "__main__":
    main()
