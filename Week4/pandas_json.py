# import pandas as pd
#
# data = {
#     "Duration": {
#         "0": 60,
#         "1": 60,
#         "2": 60,
#         "3": 45,
#         "4": 45,
#         "5": 60
#     },
#     "Pulse": {
#         "0": 110,
#         "1": 117,
#         "2": 103,
#         "3": 109,
#         "4": 117,
#         "5": 102
#     },
#     "Maxpulse": {
#         "0": 130,
#         "1": 145,
#         "2": 135,
#         "3": 175,
#         "4": 148,
#         "5": 127
#     },
#     "Calories": {
#         "0": 409,
#         "1": 479,
#         "2": 340,
#         "3": 282,
#         "4": 406,
#         "5": 300
#     }
# }
#
# df = pd.DataFrame(data)
# # print(df.tail(2))
# # print(df.head(2))
# print(df.info())
import pandas
df = pandas.read_csv('test.csv')
# print(df)
# for x in df.index:
  # print(df.loc[x, 'AL'])
# print(df.corr())
# print(df.describe())
# print(df.mean())
# import matplotlib.pyplot as mathplotvar
# df.plot(kind="scatter", x='AT', y='BE')
# df['AT'].plot(kind='hist')
# mathplotvar.show()
# print(df)
df.fillna(0, inplace=True)
# print(df)
# print(df.fillna(0))
# df['AL'].fillna(100, inplace=True)
# print(df)
# df.loc[7, 'AL'] = 45
# print(df)
df.replace(': ', 0, inplace=True)
df.replace(':', 0, inplace=True)
# print(df.transpose())
print(df)
df.to_csv('test1.csv')