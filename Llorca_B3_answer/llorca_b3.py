import pandas as pd #type: ignore

df = pd.read_csv('Exam_Table.csv')

unique_sci_name = df['Scientific Name'].dropna().drop_duplicates()

unique_sci_name.to_csv('b1_output3.csv', index=False)