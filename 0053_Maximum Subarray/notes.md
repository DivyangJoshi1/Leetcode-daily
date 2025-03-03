# **Maximum Subarray - LeetCode 53**

## **Problem Statement**
Given an integer array `nums`, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.

### **Example 1:**
#### **Input:**
```
nums = [-2,1,-3,4,-1,2,1,-5,4]
```
#### **Output:**
```
6
```
#### **Explanation:**
The subarray `[4,-1,2,1]` has the maximum sum of `6`.

---

## **Approach 1: Kadane’s Algorithm (Greedy)**
- Iterate through the array while keeping track of the maximum sum encountered.
- Maintain a `current_sum`, which resets when it goes negative.
- Update `max_sum` with the highest encountered sum.

### **Time Complexity:** `O(n)`
### **Space Complexity:** `O(1)`

---

## **Approach 2: Divide and Conquer**
- Recursively divide the array into left and right halves.
- Compute:
  - Maximum subarray sum in the left half.
  - Maximum subarray sum in the right half.
  - Maximum sum that crosses the middle.
- Return the maximum of these three values.

### **Time Complexity:** `O(n log n)`
### **Space Complexity:** `O(log n)`

---

## **Key Takeaways**
✅ **Kadane’s Algorithm** is the optimal solution with `O(n)` complexity.  
✅ **Divide and Conquer** is an alternative approach with `O(n log n)` complexity.  
✅ The problem focuses on optimizing subarray sums efficiently.  

---

## **Related Problems**
- **[152] Maximum Product Subarray**
- **[918] Maximum Sum Circular Subarray**
- **[325] Maximum Size Subarray Sum Equals k**