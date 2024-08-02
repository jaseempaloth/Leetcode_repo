# 586. Customer Placing the Largest Number of Orders
# data = [[1, 1], [2, 2], [3, 3], [4, 3]]
# orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_customer = orders.groupby('customer_number').size().reset_index(name='total_orders')
    order_customer = order_customer.sort_values('total_orders', ascending=False)
    final = order_customer.drop(['total_orders'], axis=1)
    return final.head(1)
    