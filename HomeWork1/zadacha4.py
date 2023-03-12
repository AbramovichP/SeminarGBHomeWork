"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""
def Minimum(a,b):
    min = None
    if a <= b:
        min = a
    else:
        min = b
    return min
def Maximum(a,b):
    max = None
    if a >= b:
        max = a
    else:
        max = b
    return max

n = int(input("n = "))
m = int(input("m = "))
k = int(input("k = "))
flag = False
min = Minimum(n,m)
max = Maximum(n,m)

if k == n or k == m:
    flag = True

for i in range(1, max):
    if i * min == k:
        flag = True
for i in range(1, min):
    if i * max == k:
        flag = True

if flag:
    print(f"{n} {m} {k} -> yes")
else:
    print(f"{n} {m} {k} -> no")

