# LeetCode 70 - Climbing Stairs

## **Problem Statement**
You are climbing a staircase. It takes `n` steps to reach the top.  
Each time you can either climb `1` or `2` steps. In how many distinct ways can you reach the top?

---

## **Approach 1: Dynamic Programming (Bottom-Up)**
### **Explanation**
- Define `dp[i]` as the number of ways to reach step `i`.
- Base cases: `dp[1] = 1`, `dp[2] = 2`.
- Recurrence relation: `dp[i] = dp[i - 1] + dp[i - 2]` (sum of ways from the last two steps).
- Compute `dp[n]` iteratively.

### **Complexity Analysis**
- **Time Complexity:** `O(n)`, as we iterate once.
- **Space Complexity:** `O(n)`, as we store results in an array.

---

## **Approach 2: Optimized Space (Fibonacci Approach)**
### **Explanation**
- Instead of using an array, maintain only two variables: `prev2` and `prev1`.
- Iteratively compute the number of ways using `prev2 + prev1`.
- Only store the last two computed values to save space.

### **Complexity Analysis**
- **Time Complexity:** `O(n)`, as we iterate once.
- **Space Complexity:** `O(1)`, as we only use two variables.

---

## **Approach 3: Mathematical Formula (Binets’s Formula)**
### **Explanation**
- This problem follows the Fibonacci sequence.
- The number of ways to reach `n` is given by the formula:

  \[
  \frac{(1 + \sqrt{5})^n - (1 - \sqrt{5})^n}{2^n \times \sqrt{5}}
  \]

- This approach calculates the result in `O(log n)` using matrix exponentiation or direct formula computation.

### **Complexity Analysis**
- **Time Complexity:** `O(log n)`, due to fast exponentiation.
- **Space Complexity:** `O(1)`, as no extra space is used.

---

## **Summary**
- **DP Approach:** Simple and intuitive but uses extra space.
- **Optimized Space Approach:** Best for large inputs.
- **Mathematical Formula:** Fastest but involves floating-point precision.

---

## **Next Steps**
- Solve variations like "Min Cost Climbing Stairs".
- Implement using memoization to see space differences.