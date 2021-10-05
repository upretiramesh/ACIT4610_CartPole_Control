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
neighbours = 3
match = [0,0,1]

ss = ''.join(str(i) for i in match)
print(ss)
# print(bin(ss))

rule_ix = sum(2**(neighbours-(c_idx+1)) for c_idx in range(neighbours) if match[c_idx]==1)
print(rule_ix)