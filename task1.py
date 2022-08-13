#Create a Boolean variable named x
x = True
# Create an integer variable named y
y=3
 # Create a float variable named z
z=3.4
# Create a string variable names s
s="Abdallah EL Araby"
#Convert the int variable to float
a=2
float(a)
print(a)
#Can we convert the str to int ?
# yes we can if the str is number but if the the str is "abdalalh"

# Create a list of numbers from 1 to 5
lis=[1,2,3,4,5]

#Create a tuple from 10 to 15
tup=(10,11,12,13,14,15)
# Convert the list to tuple
lis_tuple=tuple(lis)

# Create a dict of 3 values
{"name" : "abdallah" , "age" :21 , "address" : "mansoura"}

# Can we use semi colon ; with python -- No
#● Python is interpreted or compiled ? interpreted

# What is the differences between low level & high level
#low language : is the machine language , It is tough to understand ,It is complex 
#high : very easy to human , It is simple

#What is the differences between = , ==
# the = is assignment with variable but === is cheek the conditon is true or false or is qutation .

# What do we mean by using != is not equal
'''
● What is the operator precedence
Multipication
Division 
Addition
Subtraction
''' 

#Create a variable x with value of 10
x = 10
x+=15
x /=15
x %= 3

#Print the exponent of 2,3
print(2**3)

#Divide 11 by 3 using python division
print(11/3)

# Can we divide 11 by 3 and get an integer number ?
print(11//3)

#Check if 10 is bigger than 15 or not

y = 15
if y > 15:
    print("true")
else :
    print("y is smaller than 15")

#In which cases we will use all
# if all conditon is true

#What is the differences between all , and
#No differences

#● What is the differences between any , or
#No differences

#What is the differences between if , elif
#we start with if for the firt condition
#on the other conditions we use elif or the elif بنعتبرها استثناء :D
#if all condition get false the else will be excuted

# Can we use more than one elif --- yes
#Can we use more than one else ---- No

#rite s simple ternary operator
print("True") if y>13 else print("false")

# in elif , python will check all the conditions no matter what ? 
#when condition come true it stop.
#in elif we use else for ... ?
#all condition false

'''
 if we have this list [2,4,6,8,10] :
○ check to see if 4 in this list or not
○ check to see if 4 and 6 in this list on not
○ check to see if 3 or 6 in this list
○ check to see if 2 , 4 and 5 in this list
'''


new_lis=[2,4,6,8,10]
if 4 in new_lis:
    print ("the number 4 Found")

if all ([4,6]) in new_lis:                             
    print ("two number found 4, 6")
if any ([3,6]) in new_lis:
    print ("number 3 or number 6 Found")
if any ([2,4,5]) in new_lis:
    print ("number 2 or number 4 or number 5 Found")
else :
    print ("number not Found")



















