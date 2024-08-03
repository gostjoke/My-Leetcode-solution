# 08/03/2024
import pandas as pd

def sum_daily_odd_even(df: pd.DataFrame) -> pd.DataFrame:
    df_even = df[df["amount"]%2==0].groupby("transaction_date").sum().reset_index().rename(columns={"amount":"even_sum"})[["transaction_date", "even_sum"]]
    df_odd = df[df["amount"]%2==1].groupby("transaction_date").sum().reset_index().rename(columns={"amount":"odd_sum"})[["transaction_date", "odd_sum"]]   
    return pd.merge(df_odd, df_even, how="outer", on="transaction_date" ).fillna(0)
