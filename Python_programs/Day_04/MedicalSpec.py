"""
The patient is stored in a list. The details of the medical specialists are stored in a dictionary as follows
{ "P": Pediatrics, "O":orthopedics, "E":ENT }
write a function to find the medical specialty visited by the maximum number of patients and
return the name of the speciality
Note: 1. Assume that there is always only one medical specialty which is visited by maximum number of patients.
      2. Perform case sensitive string comparison whereever necessary.

Sample Input                                     Expected Output
[101,P,102,O,302,P,305,P]
[101,O,102,O,302,P,305,E,401,O,656,O]
[101,O,102,E,302,P,305,P,401,E,656,O,987,E]
"""

medical_spec = {
    "P": "Pediatrics",
    "O": "Orthopedics",
    "E": "ENT"
}

# Data = input().split()
def find(Data):
    # max = 0
    # setKey = ''
    # for i in range(0,len(Data),2):
    #     if(Data[i] > max):
    #         max = Data[i]
    #         setKey = Data[i+1]
    # print(medical_spec[setKey])
    pc = Data.count('P')
    oc = Data.count('O')
    ec = Data.count('E')
    if(pc > ec and pc>0):
        print(medical_spec['P'])
    elif(ec > 0):
        print(medical_spec['E'])
    else:
        print(medical_spec['O'])

find([101, 'P',102,'O', 302, 'P', 305, 'P'])
find([101, 'O',102, 'O', 302, 'P', 305,'E', 401, 'O', 656, 'O'])
find([101, 'O',102, 'O', 302, 'P', 305,'E', 401, 'O', 656, 'O',987,'E'])