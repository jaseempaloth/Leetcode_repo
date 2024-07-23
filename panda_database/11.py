# 176. Second Highest Salary
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee[['salary']].rank(method='dense', ascending=False)
    second_highest = employee[employee['rank'] == 2]['salary']
    return pd.DataFrame({'SecondHighestSalary': [None if len(second_highest) == 0 else second_highest.iloc[0]]})
