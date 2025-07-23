---
marp: true
theme: style
size: 16:9
paginate: true
---

# Pythonセミナー 第2回

## 関数の引数の応用

---

## この時間に学ぶこと

- 関数の引数を、より柔軟に扱う方法を学ぶ
- `*args` を使って、任意の数の「位置引数」を受け取る方法を理解する
- `**kwargs` を使って、任意の数の「キーワード引数」を受け取る方法を理解する
- これらのテクニックが、なぜデコレーターなどで重要になるのかを知る

---

## 引数の基本（復習）

通常、関数を定義する際には、受け取る引数の数と名前は決まっています。
しかし、もっと柔軟に引数を受け取りたい場合があります。

**コード例: `python/02/args_basic.py`**

```python
def introduce(name, age):
    print(f"私の名前は{name}です。年齢は{age}歳です。")

introduce("田中", 30) # 位置引数
introduce(age=25, name="鈴木") # キーワード引数
```

---

## 任意の数の「位置引数」を受け取る: `*args`

引数名の前に `*` を付けると、その関数は任意の数の位置引数を**タプル**として受け取ることができます。
慣習的に `args` (argumentsの略) という名前が使われます。

**コード例: `python/02/args_star.py`**

```python
def sum_all(*args):
    print(f"受け取った引数: {args}") # argsはタプル
    # ... (合計を計算する処理)
```

---

## 任意の数の「キーワード引数」を受け取る: `**kwargs`

引数名の前に `**` を付けると、その関数は任意の数のキーワード引数を**辞書**として受け取ることができます。
慣習的に `kwargs` (keyword argumentsの略) という名前が使われます。

**コード例: `python/02/kwargs_star_star.py`**

```python
def print_profile(**kwargs):
    print(f"受け取った引数: {kwargs}") # kwargsは辞書
    # ... (プロフィールを表示する処理)
```

---

## 全部乗せ: 通常の引数と`*args`, `**kwargs`

これらは組み合わせて使うことができます。

* ただし、**書く順番が重要**です。
* 順番: 通常の引数 → `*args` → `**kwargs`

**コード例: `02/args_kwargs_all_in_one.py`**

```python
def all_in_one(a, b, *args, **kwargs):
    # 詳細は `02/args_kwargs_all_in_one.py` を参照
    pass
```

---

## なぜこれらが必要なのか？

**「他の関数に、受け取った引数をそのまま渡したい」** 場合に非常に重要になります。

例えば、ある関数をラップ（包み込む）して、前後に処理を追加したい場合を考えます。
中の関数がどんな引数を受け取るか分からなくても、`*args`と`**kwargs`を使えば、すべての引数をそのまま渡すことができます。

---

## デコレーターでの活用例

これこそが、まさにデコレーターがやっていることです。

**コード例: `python/02/decorator_example.py`**

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # funcがどんな引数を持つか分からない！
        # でも *args, **kwargs を使えば大丈夫
        # 受け取った引数をそのままfuncに渡す
        return func(*args, **kwargs)
    return wrapper
```

---

## 引数のアンパック

`*`や`**`は、関数を呼び出す側で使うこともできます。
リストや辞書を展開して、関数の引数として渡すことができます。
これを「アンパック」と呼びます。

**コード例: `02/unpacking_example.py`**

```python
numbers = [1, 2, 3]
sum_all(*numbers) # sum_all(1, 2, 3) と同じ

profile = {"name": "高橋", "age": 40}
print_profile(**profile) # print_profile(name="高橋", age=40) と同じ
```

---

## 2時間目のまとめ

- `*args`: 任意の数の「位置引数」をタプルとして受け取る
- `**kwargs`: 任意の数の「キーワード引数」を辞書として受け取る
- これらを使うことで、どんな引数を持つ関数でもラップできる、柔軟な関数を作れる
- この仕組みは、次回復習するデコレーターの核心部分で使われている
- `*`や`**`を呼び出し側で使うと、リストや辞書を引数としてアンパックできる
