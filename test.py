import pandas as pd
import re

def clean_dataframe(df):
    for col in df.columns:
        df[col] = df[col].str.strip()

        df[col] = re.sub(r'\W+', '', df[col])

        df[col].fillna('', inplace=True)
    
    return df

