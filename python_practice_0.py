# Data Types :
'''
1. int 
2. float
3. bool
4. str
5. list
6. tuple
7. set
8. dict
'''
#These are fundamental data types.

#Math Functions:

print(round(3.123456,2))
print(abs(-20))
print(sum((3,5)))
print(sum([1,2,3,4]))

#Dwvwloper Fundamentals:

''' Don't read the dictionary.'''

#Operator Precedence:
'''
1. ()
2. **
3. *,/
4. +,-

'''
#Complex: 
print(bin(5))
print(int('0b101',2))

#Variables :

a,b,c=1,2,3
print(a,b,c)

#Augmented assignment operator
a=5
a=a+2  #here we can write a+=2 , output will be same.
print(a)

#Strings:
'''
A string is simply piece of texts.
'''

print("Hi ! My name is Keshav.")

long_string='''WOW 
               O O
               ---'''
print(long_string)

#Addition of strings:
first_name= "Keshav"
middle_name="Raj"
last_name="Pandey"
full_name=first_name+' '+middle_name+' '+last_name

print(full_name)

#String Concatenation:
''' String concatenation only works with string.'''
print('Hello'+' '+'world')

#Type Conversion:
a=str(100)
b=int(a)
c=type(b)

print(c)

#Escape Sequence:
weather="Its \" still \" raining outside\nBut what are you doing here."
print(weather)

#Formatted Strings:
name='Keshav'
age=22
print('Hi'+' '+name+'!'+'you are '+str(age)+' years old.')

#Alternate Method- I

print(f'Hi {name}!you are {age} years old.')

#Alternate- II
print('Hi {0}!you are {1} years old.'.format(name,age))

#String Indexes:

selfish='01234567'
print(selfish[-1])
print(selfish[: :-1])
print(selfish[1:7])
'''
Strings are immutable, they can't be changed.
'''
#Built-In functions and actions:
'''
1. len()
2. upper()
3. lower()
4. capitalize()
5. find()
6. replace()

'''
quote="niKhIl SInGh"
print(quote.upper()) 
print(quote.lower())
print(quote.capitalize())
print(quote.find('hI')) #find gives the index at which the string is present.

quote_1='to be or not to be'
print(quote_1.replace('be','me'))
print(quote_1)   #The original string will not change because strings are immutable.

#Type Conversion:
#Write a python program to calculate the age.
birth_yr=int(input('Enter the year of birth:')) 
age=2023-birth_yr
print(f'You are {age} years old.')

#Developer Fundamental:
'''
Commenting your codes.
    Guidelines to commenting your code:
       1. Be concise and keep things simple.
       2. Add comments only when it is complex to understand.
'''
#Note: 
print('*'*10)