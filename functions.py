#there are many functions we have used before like str print and type 
# now we are going to see(defining) our own function

def greeting(name):
    print("welcome:",name)  #yeh function ka part hay kinka isma spaces hay 4 spaces jitni bhi ho sakti hay greater than 0
greeting("Ali")   # spce=0 yeh function ka part nai hay so yeh function ko call karain ga
greeting("Ahmed")
result=greeting("cristian")
print(result)   # it will give none(means things are empty or return nothing) bcz there no no return type in the function and it only prints when it is called directly or through variable as cristaian
greeting("amna")   

print("---NEW FUNCTION---")
def dept(name,department):
    print("welcome" ,name)
    print("you are a student of ",department)

dept("zara","cs")
dept("muiz","IT")




                    #ANOTHER EXAMPLE

name="kay"
number=len(name)*9
print("hello",name, "your lucky number is:",str(number))
name="cameron"
number=len(name)*9  #len() is tells us the total number of characters
print("hello",name," your lucky number is:",str(number))
  

  # now this code is not reuseable so we'll use function for it :

def lucky_number(name):
    number=len(name)*9
    print("hello",name," your lucky number is:",str(number))
# now call the function
lucky_number("james")
lucky_number("jordan")








def calculate(d):    # ts nor clear or self documented code 
    q=3.14
    z=q*(d**2)
    print(z)
calculate(5)
  

  # self documneted version of this code

def circle_area(radius):    # ts nor clear or self documented code 
    pi=3.14
    area=pi*(radius**2)
    print(area)
circle_area(5)
  

