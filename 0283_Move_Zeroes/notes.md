# LeetCode 283 - Move Zeroes

## **Problem Statement**
Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of non-zero elements. Do this in-place without making a copy of the array.

## **Approach 1: Using Extra List**
- Extract all non-zero elements.
- Count the number of zeros.
- Modify the original list by placing non-zero elements first and then appending the required number of zeros.

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (Uses extra space)

---

## **Approach 2: Two Pointers (In-place)**
- Use two pointers: `left` tracks the position to place a non-zero number, `right` iterates over the array.
- Swap elements when `right` finds a non-zero and `left` is at zero.

**Time Complexity:** O(n)  
**Space Complexity:** O(1) (In-place modification)

---

## **Approach 3: Optimized Two-Pointer**
- Similar to Approach 2 but avoids unnecessary swaps when `left == right`, making it more efficient.

---
✅ **All solutions pass all test cases on LeetCode.**