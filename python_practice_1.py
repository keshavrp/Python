#List: 
amazon_cart=['notebook','sunglass']
print(amazon_cart[1])
#List Slicing:
'''
Lists are mutable.
The idea of copying and modifying a list.
'''
#Copying:
amazon_cart=['notebooks','sunglasses','toys','grapes']
amazon_cart[0]='laptop'
new_cart=amazon_cart
new_cart[0]='gum'

print(new_cart)
print(amazon_cart)

#Modifying: 
amazon_cart=['notebooks','sunglasses','toys','grapes']
amazon_cart[0]='laptop'
new_cart=amazon_cart[:]
new_cart[0]='gum'

print(new_cart)
print(amazon_cart)

#Matrix:
matrix=[[1,5,1],[0,1,0],[1,0,1]]
print(matrix[0][1])

#List Methods: I
basket=[1,2,3,4,5]
print(len(basket))

#Adding objects in the lists:
# 1. append() Method:  Append adds the object in the last.
basket=[1,2,3,4,5]
new_basket=basket.append(100)
print(new_basket)
print(basket)

# 2. insert() Method: Insert adds the object on the index given.
object=[1,2,3,4,5,6]
new_object=object.insert(2,100)
print(new_object)
print(object)

# 3. extend() Method: Etend adds more than one object from the end of list.
test=[1,2,3,4,5]
new_test=test.extend([100,102,103])
print(new_test)
print(test)

#Removing objects from the list:
# 1. pop() Method: Pop removes the last object from the list if argument is not given.
# if argument is given then it removes the object which are at the index of the argument.
a=[1,2,3,4,5]
new_a=a.pop(2)
print(new_a)
print(a)

# 2. remove() Method: remove removes the given argument from the list.
b=[1,2,3,4,5]
new_b=b.remove(4)
print(new_b)
print(b)

# 3. clear() Method: It removes all the elements from the list.
c=[1,2,3,4,5]
new_c=c.clear()
print(new_c)
print(c)

#List Methods: II
list_5=[1,2,3,4,5]
print(list_5.index(2))
print(list_5.index(2,1,4))

# in keyword :
list_1=['a','b','c','d','e']
print('d' in list_1)
print('x' in list_1)

# count() Keyword: 
list_2=['a','b','d','c','d','e']
print(list_2.count('a'))
print(list_2.count('d'))

#List Methods: III
# sort() Method: 
list_3=['a','x','b','c','d','e','d']
list_3.sort()
print(list_3)
print(sorted(list_3))

# reverse Method: 
list_4=['a','x','b','c','d','e','d']
list_4.sort()
list_4.reverse()
print(list_4)

#Common list patterns:
# 1. range() : 

print(list(range(1,100)))

# 2. join() : 
sentence='!'
new_sentence=sentence.join(['Hi','my','name','is','keshav'])
print(new_sentence)

#List unpacking:
a,b,c,*other, d=[1,2,3,4,5,6,7]
print(a,b,c,other,d)

#None : 
weapon=None
print(weapon)