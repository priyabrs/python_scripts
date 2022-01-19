import pandas as pd

squirrel_data_df = pd.read_csv('2018_cp_squirrel_data.csv')
sq_dict = squirrel_data_df['Primary Fur Color'].value_counts().to_dict()
df= pd.DataFrame(sq_dict.items(), columns=['color', 'count'])
df.to_csv('squirrel_count_by_color.csv')
# .to_csv('./100 Days/python_scripts/squirrel_data_analysis/squirrel_count_by_color.csv'))