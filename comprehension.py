numbers=[]
for x in range(5):
    numbers.append(x)
print(numbers)
   

   # isko ek line ma bhi kar sakta hay   (COMPREHENSION LIST) , SYNTAX:   [expression for variable in iterable]  
   # expression= vo value jo list ka andar jai gein
numbers=[x for x in range(5)]
print(numbers)
# now let's change the expression jisna list ka andar jana ha 

numbers=[x for x in range(5)]
print(numbers)




         # lets differentiate between list comprehension and normal method

squares=[]
for x in range(5):
    squares.append(x*x)
print(squares)


squares=[x*x for x in range(5)]
print(squares)


 


words="python"
letters=[letter for letter in words]
print(letters)



names=["ali","ahmed","usman"]
capitilize=[name.upper() for name in names]
print(capitilize)





# using condition in comprehension list

even=[x for x in range(10) if x%2==0]
print (even)






   # simple:
pairs=[]

for x in [1,2]:
    for y in [10,20]:
        pairs.append((x,y))


        # comprehesnion:
pairs=[(x,y) for x in [1,2] for y in [10,20]]







word="education"
vowel="aeiou"
found_vowel=[char for char in word.lower() if char in vowel]
print(found_vowel)




list=["EVEN" if x%2==0 else "ODD" for x in range(1,11)]
print(list)