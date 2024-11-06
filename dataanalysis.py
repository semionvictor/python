import pandas as pd

# data = [20,30,40,50,60]

# df = pd.Series(data)
# print(df)


# data = {
#     "Name":["chiboy","man","stan","boy"],
#     "Age":[20,30,4,2]
# }


# df = pd.DataFrame(data)
# print(df)


df = pd.read_csv("fff.csv", encoding="ISO-8859-1")
# print(df.head())
# print(df.tail())



print(df.shape)
print(df.columns)