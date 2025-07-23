def sum_all(*args):
    print(f"受け取った引数: {args}") # argsはタプル
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))       # -> 6
print(sum_all(10, 20, 30, 40)) # -> 100