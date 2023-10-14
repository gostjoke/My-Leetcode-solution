"""
10/14/2023
"""
import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.sort_values("visited_on").groupby("visited_on")[["amount"]].sum()
    df = df.assign(amount = df.rolling("7D").sum(), average_amount = round(df.rolling("7D").sum()/7, 2))
    df = df.reset_index()

    df = df[df["visited_on"]>=(df["visited_on"][0]+ pd.Timedelta(days=6))]
    return df
