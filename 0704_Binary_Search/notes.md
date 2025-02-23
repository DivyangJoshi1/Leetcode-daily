# 📌 Binary Search  

## 🔍 Problem Statement  
Given a sorted array of integers `nums` and a target value `target`, return the **index** of the target if it exists in the array. Otherwise, return `-1`.  

### Example  
```plaintext
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 is at index 4.

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 is not in the array.
```

---

## 🏷️ Solutions  

### 1️⃣ Iterative Binary Search - **O(log n)**
- Use two pointers: `left` and `right` to track the search space.
- Find the middle element `mid = (left + right) / 2`.
- If `nums[mid] == target`, return `mid`.
- If `target < nums[mid]`, search in the **left half** (`right = mid - 1`).
- Else, search in the **right half** (`left = mid + 1`).
- **Time Complexity:** `O(log n)` (dividing search space in half).  
- **Space Complexity:** `O(1)` (constant space).  

### 2️⃣ Recursive Binary Search - **O(log n)**
- Recursively divide the array into halves.
- **Base case:** If `left > right`, return `-1`.
- Otherwise, find the middle index and apply the same logic.
- **Time Complexity:** `O(log n)`.  
- **Space Complexity:** `O(log n)`, due to recursive calls.  

---

## 📝 Notes  
- **Binary Search** only works on **sorted arrays**.  
- Iterative method is **more memory efficient** than recursion (no stack overhead).  
- This is a fundamental algorithm used in searching problems and **divide & conquer** approaches.  
