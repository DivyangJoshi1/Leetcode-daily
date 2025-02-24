# Leetcode 189 - Rotate Array

## Problem Statement:
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

---

## **Approach 1: Reverse Method (Optimal - O(n) Time, O(1) Space)**

### **Idea:**
- Reverse the **entire array**.
- Reverse the **first k elements**.
- Reverse the **remaining n-k elements**.
- This shifts the array efficiently in-place.

### **Steps:**
1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the last `n-k` elements.

### **Complexity:**
- **Time:** `O(n)` (Reversal takes `O(n)`)
- **Space:** `O(1)`

✅ **Used in both Python and Java**

---

## **Approach 2: Cyclic Replacements (Python - O(n) Time, O(1) Space)**

### **Idea:**
- Treat array rotation as a **cyclic movement**.
- Swap elements in-place following cycles until all elements are moved.

### **Steps:**
1. Start at an index.
2. Move the element `k` steps ahead.
3. Repeat until the cycle completes.
4. Continue for all elements.

### **Complexity:**
- **Time:** `O(n)`
- **Space:** `O(1)`

✅ **Used in Python**

---

## **Approach 3: Extra Array (Java - O(n) Time, O(n) Space)**

### **Idea:**
- Use an **extra array** to store shifted values.
- Place each element in its new position `(i + k) % n`.
- Copy back to the original array.

### **Complexity:**
- **Time:** `O(n)`
- **Space:** `O(n)`

✅ **Used in Java**