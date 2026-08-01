class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        # Stores already solved subproblems
        memo = {}

        # Returns maximum score difference current player can achieve
        def dp(left, right):

            # Base case: only one number left
            if left == right:
                return nums[left]

            # Return stored answer if already computed
            if (left, right) in memo:
                return memo[(left, right)]

            # Choose left number
            take_left = nums[left] - dp(left + 1, right)

            # Choose right number
            take_right = nums[right] - dp(left, right - 1)

            # Store the better choice
            memo[(left, right)] = max(take_left, take_right)

            return memo[(left, right)]

        # Player 1 wins if difference is >= 0
        return dp(0, len(nums) - 1) >= 0