class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)
        nums.sort()
        closest = 100000
        for index in range(len_nums - 2):
            left = index + 1
            right = len_nums - 1
            while left != right:
                summa = nums[index] + nums[left] + nums[right]
                if abs(summa - target) < abs(closest - target):
                    closest = summa
                if summa > target:
                    right -= 1
                elif summa < target:
                    left += 1
                else:
                    return target
        return closest
