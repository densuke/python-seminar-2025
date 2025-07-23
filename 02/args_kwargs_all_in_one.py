def all_in_one(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

all_in_one(1, 2, 3, 4, 5, name="佐藤", job="エンジニア")