first = {1, 2, 3, 4, 5}
second = {2, 4, 5, 6}
# проверка равенства множеств
print(first == second)  # False
# множество second является подмножеством first
print(second < first)  # True
# объединение множеств
union = first | second  # union = first.union(second)
print(union)  # {1, 2, 3, 4, 5, 6} (в произвольном порядке)
# пересечение множеств
intersection = first & second  # intersection = first.intersection(second)
print(intersection)  # {2, 4, 5} (в произвольном порядке)
# разность множеств
difference = first - second  # difference = first.difference(second)
print(difference)  # {1, 3} (в произвольном порядке)
# симметрическая разность
symmetric_difference = first ^ second  # symmetric_difference = first.symmetric_difference(second)
print(symmetric_difference)  # {1, 3, 6} (в произвольном порядке)
