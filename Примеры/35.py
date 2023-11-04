first = [4, 5, 1, 2, 3, 4, 5]
index = first.index(3)  # возвращает индекс первого вхождения элемента в список
print(index)  # 4
count = first.count(4)  # возвращает количество вхождений элемента в список
print(count)  # 2
first.sort()  # сортирует список по возрастанию
print(first)  # [1, 2, 3, 4, 4, 5, 5]
first.reverse()  # переворачивает список
print(first)  # [5, 5, 4, 4, 3, 2, 1]
