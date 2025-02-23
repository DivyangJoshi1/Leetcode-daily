# Leetcode 238 - Product of Array Except Self

## **Problem Statement**
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.  
You **must** solve the problem **without using division** and in **O(n) time**.

---

## **Approaches Used**

### **1. Optimized Prefix & Suffix (Python)**
- **Two-pass approach**
- First pass: Compute prefix product.
- Second pass: Multiply with suffix product using a single variable.

### **2. Space-Optimized Prefix & Suffix (Python)**
- Instead of using a separate prefix and suffix array, update `answer[]` directly.
- Saves extra space while maintaining O(n) time complexity.

### **3. Left and Right Product (Java)**
- **Single pass approach**.
- First pass: Compute left product directly in the result array.
- Second pass: Multiply with right product while updating in place.

---

## **Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|---------------|----------------|
| Optimized Prefix & Suffix (Python) | O(n) | O(1) |
| Space-Optimized Prefix & Suffix (Python) | O(n) | O(1) |
| Left and Right Product (Java) | O(n) | O(1) |

---

## **Example**
**Input:**  
`nums = [1,2,3,4]`  

**Output:**  
`[24,12,8,6]`  

**Explanation:**
- Prefix pass: `[1, 1, 2, 6]`
- Suffix pass: `[24,12,8,6]`

---