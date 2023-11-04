first = [1, 2, 3]
first.append(4)  # добавляет новый элемент в конец списка
print(first)  # [1, 2, 3, 4]
second = [5, 6, 7]
first.extend(second)  # расширяет список другим списком
print(first)  # [1, 2, 3, 4, 5, 6, 7]
first.remove(5)  # удаляет элемент со значением 5
print(first)  # [1, 2, 3, 4, 7]
first.insert(2, 10)  # вставляет элемент на позицию с индексом 2
print(first)  # [1, 2, 10, 1, 2, 1, 2]
