# Minimum Path Sum

## Problem Statement
Given an `m x n` grid filled with non-negative integers, find a path from the top-left to the bottom-right, which minimizes the sum of all numbers along its path.  
You can only move **either down or right** at any point in time.

---

## Approaches

### **1️⃣ Dynamic Programming (Bottom-Up)**
- Define `dp[i][j]` as the minimum sum required to reach `(i, j)`.
- Transition formula: `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`
- Time Complexity: **O(m * n)**
- Space Complexity: **O(m * n)**

### **2️⃣ Space Optimized Dynamic Programming**
- Instead of `dp[m][n]`, we use a **1D array** of size `n`.
- Time Complexity: **O(m * n)**
- Space Complexity: **O(n)**

### **3️⃣ Recursion + Memoization**
- Use DFS to explore all paths and store results in a cache.
- Time Complexity: **O(m * n)**
- Space Complexity: **O(m * n) (recursive stack + cache)**

### **4️⃣ BFS with Priority Queue**
- Uses Dijkstra-like approach with a **min-heap**.
- Time Complexity: **O(m * n log(m * n))**
- Space Complexity: **O(m * n)**

---

## Key Takeaways
✅ **DP approach is the most optimal in terms of time complexity.**  
✅ **Using a 1D array significantly reduces space usage.**  
✅ **Recursive approach is easy to implement but has higher memory usage.**  
✅ **BFS works but is slower for large inputs.**  

---
