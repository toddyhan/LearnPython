

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

def changer_copy(x, y):
    x = 2
    y = y[:]
    y[0] = 'spam'
x_copy = 1
y_copy = [1,2]
changer_copy(x_copy,y_copy)
print ("x_copy: ", x_copy)
print ("y_copy:", y_copy)

def ref_value(x, y, name):
    print ("x: ", x)
    print ("y: ", y)
    print ("name: ", name)
name = 6
ref_value(name=100, x=200, y=300)

def printargs(*args):
    print(args)
printargs(1,'aa')

def func(spam, eggs, toast=0, ham=0):
    print(spam, eggs, toast, ham)
func(1,2)
func(1,ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1,2,3,4)


def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

print(intersect('SPAM', 'SCAM', 'SMDCD'))