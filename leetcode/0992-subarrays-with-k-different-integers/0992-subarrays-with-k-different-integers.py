class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def do(k):
            window = defaultdict(int)
            left = count = 0

            for right in range(n):
                window[nums[right]] += 1

                while len(window) > k:
                    window[nums[left]] -= 1
                    if not window[nums[left]]:
                        del window[nums[left]]

                    left += 1

                count += right - left + 1

            return count
            
        return do(k) - do(k - 1)

        