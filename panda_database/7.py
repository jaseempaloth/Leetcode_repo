# 1667. Fix Names in a Table
import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users.name = users.name.str.capitalize()
    return users.sort_values(by='user_id')


# example

data = {
    'user_id': [2, 1, 4, 3],  # Unique identifier for each user
    'name': ['john doe', 'JANE DOE', 'ALICE jones', 'bob smith']
    # Usernames with some inconsistencies in capitalization or spacing
}
users = pd.DataFrame(data)
fixed_name = fix_names(users)
print(fixed_name)
