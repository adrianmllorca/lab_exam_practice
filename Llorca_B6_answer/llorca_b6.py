import pandas as pd #type: ignore

df = pd.read_csv('Exam_Table.csv')

df['HRID'] = df.Location.str.replace(', ', '-') + '-' + df.Site + '-' + df.Replicate.astype(str)

df.to_csv('b1_output6.csv', index=False)