class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                product = digit1 * digit2

                pos1 = i + j
                pos2 = i + j + 1

                total = product + res[pos2]

                res[pos2] = total % 10
                res[pos1] += total // 10

        # remove leading zeros
        result = ""
        for num in res:
            if not (len(result) == 0 and num == 0):
                result += str(num)

        return result