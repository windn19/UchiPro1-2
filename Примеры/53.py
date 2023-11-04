first = [i ** 2 for i in range(1, 6)]
second = {s.upper() for s in 'hello'}
third = {k: chr(k) for k in [97, 98, 99]}
fourth = [i for i in range(10) if i % 3 == 0 or i % 2 == 0]  # с фильтрацией
print(first)  # [1, 4, 9, 16, 25]
print(second)  # {'L', 'E', 'O', 'H'}
print(third)  # {97: 'a', 98: 'b', 99: 'c'}
print(fourth)  # [0, 2, 3, 4, 6, 8, 9]
