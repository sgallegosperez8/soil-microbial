import pandas as pd
import re


#MAR282026
# edited metadata to correct format for qiime2 
#combined columns sample and id to one column with id "sample-id"
#create a row to include data type to meet qiime2 requirement 



n_data = pd.read_csv('Nachusa_16s_all_metadata_edited.csv')

n_data['sample-id'] = n_data['sample'] + " "+ n_data['ID'].astype(str)

n_data = n_data.drop(columns= ['ID','sample'])

n_data = n_data.set_index('sample-id').reset_index()

# Insert a new row at the top, str=categorical,float64=numerical, and sample-id=#q2:types

top_row={}
for col in n_data.columns:
    if n_data[col].dtype == 'str':
        top_row[col] = "categorical"
    elif n_data[col].dtype == 'float64':
        top_row[col] = "numerical"

top_row['sample-id'] = '#q2:types'

# Insert a new row at the top
top_row = pd.DataFrame([top_row])
df = pd.concat([top_row, n_data]).reset_index(drop=True)

df.to_csv('Nachusa_16s_all_metadata_edited2.csv', index=False)