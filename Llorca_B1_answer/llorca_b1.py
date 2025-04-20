import pandas as pd #type: ignore

df = pd.read_csv('Exam_Table.csv')

filtered_interval = df.loc[df['Interval'] == '30-0']

filtered_interval.to_csv('b1_output1.csv', index=False)