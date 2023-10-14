"""
10/14/2023
"""

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna(0)
