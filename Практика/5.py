words = {}
for word in input().split():
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

for key, value in words.items():
    if value == max(words.values()):
        print(key)