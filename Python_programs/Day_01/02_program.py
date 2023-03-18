#Decision making statements
#read a number
#multiple 3-->
#multiple 5-->
#multiple 3 and 5
#else print invalid
number = int(input("Enter an integer number:"))
print(number,type(number))
if number%3==0 and number%5==0:
    print("Its a multiple of both")
elif number%5==0:
    print("Its a multiple of 5")
elif number%3==0:
    print("Its a multiple of 3")
else:
    print("invalid")
    
