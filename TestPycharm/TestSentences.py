
x = 'spamegg'

while x:
    print(x)
    x = x[1:]

a = 0; b = 10
while a < b:
    print(a)
    a = a + 1

y = 47
x = (int)(y / 2)
while x > 1:
    if y % x == 0:
        print(y, " has factor ", x)
        break
    x = x -1
else:
    print(y, " is prime")

s1 = "spam"
s2 = "sbam"
res = []
for x in s1:
    if x in s2:
        res.append(x)
print(res)