def print_profile(**kwargs):
    print(f"受け取った引数: {kwargs}") # kwargsは辞書
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

print_profile(name="山田", age=28, city="東京")
# - name: 山田
# - age: 28
# - city: 東京