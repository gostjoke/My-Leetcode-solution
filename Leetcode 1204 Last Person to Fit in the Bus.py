# python verson XD
import pandas as pd

def last_passenger(df: pd.DataFrame) -> pd.DataFrame:
    df.sort_values(by="turn", inplace =True)

    total_weight = 0
    df_len = len(df)-1
    last_person = ""
    for ind, rows in df.iterrows():
        total_weight += rows["weight"]
        if total_weight == 1000:
            df = pd.DataFrame({"person_name":[rows["person_name"]]})
            return df
        elif total_weight > 1000:
            df = pd.DataFrame({"person_name":[last_person]})
            return df

        elif ind == df_len: 
            df = pd.DataFrame({"person_name":[rows["person_name"]]})
            return df
            
        last_person = rows["person_name"]
