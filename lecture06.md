---
marp: true
theme: style
size: 16:9
paginate: true
---

# Pythonセミナー 第6回

## pytestによる発展的なテスト

---

## この時間に学ぶこと

- `doctest`の限界と、本格的なテストフレームワークの必要性を理解する
- `pytest`の基本的な使い方と、シンプルなテストの書き方を習得する
- テストの準備と後片付けを自動化する「フィクスチャ」の概念を学ぶ
- 例外の発生や、特定の警告が出ることをテストする方法を知る

---

## なぜ`pytest`なのか？

`doctest`は手軽で便利ですが、複雑なテストには向きません。

- テストのセットアップ（準備）やクリーンアップ（後片付け）が難しい
- テストケースが増えると、docstringが読みにくくなる
- 詳細なテストレポートや、柔軟なテスト実行ができない

`pytest`は、Pythonで最も広く使われているテストフレームワークです。
シンプルに書けるのに非常に高機能で、プラグインも豊富なため、あらゆるテストに対応できます。

---

## `pytest`の基本

1.  **インストール**: `uv add --dev pytest`
2.  **ファイル名**: テストファイルは `test_*.py` または `*_test.py` という名前にします。
3.  **関数名**: テスト関数は `test_*` という名前にします。
4.  **アサーション**: テストの検証には、Python標準の `assert` 文を使います。
5.  **実行**: コマンドラインで `pytest` と入力するだけです。

---

## 簡単なテストを書いてみよう

**コード例: `06/calc.py`**
```python
def add(a, b):
    return a + b
```

**コード例: `06/test_calc.py`**
```python
from calc import add

def test_add_positive_numbers():
    assert add(2, 3) == 5
# ...
```

---

## `pytest`の実行

`pytest`を実行すると、これらの`test_`で始まる関数が自動的に発見・実行されます。

pytestを入れた記憶の無い方は追加しておきましょう。

```powershell
uv add --dev pytest
```

で、実行します

```powershell
uv run pytest 06/test_calc.py
```

---

## フィクスチャ: テストの「準備」と「後片付け」

フィクスチャ (fixture) は、テストを実行するための前提条件（データ、オブジェクト、環境設定など）を準備するための仕組みです。

- `@pytest.fixture` デコレータを付けて定義します。
- テスト関数が、フィクスチャ関数名を引数として受け取ることで利用できます。
- テストの実行前に準備処理を行い、テスト終了後に後片付け処理を行うことができます。

---

## フィクスチャの例

一時的なテストファイルを作成し、テスト終了後には自動で削除するフィクスチャです。少し長くてスライドをはみ出すので、実際のコードを見てください。

**コード例: `06/fixture_example.py`**
```python
import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    # ...準備処理...
    yield file_path
    # ...後片付け処理...

def test_read_write_file(temp_file):
    with open(temp_file, 'w') as f:
        f.write("hello")
    with open(temp_file, 'r') as f:
        assert f.read() == "hello"
```

---

## 例外をテストする: `pytest.raises`

特定の例外が発生することを期待するテストを書くには、`pytest.raises`を使います。こちらも実際のコード例を見てください。

**コード例: `06/raises_example.py`**
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)
```
`with`ブロック内で指定した例外が発生すればテストは成功、しなければ失敗となります。

---

## 6時間目のまとめ

- 複雑なテストには、`pytest`のような専門のフレームワークが不可欠
- `pytest`は、`test_`で始まるファイル・関数を自動で認識して実行する
- アサーションには、シンプルな`assert`文が使える
- `@pytest.fixture`を使うと、テストの準備や後片付けを共通化・自動化できる
- `pytest.raises`を使うと、特定の例外が発生することを簡単にテストできる
