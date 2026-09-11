class Solution:
    def totalNumbers(self, digits):
        available = [0] * 10

        for digit in digits:
            available[digit] += 1

        ans = set()

        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            if a == b == c:
                if available[a] >= 3:
                    ans.add(num)

            elif a == b:
                if available[a] >= 2 and available[c] >= 1:
                    ans.add(num)

            elif a == c:
                if available[a] >= 2 and available[b] >= 1:
                    ans.add(num)

            elif b == c:
                if available[b] >= 2 and available[a] >= 1:
                    ans.add(num)

            else:
                if (available[a] >= 1 and
                    available[b] >= 1 and
                    available[c] >= 1):
                    ans.add(num)

        return len(ans)
        