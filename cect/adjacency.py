import pandas as pd

df = pd.read_excel('cect/data/CElegansNeuronTables.xls')
df = df.iloc[:, :-1]
df = df.drop("Type", axis = 1)
am = pd.crosstab(df["Origin"],df["Target"])
print(am)



