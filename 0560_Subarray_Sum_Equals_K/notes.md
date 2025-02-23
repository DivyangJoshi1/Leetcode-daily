# 📌 Subarray Sum Equals K  

## 🔍 Problem Statement  
Given an integer array `nums` and an integer `k`, return the **total number of subarrays** whose sum equals `k`.  

### Example  
```plaintext
Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2
```

---

## 🏷️ Solutions  

### 1️⃣ Brute Force - **O(n²)**
- Use two nested loops to check all possible subarrays.
- Maintain a `sum` variable and update it for each subarray.
- If `sum == k`, increase the count.
- **Time Complexity:** `O(n²)` (not efficient for large arrays).
- **Space Complexity:** `O(1)`, as no extra storage is used.

### 2️⃣ Optimized Approach using HashMap - **O(n)**
- Maintain a **prefix sum** to keep track of cumulative sums.
- Use a **HashMap** (`prefixSumMap`) to store **(prefix sum → frequency)**.
- At each step:
  - Compute the cumulative sum.
  - Check if `(sum - k)` exists in the HashMap.
  - If it exists, add the stored frequency to `count`.
  - Update the HashMap with the new sum.
- **Time Complexity:** `O(n)`, as we traverse the array once.
- **Space Complexity:** `O(n)`, due to HashMap storage.

---

## 📝 Notes  
- **Brute force** is intuitive but inefficient for large inputs.  
- **Using HashMap** improves efficiency to `O(n)`.  
- Works well for **positive and negative numbers**, unlike sliding window techniques.  
