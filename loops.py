"""Common errors in Loops
If you get an error message on a loop or it appears to hang, your debugging checklist should include the following checks:
Failure to initialize variables. Make sure all the variables used in the loop’s condition are initialized before the loop.
Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables. You can often prevent an infinite loop by using the break keyword or by adding end criteria to the condition part of the while loop."""




x=0
while x<5:
   print("not reached there,x=",str(x))
   x=x+1
print("x=",str(x))





def attempts(n):
   x=0  
   while x<n:
      print("Attempt:",str(x))
      x+=1
   print("done")
   
attempts(5)







"""while my_variable<10:  # its not defined so it will give error lets fix it 
     
     print("hello")
     my_variable+=1"""""

my_variable=5
while my_variable<10:
   print("hello")
   my_variable+=1









sum=0
x=1
while x<10:
   sum=sum+x
   x=x+1

product=1
while x<10:  # as the value of x is already ten from last sum loop so this loop wont run and the pruct will remain 1 but if we wanna run it then redefine x=0 again here
   product=product*x
   x=x+1

print(sum,product)









"""while x%2==0:
   x=x/2   # this will give an infinite bcz if vzlue =0 the loop never stops to solve this put condition :
 


 #if x!=0:  
   while x%2==0:
      x=x/2

      #OR:

while x!=0 and x%2==0:
   x=x/2"""










def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n=n+1

print_range(1, 5)






       # FOR LOOP
for x in range(5): # range of numbers will start from 0 by default and the range of number will be one less than the given value
   print(x)          #range(stop)





product=1
for n in range(1,10):     #range(start,stop)
   product=product*n
print(product)




friends =['taylor','alex','eli']
for friend in friends:
   print("Hi ",friend)






values=[0,5,4,33,5,55,3]
sum=0
length=0
for value in values:
   sum+=value
   length+=1
print("Total sum= ",str(sum),"-Average= ",str(sum/length))








def to_celcius(x):
   return(x-32)*5/9

for x in range(0,101,10):    # 0 lower limit hay or 101 end wali or hamna pehla kaha tha last element sa pichli value par rukta loop means 100 par ruka ga or 10 ka gap hoga
   print(x,to_celcius(x))  #range(start, stop, step) 









# This loop iterates on the value of the "n" variable in a range
# of 0 to 10 (the value of the end-of-range index 11 is excluded).
# The incremental value for the loop is 2. The print() function will 
# output the resulting value of "n" as the loop counts from 0 to 10 
# (end-of-range index 11) in incremental steps of 2. This is one 
# method that can be used in Python to print a list of even numbers.


for n in range(0,11,2):
    print(n)


# The loop should print 0, 2, 4, 6, 8, 10










            # NESTED FOR LOOP

for left in range(7):
   for right in range(left,7):
      print("[",str(left),"|"," ",str(right),"]",end=" ")
      print()













teams=['dragons','wolves','pandas','unicorns']
for home_team in teams:
   for away_team in teams:
      if home_team!=away_team:
         print(home_team ,"vs", away_team)









         # strings in for loop

greeting="hello"
for c in greeting:
   print("the character is:",c)
   