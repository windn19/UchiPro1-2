# a, b, c = map(int, input().split())
# m = a
# if m < b:
#     m = b
# if m < c:
#     m = c
# print(m)
#
# print(max(a, b, c))
a, b, c = map(int, input().split())
m = a
if a < b:
    if b < c:
        m = c
    else:
        m = b
print(m)