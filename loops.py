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


