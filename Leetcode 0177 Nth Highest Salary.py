"""
10/15/2023
"""
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset='salary')
    employee = employee.sort_values(by=["salary"], ascending=False)
    employee = employee.rename(columns={'salary':f'getNthHighestSalary({N})'})
    employee = employee.iloc[:,[1]]

    if len(employee) < N:
        return pd.DataFrame({f'getNthHighestSalary({N})':nan}, index=[0])
    else:
        print(employee)
        return employee.iloc[[N-1]]
