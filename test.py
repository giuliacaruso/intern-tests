import pandas as pd
import re

def clean_dataframe(df):
    for col in df.columns:
        
        if df[col].dtype==object:   #check if column type is string
            
            df[col] = df[col].str.strip()
            
            df[col] = [re.sub(r'\W+', '', x) for x in df[col]]   #remove special characters in each element of the column

        df[col].fillna('', inplace=True)
    
    return df

