import functools
import time

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# キャッシュなしだと非常に時間がかかる
start = time.time()
fib(35)
print(f"実行時間: {time.time() - start:.4f}秒")