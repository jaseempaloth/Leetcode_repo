# 527. Patients With a Condition
import pandas as pd
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[patients['conditions'].str.contains('DIAB1', case=False)]
    return df
    

