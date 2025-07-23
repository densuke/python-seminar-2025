from typing import Optional

def get_user(user_id: int) -> Optional[dict]:
    """指定されたIDのユーザー情報をデータベースから取得します。

    Args:
        user_id: 取得対象のユーザーID。

    Returns:
        ユーザー情報を含む辞書。ユーザーが見つからない場合はNoneを返します。

    Raises:
        ConnectionError: データベースへの接続に失敗した場合。
    """
    # ... (実際の処理)
    pass