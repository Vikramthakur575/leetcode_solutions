class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # We need C(n + k - 1, 2k)
        N = n + k - 1
        R = 2 * k

        # factorials
        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        # Fermat's Little Theorem:
        # inverse(x) = x^(MOD-2) mod MOD
        inv_fact = [1] * (N + 1)
        inv_fact[N] = pow(fact[N], MOD - 2, MOD)

        for i in range(N, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        return fact[N] * inv_fact[R] % MOD * inv_fact[N - R] % MOD