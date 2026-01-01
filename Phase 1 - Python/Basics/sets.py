"""
Duplicate value are notr allowed in set.
Set is unorderd so print value is random sequence
"""

collection={1,2,5,"Namaste","Duniya",1,4,"Namaste"}

print(collection)
print(type(collection))
print(len(collection))

#empty set
collection1={} #this is dict not set
#correct way to create empty set
collection2 = set() #enpty set

print(type(collection1))
print(type(collection2))

#method of set
collection.add("Hello")
print(collection)

empty = set()

empty.add(1)
empty.add("Namaste")
print(empty)

empty.remove(1)
print(empty)

empty.clear()
print(empty)

alish={1,3,5,6,7,"World"}
print(alish.pop())
print(alish.pop())

print("Union and intersection Method")
set1={1,2,3}
set2={3,4,5}
#Union
print(set1.union(set2))
print(set1)
print(set2)

print(set1.intersection(set2))