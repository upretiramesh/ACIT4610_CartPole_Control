import random
import os
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
import time
# start = time.perf_counter()
# model_path = './models/'
# result_path = './result/'
#
# if not os.path.exists(model_path):
#     os.mkdir(model_path)
# else:
#     for file in os.listdir(model_path):
#         os.remove(model_path+file)
# #
from datetime import datetime
# outfile = open(model_path+'best_rule_date_{}'.format(datetime.now().strftime("%D").replace('/','_')), 'wb')
# pickle.dump(ll3,outfile)
# outfile.close()
# outfile = open(model_path+'best_rule_date_{}'.format(datetime.now().strftime("%D").replace('/','_')), 'rb')
# df = pickle.load(outfile)
# print(df)
#
# #
# ll3 = [1,1,1,1,1,1,1,1,1,1,1]
# outfile = open(model_path+'best_rule_date_{}'.format(datetime.now().strftime("%D").replace('/','_')), 'wb')
# pickle.dump(ll3,outfile)
# outfile.close()
# outfile = open(model_path+'best_rule_date_{}'.format(datetime.now().strftime("%D").replace('/','_')), 'rb')
# df = pickle.load(outfile)
# print(df)

# import config
# config.NEIGHBOURS = 10
# print(config.NEIGHBOURS)

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

#######################################
# x = 0.17267239093780518/2
# for i in range(10, 0, -1):
#     print(x, i, x/i)
import time
# start = time.perf_counter()
# model_path = './models/'
# result_path = './result/'
#
# if not os.path.exists(model_path):
#     os.mkdir(model_path)
# else:
#     for file in os.listdir(model_path):
#         os.remove(model_path+file)
# #
from datetime import datetime
# outfile = open(model_path+'best_rule_date_{}'.format(datetime.now().strftime("%D").replace('/','_')), 'wb')
# pickle.dump(ll3,outfile)
# outfile.close()
# outfile = open(model_path+'best_rule_date_{}'.format(datetime.now().strftime("%D").replace('/','_')), 'rb')
# df = pickle.load(outfile)
# print(df)
#
# #
# ll3 = [1,1,1,1,1,1,1,1,1,1,1]
# outfile = open(model_path+'best_rule_date_{}'.format(datetime.now().strftime("%D").replace('/','_')), 'wb')
# pickle.dump(ll3,outfile)
# outfile.close()
# outfile = open(model_path+'best_rule_date_{}'.format(datetime.now().strftime("%D").replace('/','_')), 'rb')
# df = pickle.load(outfile)
# print(df)

# import config
# config.NEIGHBOURS = 10
# print(config.NEIGHBOURS)


# Action:
# 0 : "push cart to the left"
# 1 : "push cart to the right"
# Observation:
# {
# cart position, cart velocity, pole angle, pole velocity
# }
#
# # print('## observation high and low limit')
# # print(env.observation_space)
# print(env.observation_space.high)
# print(env.observation_space.low)
# #
# # print('## action space ##')
# # print(env.action_space)
#
# game = defaultdict(list)
#
# for i_episode in range(20):
#     observation = env.reset()
#     for t in range(1000):
#         env.render()
#         if observation[3] < -0.7003292: #PV
#             action = 0
#         elif observation[3] > 0.7003292:
#             action = 1
#         elif observation[2] < -0.11003292: #PA
#             action = 0
#         elif observation[2] > 0.11003292:
#             action = 1
#         else:
#             action = env.action_space.sample()
#
#         game['aa'].append(action)
#         # print(observation, action)
#         observation, reward, done, info = env.step(action)
#
#         for x, y in zip(['cp', 'cv', 'pa', 'pv'], observation):
#             game[x].append(y)
#
#         if done:
#             print('####### Finished ############')
#             print("Episode finished after {} timesteps".format(t+1))
#             print('################################################3')
#             break
# env.close()
# #
# df = pd.DataFrame(game)
# df.astype(dtype=np.float64)
#
#
# print('## describe ##')
# # print(df.describe())
#
# print('## correlation ##')
# print(df.corr())
#
# print('##################################')
# print('CP: ', df.cp.min(), df.cp.max())
# print('CV: ', df.cv.min(), df.cv.max())
# print('PA: ', df.pa.min(), df.pa.max())
# print('PV: ', df.pv.min(), df.pv.max())
# print('#######################################')