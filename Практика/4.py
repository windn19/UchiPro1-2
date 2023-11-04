s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())
s = (s1 | s2 | s3) - (s1 & s2) - (s2 & s3) - (s1 & s3)
print(*sorted(s))
