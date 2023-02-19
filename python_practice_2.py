#Dictionaries: 
dictionary={
    'a':[1,2,3],
    'b':'hello',
    'x':True
}
my_list=[{
    'a':[1,2,3],
    'b':'hello',
    'x':True},
{
     'a':[4,5,6],
     'b':'hello',
     'c':True 
    }]

print(my_list[0]['a'][2])
print(dictionary['a'][1])
 #A dictionary keys always has to be immutable.

user={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}

print(user.get('age',55)) #If its already age is assigned to a different value then it will print the previous value which is assigned to it.

dict_1={
    '123':[1,2,3],
    '123':'hello'
}

print(dict_1['123'])

#Dictionary Methods: I
user_1={
    'basket':[1,2,3],
    'greet':'hello'
}

print(user.get('year'))

#Dictionary Methods: II

user_2=dict(name='keshav')
print(user_2)

# .keys() Method:

user={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}
print('age' in user.keys())
print('you' in user.keys())

# .values() Method:

user={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}

print('hello' in user.values())

# .items() Method:

user={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}

print(user.items())

# .clear() Method:

print(user.clear())
print(user)

# .copy() Method:
user_3={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}

user_4=user_3.copy()
print(user_3.clear())
print(user_4)

# .pop()/ .popitem() Method:
'''
.popitem(): Removes the last items from the dictionary.
.pop(): Removes the values of keys entered in .pop().
'''

user_5={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}

print(user_5.pop('age')) # Gives the values which is poped.
print(user_5)

print(user_5.popitem())

# .update() Method: 

user_6={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}

print(user_6.update({'age':50}))
print(user_6)

user_7={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}

print(user_7.update({'ages': 55}))
print(user_7)