import pandas as pd

# df = pd.DataFrame(
#     {
#         "a":[14,51,6],
#         "b":[72,8,72],
#         "c":[100,11,12]
#     }, index=[1,2,3]
# )
df = pd.DataFrame(
    [[14,51,6],
     [72,8,72],
     [100,11,12]],
    index=[1,2,3], columns=["a","b","c"])
print(df)
