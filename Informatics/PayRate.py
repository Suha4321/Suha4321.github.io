hours = 40
if  type(hours) != int:
    print('error in datatype')
else:
    if hours <= 40 :
        pay = hours *10
        print(pay)
    else:
        pay = 40*10 + (rate-40)*15
        print(pay)
