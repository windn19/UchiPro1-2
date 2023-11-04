date = input()
dd, mm, yyyy = date[3:5], date[:2], date[6:]
print(f'{dd}.{mm}.{yyyy}')