class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1
        res = []

        for size in range(n, 0, -1):
            index = k // fact
            res.append(nums.pop(index))

            k %= fact

            if size > 1:
                fact //= size - 1

        return "".join(res)