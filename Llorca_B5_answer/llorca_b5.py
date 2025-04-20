import pandas as pd #type: ignore

df = pd.read_csv('Exam_Table.csv')

mean_count = df.loc[df["Scientific Name"] == "Pomacentrus adelus", ['Count']].mean()

output_df = pd.DataFrame({'Scientific Name' : "Pomacentrus adelus", 
                          'Mean Count' : mean_count})

output_df.to_csv('b1_output5.csv', index=False)