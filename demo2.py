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
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('performance.csv')

print(df[df.rule==106])

print(df.rule.value_counts())
