def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(10, 20) # ここを"20"にしてみよう!
# VS Code上でこのコードを書くと、`"20"`の部分に波線が表示され、「Expected type 'int', got 'str' instead」のような警告が表示されます。
# これにより、実行前にバグを発見できるのです。

