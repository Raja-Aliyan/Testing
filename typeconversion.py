#typeconversion(implicit or automatic conversion)
a=2
b=4.5
sum=a+b   #int -> float bcz its superior
print(sum)


"""a="2"
b=4.34
print(a+b)"""  #it will giver error  now to solve this we will use typecasting
  

           #TYPECASTING(only valid numbers will owrk only)

a="2"
b=1
c=int(a)
sum=b+c
print(sum)

# or
a=int("2")     # can convert in into any data type
b=3.43
print(type(a))
print(a+b)



a=str(3) # int to string
print(type(a))




base:int=5   #used annotation(:int) and its optional
height=45
area=(base*height)/2
print("the area is:",str(area))  #temporray time k lia string 
print(type(area))   #yeh float ho hoga

#if you want string then=
area=str(area)
print(type(area))


a="hello"
b=4
b=str(b)
print(a+b)
#OR
print(a+str(b))





print("2+2=" ,(2+2) )