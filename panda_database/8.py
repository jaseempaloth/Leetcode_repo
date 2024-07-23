# 1517. Find Users With Valid E-Mails
import pandas as pd
def valid_email(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users['mail'].str.match(r'[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$')]
    return df