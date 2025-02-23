# Search Insert Position (LeetCode 35)

## **Problem Statement**
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## **Approaches & Explanation**

### **1️⃣ Brute Force - Linear Search**
- Traverse the array and find the first index where `nums[i] >= target`.
- If no such index is found, return `nums.length`.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

### **2️⃣ Optimized Approach - Binary Search**
- Since the array is sorted, use Binary Search to efficiently find the target or the correct insertion index.
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

### **3️⃣ Most Optimized - Using `bisect` in Python**
- Python has a built-in module `bisect` that efficiently finds the insertion index.
- `bisect_left(nums, target)` returns the leftmost index where `target` can be inserted to keep the list sorted.
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

## **Code Implementations**
- **Java (Brute Force - Linear Search) → `01_SearchInsert_Linear.java`**
- **Java (Binary Search) → `02_SearchInsert_BinarySearch.java`**
- **Python (Using `bisect`) → `03_SearchInsert_Bisect.py`**

## **Key Takeaways**
- If performance is critical, use **Binary Search** (O(log n)).
- For Python, `bisect` is the easiest and most efficient way to solve the problem.
