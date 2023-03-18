""" A traveler on a visit to India is in need of some Indian Rupees(INR) but he has money belonging to another currency.
He wants  to Know how much money he should provide in the currency he has, to get the specified amount in INR.
--> Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveller has.
--> The program should identify and display the amount the traveller should provide in  the currency he has, to get the specified amount in INR.
--> Note: Use the forex information provided in the table below for the calculation.
--> Consider that only the currency names mentioned in the table are valid.
For any invalid currency name, display -1.
CURRENCY:                                         EQUIVALENT OF 1.00 INR:
Euro                                                     0.01417
British Pound                                            0.0100
Australian Dollar                                        0.02140
Canadian Dollar                                          0.02027     """


def currencycal(AmountINR,cur):
    if cur=="Euro":
        print(AmountINR*0.01417)
    elif cur=="British Pound":
        print(AmountINR*0.0100)
    elif cur=="Australian Dollar":
        print(AmountINR*0.02140)
    elif cur=="Canadian Dollar":
        print(AmountINR*0.02027)
    else:
        print(-1)
currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Australian Dollar")
currencycal(300,"Canadian Dollar")

