def calculateparking(hour):
    amount =0
    price_before3hour=2000
    price_after3hour=1000
    price_max =10000
    
    if hour <= 3 :
      amount = price_before3hour*hour
    else:
        numafter_3hour =hour -3
        amount = (price_after3hour*numafter_3hour)+(price_before3hour*3)
    if amount> price_max:
        amount =price_max
    return amount   

amount=calculateparking(6)
print(amount)