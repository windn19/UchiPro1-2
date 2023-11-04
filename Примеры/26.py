first = 'HELLO Hello hello'
# количество вхождений подстроки в строку
print(first.count('l'))  # 4
print(first.count('ell'))  # 2
# возвращает индекс первого вхождения подстроки
print(first.find('e'))  # 7
# возвращает индекс последнего вхождения подстроки
print(first.rfind('ell'))  # 13
# возвращает строку с заменой
print(first.replace('e', 'E'))  # HELLO HEllo hEllo
