# Problem 2: Add Two Numbers

## Problem Statement:
- Given two non-empty linked lists representing two non-negative integers.
- Digits are stored in **reverse order**.
- Each node contains a **single digit**.
- Return the sum as a linked list in **reverse order**.

## Approaches:

### 1️⃣ Iterative Approach (Using Dummy Node)
- Traverse both linked lists while maintaining a carry.
- Sum corresponding digits, create new nodes, and adjust carry.

✅ **Time Complexity:** O(max(m, n))  
✅ **Space Complexity:** O(max(m, n)) (new list storage)  

### 2️⃣ Recursive Approach
- Base case: If both lists and carry are empty, return null.
- Compute sum and carry for current digit.
- Recursively process the next nodes.

✅ **Time Complexity:** O(max(m, n))  
✅ **Space Complexity:** O(max(m, n)) (recursion stack)

## Edge Cases Considered:
- Lists of different lengths.
- Carry overflow (e.g., 9 + 9).
- One list being empty.

## Optimizations:
- We cannot optimize time beyond **O(max(m, n))** since we must traverse all digits.
