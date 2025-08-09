# 20250808
import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    # 1e-6 to avoid 0
    queries["quality"] = queries["rating"]/queries["position"] + 1e-6
    queries["poor_query_percentage"] = (queries.rating < 3) * 100
    return queries.groupby("query_name").agg({'quality':'mean', 'poor_query_percentage':'mean'}).round(2).reset_index()
