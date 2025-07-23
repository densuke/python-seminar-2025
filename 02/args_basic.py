def introduce(name, age):
    print(f"私の名前は{name}です。年齢は{age}歳です。")

# 位置引数 (positional arguments)
introduce("田中", 30)

# キーワード引数 (keyword arguments)
introduce(age=25, name="鈴木")