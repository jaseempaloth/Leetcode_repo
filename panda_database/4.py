# 1148. Article Views I

import pandas0 as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    article_views_df = views[(views['author_id'] == views['viewer_id'])]
    article_views_df = article_views_df[['author_id']].drop_duplicates()
    article_views_df = article_views_df.sort_values(by=['author_id'])
    return article_views_df.rename(columns={'author_id': 'id'})

# Sample data
data = {
    'author_id': [1, 2, 1, 3, 2, 3],
    'viewer_id': [1, 2, 3, 3, 2, 1]
}

# Create DataFrame
views_df = pd.DataFrame(data)

# Print the result of the function call
print(article_views(views_df))

