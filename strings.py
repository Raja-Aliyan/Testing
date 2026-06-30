str1="python"
str2='language'    # can write in  '' or "" or """ """
print(str1+str2)      # this is called concatenating

#str3="learning'        
     # it will give an syntax error

print("example"*3)
print(len("00000000000000 cat"))



name = "Jaylen"
print(name[1])



text = "Random string with a lot of characters"
print(text[-1])
print(text[-2])




color = "Orange"
color[1:4]




fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])











"""
message = "A kong string with a silly typo"
message[2] = "l" 
"""
#This will throw an error ( str object does not support item assignemnt)     bcz pyhton strings are immutable 






    # (,) use karna sa vo strings ko as it it neecha print kardega
    # (+) use karna sa vo dono strings ko combine kardain ga


message="A kong string with a silly typo"
new_message=message[0:2]+"L"+ message[3:]
print(new_message)





      # this is a concept of memeory managment
message = "This is a new message"
print(message)
message = "And another one"
print(message)






             # index function index batata hay ka koi variable kis index par para hay 



pets="Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))   
print(pets.index("Dog"))
print(pets.index("s"))













pets="Cats & Dogs"
print("Dragons" in pets)
print("Cats" in pets)









def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email            





animals = "lions tigers and bears"
print(animals.index("bears"))



animals = "lions tigers and bears"
print("tigers" in animals)






print("Mountains".upper())
print("Mountains".lower())








                   # STRIP METHOD ( string sa unwanted cheezo ya sapces ko remove karta hay lekin sirf start or end sa middle sa kuch change nai hota)


name="  hello   "
print(name.strip())
#agar sirf left sa remove karna hay to:
print(name.lstrip())
#agar right sa sirf karna ho to:
print(name.rstrip())


# agar specific chararcter remove karna hay to:
text="*** hello***"
print(text.strip("*"))
print(text.lstrip("*")) 


# agar multiple character ko remove karna ho to:
print(text.strip("*o")) # yaha par * and o 
    




                              # COUNT METHOD

message="The number of times e occurs in this string is 4"
print(message.count("e"))





                        # isnumeric()  yeh check krta hay "Kya is string ke saare characters numeric (numbers) hain?"

number="12434"
print(number.isnumeric())
num="a2323"
print(num.isnumeric())
