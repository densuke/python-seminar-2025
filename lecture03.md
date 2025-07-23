---
marp: true
theme: style
size: 16:9
paginate: true
mermaid: true
---
<style>
</style>

# Pythonセミナー 第3回

## デコレーター入門

---

## この時間に学ぶこと

- デコレーターとは何か、その基本的な考え方を理解する
- デコレーターの作り方と使い方を学ぶ
- Pythonの標準ライブラリが提供する便利なデコレーターを知る
- フレームワークで使われるデコレーターの役割を理解する

---

## `@` の役割

- `@`はPythonを使っていくと出てくる構文で『デコレーター』と呼ばれます
- 役割は『関数を修飾する』こと

```python
@some_decorator
def my_function():
    pass
```

これで`my_function`は`some_decorator`で修飾された関数になります。
って『修飾(デコレート)』とは何?
これを知ることが今後大切になってきます。

---

## デコレータへの道
### Pythonとオブジェクトの関係

※※ **ここから暫くは小難しい話となります** 耐えてください ※※

デコレータを本格的に理解する前に、Pythonの内部的な挙動を知っておくと理解が深まります。
少し難易度が高いですが、普段できないところなので、ちょっと掘り下げてみましょう。

```powershell
PS> uv run python    # インタプリタ起動、バージョンは今回適当でOK
>>>
```

しばらくプロンプトは `>>>` となります。

---

### 現代Pythonは『全てがオブジェクト』である
<div class="container">
<div class="col-4">

```python
>>> id(0)
>>> id(1)
>>> id("42")
```
</div>

<div class="col-6">
<pre class="mermaid">
graph LR
    A["シンボルa"] --参照(=ID)--> O1["オブジェクト 42<br>(id=1001)"]
    B["シンボルb"] --参照(=ID)--> O1
    C["シンボルc"] --参照(=ID)--> O2["オブジェクト 'hello'<br>(id=2001)"]
</pre>
</div>
</div>

---

### オブジェクトとしてメソッドやフィールドが存在する

```python
>>> dir(0)
>>> dir(42)
```

足し算や引き算などの四則演算は所詮左辺のオブジェクトのメソッドが呼ばれているだけ。

```python
>>> (20).__add__(1) # 20+1
```
---

### 関数だってオブジェクト

<div class="container">

<div class="col-3">

```python
>>> def foo():
...    return 42
...
>>> id(foo)
>>> dir(foo)
```

</div>

<div class="col-7">

<pre class="mermaid">
graph LR
    A["シンボルfoo"] --参照(=ID)--> O1["関数定義<br>(id=1002)"]    
</pre>

</div>
</div>

---

### 関数かそうでないか?

* 関数も実体はオブジェクト
* 関数というよりは『呼び出し可能』なものは `__call__` が定義されている。
    * def文は指定の名前でシンボルを作成し、`__call__`等を付与する処理の文
* というよりは関数というクラス(function)に属しているものである

```python
>>> foo.__call__()
>>> (42).__call__() # NG
```

---

### 関数もID管理されているので

普通に値として返せる

```python
>>> def hello():
...     def wrapper():
...         return "Hello"
...     return wrapper      # 注意、BSキーなどでひとつ戻すこと
...                         # ここはそのまま改行で関数定義の終了
>>> hello() # ???
>>> x = hello()
>>> x()
```

---

### 関数に関数を渡してもよい

関数の引数って、結局IDを渡しているだけ

```python
>>> def foo():
...     return 42
...     
>>> 
>>> def f(x):
...     return x()
...     
>>> f(foo)
```

---

### だったらこんなこともして良いよね

```python
>>> def log(f):
...     def wrapper():
...         print("---before---")
...         f()
...         print("---after---")
...     return wrapper
...     
>>> def foo():
...     print("foo")
...     
>>> wrapped_foo = log(foo)
>>> wrapped_foo()
```

---

### さらにこんなことをしたら?

```python
# 前の続きになります
>>> def bar():
...    print("bar")
...
>>> bar = log(bar) # ???
>>> bar()
```

※ 途中でbarの指すIDが変わることに注意!

---

### なにが起きたのか?

* 関数もオブジェクトであり、変数同様ID管理されている
* 引数で渡す物の実体はIDであり、戻り値だってIDである
* つまり、関数も変数と同じように扱える
* 関数xを渡して、関数xを呼び出す関数を返してもらうことができる
* 戻り値で本来の関数を置き換えることもできる
    ```python
    bar = log(bar) 
    ```

---

### Python側の『デコレーター』

```python
>>> @log
... def baz():
...     print("baz")
...
>>> baz = log(baz)
```

※※ 小難しい話はここで終わりです ※※

---

## デコレーターとは？

一言でいうと、**「関数を修飾（デコレート）する関数」** です。

ある関数を受け取り、何らかの処理を追加した**新しい関数を返す**、高階関数の一種です。
元の関数のコードを直接変更することなく、機能を追加・変更できるのが大きなメリットです。

**コード例: `03/decorator_basic.py`**

```python
@my_decorator
def my_function():
    pass # 詳細は `03/decorator_basic.py` を参照
```

---

## 簡単なデコレーターを作ってみよう

関数の実行前後にメッセージを出すデコレーターを作ってみます。

**コード例: `03/decorator_simple.py`**

```python
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # ... (処理)
        return result
    return wrapper

@logger_decorator
def say_hello(name):
    print(f"こんにちは、{name}さん！")
```

---

## 実用的なデコレーター紹介 (1)

### `@functools.lru_cache`

関数の結果をキャッシュ（一時保存）して、同じ引数での呼び出しを高速化します。重い計算を何度も行う場合に非常に有効です。今回はLRU(Least Recently Used)のサンプルです。

**コード例: `03/lru_cache_example.py`**

```python
@functools.lru_cache(maxsize=None)
def fib(n):
    # ... (フィボナッチ計算)
    return fib(n-1) + fib(n-2)
```

---

## 実用的なデコレーター紹介 (2)
### `@functools.singledispatch`

関数の最初の引数の型によって、処理を切り替える「ジェネリック関数」を作成できます。同じ関数名で、渡すデータの型に応じて異なる振る舞いをさせたい場合に便利です。

**コード例: `03/singledispatch_example.py`**

```python
from functools import singledispatch

@singledispatch
def process(obj):
    # ... (型に応じた処理)
```

---

## 実用的なデコレーター紹介 (3)

### `@bottle.route` (フレームワークの例)

Webフレームワークなどで、特定のURLへのアクセスと、それを処理する関数を結びつけるのによく使われます。
ここではBottle(`@route('/hello')`)を例にします。

**コード例: `03/bottle_example.py`**

```python
from bottle import route, run

@route('/')
def hello():
    return "<h1>Hello World!</h1>"
```

---

## 3時間目のまとめ

- デコレーターは、関数を引数に取り、新しい関数を返す高階関数である
- `@` はデコレーターを適用するためのシンタックスシュガー
- `@lru_cache`: 関数の結果をキャッシュして高速化する
- `@singledispatch`: 引数の型によって処理を振り分ける
- Webフレームワークでは、URLと処理関数を紐づけるのによく使われる

<!-- Mermaidを読み込み -->
<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
</script>
