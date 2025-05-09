import sys
from typing import List

class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        def popcount(num):
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
            return count

        fact = [1] * (M + 1)
        inv_fact = [1] * (M + 1)
        for i in range(1, M + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        if M >= 0 and fact[M] != 0:
            inv_fact[M] = pow(fact[M], MOD - 2, MOD)
        elif M == 0:
            inv_fact[0] = 1

        for i in range(M - 1, -1, -1):
            if (i + 1) <= M:
                inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        if M == K:
            if M > n:
                return 0

            dp_poly = [0] * (M + 1)
            dp_poly[0] = 1

            for i in range(n):
                num_val = nums[i]
                for j in range(M, 0, -1):
                    dp_poly[j] = (dp_poly[j] + dp_poly[j - 1] * num_val) % MOD

            sum_of_prods_combinations = dp_poly[M]
            result = (fact[M] * sum_of_prods_combinations) % MOD
            return result

        dp = [[{} for _ in range(M + 1)] for _ in range(M + 1)]
        dp[0][0] = {0: 1}

        for i in range(n):
            num_val = nums[i]
            next_dp = [[{} for _ in range(M + 1)] for _ in range(M + 1)]
            num_powers = [1] * (M + 1)
            for p in range(1, M + 1):
                num_powers[p] = (num_powers[p - 1] * num_val) % MOD

            for j_prev in range(M + 1):
                for carry_prev in range(M + 1):
                    if not dp[j_prev][carry_prev]:
                        continue
                    for count_i in range(M - j_prev + 1):
                        j = j_prev + count_i
                        current_sum = count_i + carry_prev
                        current_bit = current_sum % 2
                        new_carry = current_sum // 2
                        if new_carry <= M:
                            factor = (num_powers[count_i] * inv_fact[count_i]) % MOD
                            for bits_prev, value_prev in dp[j_prev][carry_prev].items():
                                bits = bits_prev + current_bit
                                term_val = (value_prev * factor) % MOD
                                target_map = next_dp[j][new_carry]
                                current_val = target_map.get(bits, 0)
                                target_map[bits] = (current_val + term_val) % MOD

            dp = next_dp

        result = 0
        m_fact = fact[M]
        for final_carry in range(M + 1):
            if not dp[M][final_carry]:
                continue
            rem_bits = popcount(final_carry)
            for bits_at_n, value in dp[M][final_carry].items():
                total_bits = bits_at_n + rem_bits
                if total_bits == K:
                    final_term = (value * m_fact) % MOD
                    result = (result + final_term) % MOD

        return result
