import random
# lst = [0, 1]
# prob = [0.8, 0.1]
# total = 0
# for _ in range(10000):
#     total += random.choices(lst, prob)[0]
# print(f'total time 1 occur in 10000 iteration is {total}')
#
# import numpy as np
# data = [np.random.choice([0,1]) for _ in range(100)]
# print(np.bincount(data))
#
# count1=0
# count0=0
# for d in data:
#     if d==0:
#         count0 +=1
#     else:
#         count1 +=1
# print('Count 0: ', count0, 'Count 1: ', count1)
# key = ''.join(str(i) for i in [1,1,1])
# print(key)
'''
lst1 = list(range(10))
lst2 = list(range(10,20))
print(lst1, lst2)
cross_over_id = random.sample(range(0,10), 3)
print('Bits to cross over: ', cross_over_id)
for id in cross_over_id:
    lst1[id], lst2[id] = lst2[id], lst1[id]
print(lst1, lst2)


ll = [1, 0, 0, 1, 0, 1, 1, 0] # 150   2+4+16+128
ll2 = [1, 0, 0, 1, 1, 0, 1, 0] # 154
ll3 = [0, 1, 1, 1, 0, 0, 1, 0] # 114

print(sum(2 ** (len(ll) - (c_idx + 1)) for c_idx in range(len(ll)) if ll[c_idx] == 1))
print(sum(2 ** (len(ll2) - (c_idx + 1)) for c_idx in range(len(ll2)) if ll2[c_idx] == 1))
print(sum(2 ** (len(ll3) - (c_idx + 1)) for c_idx in range(len(ll3)) if ll3[c_idx] == 1))


print(random.random())


##################################
CP:  -2.4249918460845947 2.4455254077911377
CV:  -2.541804075241089 2.4392290115356445
PA:  -0.1711875945329666 0.175487220287323
PV:  -1.0212944746017456 1.0190690755844116
#######################################
'''
# x = 0.17267239093780518/2
# for i in range(10, 0, -1):
#     print(x, i, x/i)

ob =0.5
for i in range(10, 0, -1):
    print(0 if -0.1 < -ob/i else 1, -ob/i)


if -1<-0.5:
    print('-1')
else:
    print('-0.5')