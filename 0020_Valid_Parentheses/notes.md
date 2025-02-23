# 📌 Valid Parentheses  

## 🔍 Problem Statement  
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**.  

A string is **valid** if:  
1. Open brackets must be closed by the same type of brackets.  
2. Open brackets must be closed in the correct order.  
3. Every close bracket has a corresponding open bracket of the same type.  

### Example  
```plaintext
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```

---

## 🏷️ Solutions  

### 1️⃣ Stack-Based Approach - **O(n)**  
- Use a **stack** to track open brackets.  
- When a closing bracket appears, check if it matches the **top** of the stack.  
- If it doesn’t match or the stack is empty, return `false`.  
- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(n)` (worst case when all are opening brackets).  

---

## 📝 Notes  
- Stack-based approach is **optimal** and widely used for **parsing expressions**.  
- Handle **edge cases**:
  - Empty string (`""`) is **valid**.
  - Strings with only closing brackets are **invalid**.
  - Strings with an odd number of brackets are **invalid**.
