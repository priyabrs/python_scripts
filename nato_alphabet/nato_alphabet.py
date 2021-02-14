student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
nato_alphabet_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {}
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
for _index, row in nato_alphabet_df.iterrows():
    nato_alphabet_dict[row.letter] = row.code
print(nato_alphabet_dict)

