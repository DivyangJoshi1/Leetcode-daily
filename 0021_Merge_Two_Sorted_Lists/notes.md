# 📌 Merge Two Sorted Lists  

## 🔍 Problem Statement  
You are given the heads of two **sorted** linked lists, `list1` and `list2`. Merge the two lists into one **sorted** linked list and return the **head** of the merged list.  

### Example  
```plaintext
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
```

---

## 🏷️ Solutions  

### 1️⃣ Iterative Approach - **O(n + m)**
- Use a **dummy node** to simplify list merging.
- Compare the values from `list1` and `list2`.
- Append the smaller node to the merged list.
- Move the pointer of the list that had the smaller value.
- When one list is exhausted, attach the remaining nodes of the other list.
- **Time Complexity:** `O(n + m)`, where `n` and `m` are the lengths of the two lists.  
- **Space Complexity:** `O(1)`, as we only modify pointers.

### 2️⃣ Recursive Approach - **O(n + m)**
- Base case: If `list1` is null, return `list2`, and vice versa.
- Compare `list1.val` and `list2.val`, set the smaller one as `head`, and recursively merge the rest.
- **Time Complexity:** `O(n + m)`, as we visit each node once.
- **Space Complexity:** `O(n + m)`, due to recursive calls.

---

## 📝 Notes  
- The **iterative** approach is **better for large lists** due to less memory overhead.  
- **Recursion** provides a more elegant solution but may cause **stack overflow** for deep recursion.  
- This is a fundamental problem in **Linked Lists** and is commonly used in **Merge Sort** algorithms.  
