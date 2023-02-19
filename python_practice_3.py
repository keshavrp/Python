#Tuples : 
'''Tuples are like lists but unlike lists we cannot modify them.Faster than list.'''

my_tuple=(1,2,3,4,5)
new_tuple=my_tuple[1:2]
print(new_tuple)

#Tuples Unpacking :
x,y,z,*other=(1,2,3,4,5)
print(x,y,z,other)

#Tuple Methods:

'''Python has two built-in methods that you can use on the tuple.'''

# 1. count() : Returns the number of times a specified value occurs in a tuple.
# 2. index() : Searches the tuple for a specified value and returns the position of where it was found.

# Sets: 
my_set={1,2,3,2,3,5,6,7,4,5}
print(my_set)
# In a set everything has to be unique.

set_1={1,2,3,4,5}
set_1.add(100)
set_1.add(2)

print(set_1)

#Conveting a list in to a set and vice-versa:
my_list=[1,2,3,4,2,5]
print(set(my_list))

print(list(my_set))

#Set does not support indexing.

print(len(my_set))

#Set Methods: 
'''
The methods which are used for sets are :
1. .difference()
2. .difference_update()
3. .union()
4. .intersection()
5. .issubset()
6. .issuperset()
7. isdisjoint()
'''
