#Conditional Logic :
# if condition1 :
#     print(" ")
# elif condition2 :
#     print(" ")
# else :
#     print(" ")

#Identation: A deep recess or notch on the edge or surface of something.

#Ternary Operator: Ternary operator also called conditional expression.
is_friend=False 

can_message="message allowed" if is_friend else "not allowed to message."
print(can_message)

#Short circuiting 
'''By short circuiting , we mean the stoppage of execution of the boolean operation if the truth value of expression has been determined already.'''

#Logical operators:

# is vs ==:

print(True==1)
print(''==1)
print([]==1)
print(10==10.00)
print([]==[])

print(end="\n")

print(True is True)
print('1' is '1')
print([] is [])
print(10 is 10)
print([1,2,3] is [1,2,3])

'''Because strings and the lists are data structures.'''

print(end="\n")
#For loops :
for item in "keshav":
    print(item)
print(end='\n')
'''An iterator is an object that contains a countable number of values.'''

#Iterable :
'''String,list,tuple,dictionary,set etc..'''

#range():

for x in range(2):
    print('email')

for i in range(10,0,-2):
    print(i)

#Enumerate():
for j,char in enumerate((1,2,3)):
    print(j,char)

#Exercise: Print index of 50. 
for k,l in enumerate(list(range(100))):
    if l==50:
        print(f'Index of 50 is:{k}')

# while looops :
m=0
while m<50:
    print(m)
    break

while m<50:
    print(m)
    m=m+1
else:
    print("all done")

#The else block will only execute if there is not a break.

#Our first GUI(Graphical User Interface):

picture=[[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]

fill="*"
empty=" "

for rows in picture:
    for pixel in rows:
        if pixel==0:
            print(empty,end=' ')
        else:
            print(fill,end=" ")
    print(" ")
