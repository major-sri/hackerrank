def bonAppetit(bill, k, b):
    
    cost=0
    for x in range(0,len(bill)):
        if x!=k:
            cost+=bill[x]
        else:
            x+=1
    cost=cost/2
    if cost==b:
        print('Bon Appetit')
    else:
        d=int(abs(b-cost))
        print(d)
