# 📌 Longest Substring Without Repeating Characters  

## 🔍 Problem Statement  
Given a string `s`, find the length of the **longest substring** without repeating characters.  

### Example  
```plaintext
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

---

## 🏷️ Solutions  

### 1️⃣ Sliding Window + HashSet - **O(n)**  
- Use a **HashSet** to track characters in the current window.  
- Use two pointers (`left` and `right`) to expand and contract the window.  
- If a character repeats, remove characters from the left until it's unique.  
- **Time Complexity:** `O(n)`, since each character is processed at most twice.  
- **Space Complexity:** `O(min(n, 26))` (only storing unique characters).  

### 2️⃣ Optimized Sliding Window + HashMap - **O(n)**  
- Instead of removing characters one by one, directly move `left` to avoid repetition.  
- Store each character’s last seen index in a **HashMap**.  
- **Time Complexity:** `O(n)`.  
- **Space Complexity:** `O(min(n, 26))`.  

---

## 📝 Notes  
- The **Sliding Window** technique is efficient for substring problems.  
- This problem helps in understanding **window expansion & contraction** strategies.  
- Works best when combined with **HashSet** or **HashMap** for quick lookups.  
