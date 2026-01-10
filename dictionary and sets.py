#dictionary

dict1 = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(dict1)

info = {
    # 'KEY': 'VALUE'
    "age": 30,
    'city': 'Los Angeles'
}

print(info)

#methods
print('Dictionary Methods')
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get('name'))

#Sets
print('Sets')
set1 = {1,2,2,2,2,2,'hello','hello','python'}
set2 = set([3,4,5,5,5,5])
print(set1)
print(type(set1))
print(len(set1))
set1.add(3)
print(set1)
set1.remove('hello')
set1.discard('python')
print(set1) 
print(set1.pop())
print(set1.clear())
print(set1.union(set2))
