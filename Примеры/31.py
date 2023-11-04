first = [1, 2, 3]
second = ['a', 'bb', 'ccc']
print(first + second)  # [1, 2, 3, 'a', 'bb', 'ccc']
print(second * 2)  # ['a', 'bb', 'ccc', 'a', 'bb', 'ccc']
print(first < [1, 2, 4])  # True
print(second in (first + second))  # False
print(len(second))  # 3
print(sum(first))  # 6
first[0] = -1
print(first)  # [-1, 2, 3]
