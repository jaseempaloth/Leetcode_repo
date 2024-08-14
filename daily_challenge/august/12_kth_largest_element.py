# 703. Kth Largest Element in a Stream
# Topics: Tree, Design ,Binary Search Tree ,Heap (Priority Queue) ,Binary Tree, Data Stream

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
        self.nums = self.nums[-k:]  
        self.nums.sort()
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort()
        elif val > self.nums[0]:
            self.nums[0] = val
            self.nums.sort()
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

