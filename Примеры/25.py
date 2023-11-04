first = 'HELLO'
second = 'world 123'
# строка состоит только из символов нижнего регистра
print(first.islower())  # True
# строка состоит только из символов верхнего регистра
print(first.isupper())  # True
# возвращает строку в нижнем регистре
third = first.lower()
print(third)  # hello
print(first)  # HELLO
# возвращает строку в которой первый символ приведен к верхнему регистру
print(second.capitalize())  # World 123
# строка состоит только из цифр
print(first.isdigit())  # False
# строка состоит только из букв
print(first.isalpha())  # True
# строка состоит только из цифр и букв
print(second.isalnum())  # False

