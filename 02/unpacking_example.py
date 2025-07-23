def sum_all(*args):
    print(f"受け取った引数: {args}") # argsはタプル
    total = 0
    for num in args:
        total += num
    return total

def print_profile(**kwargs):
    print(f"受け取った引数: {kwargs}") # kwargsは辞書
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

numbers = [1, 2, 3]
print(sum_all(*numbers)) # sum_all(1, 2, 3) と同じ

profile = {"name": "高橋", "age": 40}
print_profile(**profile) # print_profile(name="高橋", age=40) と同じ