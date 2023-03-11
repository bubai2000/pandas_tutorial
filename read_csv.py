import pandas as pd
import os
import pdb

# Be careful while joining path because it's OS specific
df = pd.read_csv(os.path.join(os.getcwd()+r'/dataset/survey_results_public.csv'))

# pd.set_option('display.max_columns',85) mainly used in jupyter notebook
# print(df)

#test

print(df.shape) #size of dataframe in (row, column) format
info=df.info() #Return metadata info about dataframe
print(info)

print(df.head(7)) #head(<n>) returns first n rows default is 5
print(df.tail()) #tail(<n>) returns last n rows default is 5
