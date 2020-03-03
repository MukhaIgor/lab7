from random import randint

n = int(input('n = '))
a = {randint(1, 100) for i in range(n)}
a.add('!')
b = 0
for k in a:
    b += 1
    if k == '!':
        break
print('Кількість пробілів = ', b - 1)
print(a)
