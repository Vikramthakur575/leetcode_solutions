class Solution:

    def smallestNumber(self, num: str, t: int) -> str:

        # ---------------------------------------------------------
        # 1. Factor t into 2, 3, 5, 7
        # ---------------------------------------------------------

        need = [0, 0, 0, 0]

        for i, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                need[i] += 1
                t //= p

        # If t contains any other prime factor,
        # no digit 1..9 can satisfy it.
        if t != 1:
            return "-1"

        # ---------------------------------------------------------
        # Factor contribution of each digit
        #
        # (2, 3, 5, 7)
        # ---------------------------------------------------------

        factor = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        # ---------------------------------------------------------
        # 2. Minimum number of digits needed for a requirement
        # ---------------------------------------------------------

        def min_digits(req):

            a, b, c, d = req

            # 5 and 7 need one digit each
            result = c + d

            best = float("inf")

            # Try how many 6s we use.
            # 6 = 2 * 3
            for sixes in range(min(a, b) + 1):

                rem2 = a - sixes
                rem3 = b - sixes

                # 8 = 2^3
                digits2 = (rem2 + 2) // 3

                # 9 = 3^2
                digits3 = (rem3 + 1) // 2

                total = sixes + digits2 + digits3

                best = min(best, total)

            return result + best

        # ---------------------------------------------------------
        # 3. Can we satisfy req using at most slots digits?
        # ---------------------------------------------------------

        def can_make(req, slots):
            return min_digits(req) <= slots

        # ---------------------------------------------------------
        # 4. Build smallest possible suffix
        # ---------------------------------------------------------

        def build(req, length):

            ans = []

            for pos in range(length):

                left = length - pos - 1

                # IMPORTANT:
                # Only digits 1..9.
                # We never put zero in the answer.
                for d in range(1, 10):

                    f2, f3, f5, f7 = factor[d]

                    new_req = [
                        max(0, req[0] - f2),
                        max(0, req[1] - f3),
                        max(0, req[2] - f5),
                        max(0, req[3] - f7)
                    ]

                    if can_make(new_req, left):

                        ans.append(str(d))
                        req = new_req
                        break

            return ''.join(ans)

        n = len(num)

        # ---------------------------------------------------------
        # 5. Find first zero
        # ---------------------------------------------------------

        first_zero = num.find('0')

        # ---------------------------------------------------------
        # 6. Prefix factor counts
        #
        # prefix[i] = factors supplied by num[0:i]
        # ---------------------------------------------------------

        prefix = [[0, 0, 0, 0] for _ in range(n + 1)]

        for i in range(n):

            d = int(num[i])

            for j in range(4):
                prefix[i + 1][j] = prefix[i][j]

            if d != 0:

                for j in range(4):
                    prefix[i + 1][j] += factor[d][j]

        # ---------------------------------------------------------
        # 7. If num itself contains no zero and works,
        #    return it.
        # ---------------------------------------------------------

        if first_zero == -1:

            if all(
                prefix[n][j] >= need[j]
                for j in range(4)
            ):
                return num

        # ---------------------------------------------------------
        # 8. Make num larger
        #
        # IMPORTANT:
        #
        # If there is a zero at position z, we CANNOT change a
        # position after z while keeping the prefix unchanged,
        # because that would leave the zero in the answer.
        #
        # Therefore:
        #
        # maximum position we can modify =
        #     first_zero
        #
        # if there is no zero:
        #     n - 1
        # ---------------------------------------------------------

        if first_zero == -1:
            last_position = n - 1
        else:
            last_position = first_zero

        # Search from right to left.
        for i in range(last_position, -1, -1):

            current = int(num[i])

            # Factors supplied by the unchanged prefix.
            before = prefix[i]

            # Try the smallest digit greater than current.
            #
            # If current == 0:
            # this becomes 1,2,3,...9.
            for d in range(current + 1, 10):

                f2, f3, f5, f7 = factor[d]

                remaining = [
                    max(
                        0,
                        need[0] - before[0] - f2
                    ),
                    max(
                        0,
                        need[1] - before[1] - f3
                    ),
                    max(
                        0,
                        need[2] - before[2] - f5
                    ),
                    max(
                        0,
                        need[3] - before[3] - f7
                    )
                ]

                slots = n - i - 1

                if can_make(remaining, slots):

                    suffix = build(
                        remaining,
                        slots
                    )

                    return num[:i] + str(d) + suffix

        # ---------------------------------------------------------
        # 9. Same length is impossible.
        #
        # Build the smallest valid number with more digits.
        # ---------------------------------------------------------

        required = min_digits(need)

        length = max(n + 1, required)

        # Extra positions can be filled with 1s.
        extra = length - required

        return '1' * extra + build(need[:], required)