def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} を実行します")
        result = func(*args, **kwargs)
        print(f"{func.__name__} の実行が完了しました")
        return result
    return wrapper

@logger_decorator
def say_hello(name):
    print(f"こんにちは、{name}さん！")

say_hello("田中")