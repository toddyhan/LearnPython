
output = open("write",'w')
input =  open("data.txt",'r')
S = input.read()
print ("read: " + S)

input = open("data.txt",'r')
L = input.readlines()
print (L)

output.write(S)
output.close()
input.close()