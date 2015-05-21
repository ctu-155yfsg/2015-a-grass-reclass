import re

x = '150-210'

y = re.split('-', x)

a, b = y

print(a)
print(b)

c = []
c.append([a, b])
print(c)
