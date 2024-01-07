list=[]

for i in range(0,100):
    list.append(i)

def func(max_lookback,list,lookback):
    list=list[::-1]
    lb_list=[]
    for i in list:
        lb_list.append(list[lookback:max_lookback])
        lookback+=1
        max_lookback+=1
    return lb_list[::-1]

z=func(25,list,0)

print(z)


