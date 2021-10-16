import pandas as pd

df = pd.read_csv('performance_mr1.csv')
gg = df.groupby(['generation'])['rule', 'avg'].agg({'avg': 'max'})
# print(gg.reset_index())
print(gg.columns)
print(gg[('avg', 'rule')].value_counts())
print(gg[gg[('avg', 'rule')]==214])