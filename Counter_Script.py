from collections import Counter

filename = 'test10.txt'
txt2 = open(filename)
txt2.read()

txt3 = Counter(txt2)
txt1 = Counter('three four five')


val = sum(txt3.values())
val1 = sum(txt1.values())

print (val)
print (val1)
print (val + val1)
