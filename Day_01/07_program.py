#categories of functions
#based on arguments
#1:positional arguments
# def function1(num1,num2,num3,num4):
#     print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
# function1(10,20,30,40)
# function1(100,200,300,400)
# #2 keyword arguments
# def function2(num1,num2,num3,num4):
#     print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
# function2(num4=10,num1=20,num2=30,num3=40)

# #3 default arguments
# def function3(name,rollno,branch,collegename="GIETU"):
#     print(name,rollno,branch,collegename)

# function3("RAVIKUMAR",16,"ECE")

# function3("rahul",8,"ECE")

#4 variable no of arguments
def function4(*var):
     for i in var:
         print(i,end=' ')

function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,60)
print()

def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
        print(sum1)
        return(sum1)
add(10,20)
print()

def add (*var):
    sum1=0
    for i in var:
        sum1=sum1+i
        print(sum1)
        return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))