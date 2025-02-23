# 📌 Reverse Linked List  

## 🔍 Problem Statement  
Given the `head` of a singly linked list, reverse the list and return its new head.  

### Example  
```plaintext
Input: head = [1,2,3,4,5]  
Output: [5,4,3,2,1]  
Explanation: The linked list is reversed.
```

---

## 🏷️ Solutions  

### 1️⃣ Iterative Approach - **O(n)**  
- Use **three pointers**: `prev`, `curr`, and `next`.  
- Traverse the list and **reverse the links**.  
- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(1)`  

### 2️⃣ Recursive Approach - **O(n)**  
- Recursively **reverse the rest of the list**.  
- Adjust the current node’s pointer.  
- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(n)` (due to recursion stack).  

---

## 📝 Notes  
- **Iterative** is more space-efficient (`O(1)` space).  
- **Recursive** is more elegant but has an `O(n)` recursion stack.  
- Be mindful of **null checks** for edge cases (empty list, single-node list).  
