import pandas as pd #type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()

col_list = df.columns.to_list()
index_list = df.index.to_list()
# print(index_list)

data_dict = {index_list[0] + 1 : col_list}

for i in range(len(index_list)):
    list_to_add = df.values[i]
    data_dict[i + 2] = list_to_add

print(data_dict)

output_df = pd.DataFrame(data_dict)

output_df.to_csv('b1_output7.csv', index=False)