class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        freq.sort(reverse=True)

        pushes = 0

        for i, f in enumerate(freq):
            if f == 0:
                break

            cost = i // 8 + 1

            pushes += f * cost

        return pushes
        