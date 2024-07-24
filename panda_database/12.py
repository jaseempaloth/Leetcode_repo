# 184. Department Highest Salary

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['sal_rank'] = employee.groupby('departmentId')['salary'].rank(ascending=False, method='min')
    employee_dept = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    employee_dept_filtered = employee_dept[employee_dept['sal_rank'] == 1]
    employee_dept_filtered = employee_dept_filtered.rename(columns={'name_y': 'Department', 'name_x': 'Employee'})
    return employee_dept_filtered[['Department', 'Employee', 'salary']]

                                                  
    