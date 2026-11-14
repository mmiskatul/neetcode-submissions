class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_list =list(set(nums))
        if len(nums)>len(unique_list):
            return True
        return False