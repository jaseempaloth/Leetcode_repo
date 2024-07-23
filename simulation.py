# 1701>Average Waiting Time
from typing import List

class Solution:
    def average_waiting_time(self, customers: List[tuple[int, int]]) -> float:
        current_time = 0
        total_time = 0

        for customer_arrival, customer_order in customers:
            if current_time > customer_arrival:
                total_time += current_time - customer_arrival
            else:
                current_time = customer_arrival
            total_time += customer_order
            current_time += customer_order

        return total_time / len(customers)
