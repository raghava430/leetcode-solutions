class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # i, not i + 1, because we can reuse the same number
                backtrack(i, path, total + candidates[i])

                path.pop()

        backtrack(0, [], 0)
        return res