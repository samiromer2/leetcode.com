from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        pos = defaultdict(list)
        res = [0] * len(nums)

        for i, v in enumerate(nums):
            pos[v].append(i)

        for arr in pos.values():
            n = len(arr)

            prefix = [0] * n
            prefix[0] = arr[0]

            for i in range(1, n):
                prefix[i] = prefix[i - 1] + arr[i]

            for i in range(n):
                current = arr[i]

                left_count = i
                left_sum = prefix[i - 1] if i > 0 else 0
                left_cost = current * left_count - left_sum

                right_count = n - i - 1
                right_sum = prefix[n - 1] - prefix[i]
                right_cost = right_sum - current * right_count

                res[current] = left_cost + right_cost

        return res