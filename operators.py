                # arithmetic operators
"""a=5
b=4
sum=a+b
# or
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # always give answer in float
print(a%b)   #use to find remainder
print(a**b) #it means a power b """

                  #RELATIONAL/comparison OPERATORS(always returns true or false)
""" a=50
b=20
print(a==b) 
print(a!=b)  
print(a>=b)
print(a<=b)  """

           #ASSIGNMENT OPERATORS

"""num=10  #its a assigment too
num+=10
a=10
a-=4
b=10
b*=5
c=7
c/=2
d=10
d**=5

print(num)
print(a)
print(b)
print(b)
print(c)
print(d)"""


                 # LOGICAL OPERATORS(not,and,or)
 # NOT OPERATOR   real result ko invert kardega
a=40
b=10
print(not(a>b))
print(not True) 
print(not False)

#AND OPERATOR        jab dono  true hona to answer true aai ga
val1=False
val2=True
print(val1 and val2)
print("this:","yellow">"blue" and "purple">"red")

#OR OPERATOR  jab b koi ek trye ho to answer true hoga

val1=True
value2=False
print(val1 or val2)

print("OR OPERATOR:",(a==b) or (a>b))
print("AND OPERATOR:", (a==b) and (a>b))





                   # COMPARE THINGS

print(10>1)
print("cat"=="dog")
#print(1<"1")  # will give error
print(1=="1") #  no error










# The greater than > operator checks if the left string has a higher 
# Unicode value than the right string. If true, the Python interpreter
# returns a True result. Since W has a Unicode value of 87, and you can 
# easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. As this is true, Python will return a True 
# result.
print("Wednesday" > "Friday")
True
 
 
# The less than < operator checks if the left string has a lower 
# Unicode value than the right string. If you reference the Unicode 
# chart above, you can see that all lowercase letters have higher 
# Unicode values than uppercase letters. We can see that B has a 
# Unicode value of 66 and b has a Unicode value of 98. This 
# comparison is the same as 66 < 98, which is true. So, Python will 
# return a True result.
print("Brown" < "brown")
True


# If the strings have the same first few letters, the comparison will 
# cycle through each letter of each string, from left to right until it 
# finds two letters that have different Unicode values. In this example, 
# both strings share the initial substring "sun", but then have 
# different letters with different Unicode values in the fourth place 
# in each string. So, the fourth letters 'b' and 't' of the two
# strings are used for the comparison. Since 'b' does not have a higher
# Unicode value than 't', the comparison returns a False result.
print("sunbathe" > "suntan")
False


# If two identical strings are compared using the less than < comparison
# operator, this will produce a False result because they are equal.
print("Lima" < "Lima")
False


# This last example illustrates the result of trying to compare two
# items of different data types using the less than < operator. The 
# greater than > and less than operators < cannot be used to compare
# two different data types. 
#print("Five" < 6)

"""Error on line 1:
    print("Five" < 6)
TypeError: '<' not supported between instances of 'str' and 'int'"""











# Use the Unicode chart in Part 2 to determine if the Unicode values of 
# the first letters of each string are higher, lower, or equal to one
# another. 


var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
 
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)