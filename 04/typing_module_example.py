from typing import List, Dict, Optional

# 文字列のリストを受け取る関数
def process_names(names: List[str]) -> None:
    for name in names:
        print(f"- {name}")

# ユーザー情報を辞書で受け取る関数
def get_user_info(user_id: int) -> Optional[Dict[str, str]]:
    if user_id == 1:
        return {"name": "Alice", "email": "alice@example.com"}
    else:
        return None # ユーザーが見つからない場合はNoneを返す