# **Maximum Square - Solution Approaches**

## **Problem Statement**
Given a binary matrix consisting of `0s` and `1s`, find the largest square containing only `1s` and return its area.

---

## **Approach 1: Dynamic Programming (2D Table)**
### **Idea**
- A `dp` table is maintained where each entry represents the **largest square ending at that position**.
- If the cell contains `1`, the square size is determined by taking the **minimum of the three adjacent values** (left, top, diagonal-top-left) and adding `1`.
- The largest side found is squared to get the final area.

### **Complexity Analysis**
- **Time Complexity:** `O(M * N)`, where `M` is the number of rows and `N` is the number of columns.
- **Space Complexity:** `O(M * N)`, as we use a `dp` table of the same size as the matrix.

---

## **Approach 2: Space Optimized Dynamic Programming (1D Table)**
### **Idea**
- Instead of a `2D dp` table, a single row `dp` array is maintained to track results.
- A variable (`prev`) is used to store the previous diagonal value.
- This reduces **space complexity** while maintaining the same **time complexity**.

### **Complexity Analysis**
- **Time Complexity:** `O(M * N)`, as we still iterate through all elements.
- **Space Complexity:** `O(N)`, since only a single row of `dp` is stored.

---

## **Approach 3: Brute Force**
### **Idea**
- Iterate over each `1` and try to expand a square from that position.
- Check all elements within the expanding square to ensure they are `1`.
- This approach is **inefficient** but demonstrates the core concept.

### **Complexity Analysis**
- **Time Complexity:** `O((M*N)^2)`, as checking for each square results in quadratic time complexity.
- **Space Complexity:** `O(1)`, as no extra storage is used beyond variables.

---

## **Comparison of Approaches**
| Approach | Time Complexity | Space Complexity | Notes |
|----------|---------------|----------------|------------|
| **Brute Force** | `O((M*N)^2)` | `O(1)` | Slow, inefficient for large inputs |
| **2D DP** | `O(M*N)` | `O(M*N)` | Simple to implement but uses extra space |
| **1D DP** | `O(M*N)` | `O(N)` | Most optimized, saves space |

---

## **Final Thoughts**
- **2D DP** is straightforward but requires extra memory.
- **1D DP** is preferred in memory-constrained environments.
- **Brute Force** is useful for conceptual understanding but should be avoided in practical applications.

---

## **References**
- Dynamic Programming principles
- LeetCode Problem: Maximum Square (LC #221)
