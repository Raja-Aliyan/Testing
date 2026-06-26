def hint_username(name):
    if len(name)<3:
     print("Invalid useranme") #it would be after if statmenet means there would be space(idented) like there's a space after funstion
    else:
       print("Valid username")
hint_username("a")
hint_username("Aliyan")


def is_even(number):
    if(number%2==0):
       return True
    else:
       return False
is_even(4)
is_even(3)





#else with if
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username:",username)
hint_username("raja")

            # or you can write like that too you can use elif

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username:",username)

hint_username("raja")
