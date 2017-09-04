

def intersect(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res

x1 = [1,2,3,4]
x2 = [2,3,4,5,6]
print(intersect(x1,x2))

y1 = [1,2,3,4]
y2 = (2,3,4)
print(intersect(y1, y2))

def changer(x, y):
    x = 2
    y[0] = 'spam'

X = 1
L = [1,2]
print("X: ", X)
print("L:", L)
changer(X,L)
print("after changer: ")
print("X: ", X)
print("L:", L)
