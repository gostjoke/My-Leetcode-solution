import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = (employees.groupby(by=["emp_id","event_day"]).sum().reset_index())[["event_day", "emp_id","total_time"]]
    employees = employees.rename(columns={"event_day":"day"})
    return employees
