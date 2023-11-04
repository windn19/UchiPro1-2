numbers = [int(n) for n in input().split()]
total = int(input())
visited = set()
for a in numbers:
    b = total - a
    if b in visited:
        print(b, a)
        break
    else:
        visited.add(a)
else:
    print(None)
