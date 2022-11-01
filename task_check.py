a, b = map(int, input().split())
result = divmod(a, b)
if not result[1]:
    print(f'Число {a} делится на {b}. Результат: {result[0]}')
else:
    print(f'Число {a} не делится на {b}. Результат: {result[0]} остаток {result[1]}')


if not a % b:
    print(f'Число {a} делится на {b}. Результат: {a // b}')
else:
    print(f'Число {a} не делится на {b}. Результат: {a // b} остаток {a % b}')
