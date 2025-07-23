# 変数の型ヒント
user_name: str = "Alice"
user_age: int = 30


# 関数の引数と戻り値の型ヒント
def greet(name: str, age: int) -> str:
    return f"こんにちは、{name}さん({age}歳)！"

# 戻り値がない場合は -> None
def print_message(message: str) -> None:
    print(message)
