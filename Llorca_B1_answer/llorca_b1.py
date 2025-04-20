import pandas as pd #type: ignore

df = pd.read_csv('Exam_Table.csv')

# filtered_interval = df[df['Interval'].str.contains('30-0', na=False)]

filtered_interval = df.loc[df['Interval'] == '30-0']

filtered_interval.to_csv('b1_output1.csv', index=False)

# C:/bio191/lab_exam_practice/Exam_Table.csv
# lab_exam_practice\Exam_Table.csv