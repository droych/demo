import array as a

a = a.array('f',[1,2.0,3])
print(type(a))
for i in a:
    print(i,end=' ')

print(dir(a))
l = a.__sizeof__()
print(l)