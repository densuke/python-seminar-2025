from functools import singledispatch

@singledispatch
def process(obj):
    print(f"デフォルト: {obj}")

@process.register(int)
def _(obj):
    print(f"整数を2倍にします: {obj * 2}")

@process.register(str)
def _(obj):
    print(f"文字列を繰り返します: {obj * 2}")

process(10)       # -> 整数を2倍にします: 20
process("Python") # -> 文字列を繰り返します: PythonPython
process([1, 2])   # -> デフォルト: [1, 2]