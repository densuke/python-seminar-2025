def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- 処理開始 ---")
        result = func(*args, **kwargs)
        print("--- 処理終了 ---")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name):
    print(f"Hello, {name}")