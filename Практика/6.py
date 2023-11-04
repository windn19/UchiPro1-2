n = int(input())
print([i for i in range(1, n + 1) if n >= 4 and i % (n // 4) == 0])