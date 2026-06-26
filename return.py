def area_triangle(base,height):
    return base*height/2
area_a=area_triangle(5,4)  # spce =0 so its not the part of the function
area_b=area_triangle(5,6)
sum=area_a+area_b
print("The sum of both areas is:",str(sum))


# ANOTHER EXAMPLE OF MULTIPLE RETURNS

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60

    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)

print(hours, minutes, seconds)
