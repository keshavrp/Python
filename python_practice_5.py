#Functions:
def say_hello():
    print('Hello')
say_hello()

print(say_hello()) #This will return the location of say_hello().

#Arguments vs Parameters:

def say_hello(name,emoji):
    return f'Hello {name} {emoji}.'

print(say_hello('Keshav','😁'))
def test(a):
    '''
    Info: This function tests and prints parameter a
    '''
    print(a)

test('!!!')
help(test)

#Walrus operator:
a="helloooooooooo"
if ((n:=len(a))):
   print(f"Too long {n} elements.")

#Scope : What variables do i have access to ?
'''
b=1
def parent():
    b=10
    def confusion():
        return b

print(parent())
print(b)


#Global Keyword:
a=10
def func():
    global a
    print(a)
func()
'''

#Non-local keyword:

def outer():
    x='local'
    def inner():
        nonlocal x
        x='nonlocal'
        print("inner:",x)
    inner()
    print("outer:",x)
outer()