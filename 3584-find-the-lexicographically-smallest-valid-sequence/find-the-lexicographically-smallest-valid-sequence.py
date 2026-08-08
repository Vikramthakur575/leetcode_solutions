class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        m = len(word2)

        last_pos = [-1] * m

        k = m - 1

        for idx, char in reversed(list(enumerate(word1))):

            if k >= 0 and char == word2[k]:
                last_pos[k] = idx
                k -= 1

        k = 0
        changed = 0

        result = []

        for idx, char in enumerate(word1):

            if k < m:

                if (
                    char == word2[k]
                    or (
                        changed == 0
                        and (
                            k == m - 1
                            or idx + 1 <= last_pos[k + 1]
                        )
                    )
                ):

                    if char != word2[k]:
                        changed = 1

                    result.append(idx)
                    k += 1

        return result if k == m else []