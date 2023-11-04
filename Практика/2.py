number = input()
if number[0] == '8' and number[1:].isdigit() and len(number) == 11:
    print('Номер введен верно')
elif number[:2] == '+7' and number[2:].isdigit() and len(number) == 12:
    print('Номер введен верно')
else:
    print('Номер введен неверно')
