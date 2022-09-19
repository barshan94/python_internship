#turple is immutable cannot insert,delete
#turple & list are the ordered collection
#turple
'''
book=('Harry potter','Major','Titanic','Red')
print(book)
print(book[1])
book1={'name':'bgb','height':'6 ft','mental':'no'}
print(book1)
print(book1['height'])
book2=['Bangla','English','Biology','Chemistry','Math']
print(book2)
print(book2[2])
book2.insert(2,'who')
print(book2)
book1.pop('name','bgb')
print(book1)
book1['height']=56
print(book1)
del book1['mental']
print(book1)
'''

'''
#slicing
a='Barshan'
b='Ghosh'
c='Bangladesh'
d='American International University Bangladesh'
print(a[-4:-1])
print(b[:])
print(c[:-4])
print(d[:-35])
print(d[-21:-10])

'''

'''
a='Barshan'
b='Ghosh'
c='Bangladesh'
d='American International University Bangladesh'

print(a[:-3:2])
print(a[:-4:-1])
print(b[-3:-5:-1])
print(b[:-4:-2])
print(c[::-2])
print(d[:-22:-1])
d='done'
print(d[:-1:2])

'''

