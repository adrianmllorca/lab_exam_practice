import pandas as pd #type: ignore

df = pd.read_csv('Exam_Table.csv')

unique_sci_name_df = df['Scientific Name'].dropna().drop_duplicates()
unique_sci_name_list = unique_sci_name_df.to_list()

mean_size_est_list = []
for species in unique_sci_name_list:
    mean_size_est = df.loc[df['Scientific Name'] == species, ['Size Est (cm)']].mean().to_string(name=False, dtype=False, index=False)
    mean_size_est_list.append(mean_size_est)

output_df = pd.DataFrame({'Scientific Name' : unique_sci_name_list,
                          'Mean_Size_Est' : mean_size_est_list})

output_df.to_csv('b1_output4.csv', index=False)