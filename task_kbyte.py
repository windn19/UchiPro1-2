n = int(input('Число: '))
c = input("Перевести в байты(b) или килобайты(k): ")
while c not in 'bk':
    c = input("Перевести в байты(b) или килобайты(k): ")
if c == 'b':
    print(f'{n}Кб = {n * 1024} байт')
else:
    print(f'{n} байт = {n / 1024: .2f}Кб')
