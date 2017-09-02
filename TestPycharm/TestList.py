
L = ['abc', [(1,2), ([3], 4), 5]]

print (L[1])
print (L[1][1])
print (L[1][1][0])
print (L[1][1][0][0])

X = [1, 2, 3]
M = ['A', X, 'B']
D = {'x':X, 'y':2}
print ("===before change===")
print (X)
print (M)
print (D)

X[1] = 'surprise'
print ("===after change===")
print (X)
print (M)
print (D)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print (L1 == L2)
print (L1 is L2)
L1 = [2,('B', 3)]
print (L1 == L2)
print (L1 is L2)

#test copy reference
C = [1, 2, 3]
E = ['X', C, 'y']
print(E)
#change reference, not the value
C = [0, 2, 3]
print(E)

C = [1, 2, 3]
E = ['X', C, 'y']
print(E)
#change value, not change reference
C[0] = 100
print(E)

C = [1, 2, 3]
#copy value
E = ['X', C[:], 'y']
print(E)
#change value, not change reference
C[0] = 100
print(E)

L3 = [4, 5, 6]
X = L3 * 4
Y = [L3] * 4
print(X)
print(Y)
L3[1] = 500
print(X)
print(Y)

L3 = [4, 5, 6]
X = L3 * 4
Y = [L3[:]] * 4
print(X)
print(Y)
L3[1] = 500
print(X)
print(Y)


