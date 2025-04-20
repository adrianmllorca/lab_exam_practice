import pandas as pd #type: ignore

df = pd.read_csv('Exam_Table.csv')

filtered_genus = df.loc['Genus'] == '^St'

filtered_genus.to_csv('b1_output2.csv', index=False)