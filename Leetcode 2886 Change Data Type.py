"""
10/14/2023
"""
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students[["grade"]].astype(int)
    return students
