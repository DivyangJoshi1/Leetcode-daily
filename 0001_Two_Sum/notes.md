# 📌 Two Sum  

## 🔍 Problem Statement  
Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.  
You **may not** use the same element twice.  
Return the answer in **any order**.  

### Example  
```plaintext
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: nums[0] + nums[1] = 2 + 7 = 9  
```

---

## 🏷️ Solutions  

### 1️⃣ Brute Force - **O(n²)**
- Iterate through all pairs and check if they sum to `target`.  
- **Time Complexity:** `O(n²)`  
- **Space Complexity:** `O(1)`

### 2️⃣ Hash Map (Optimal) - **O(n)**
- Store elements in a **hashmap** while iterating.  
- Check if `target - num` exists in the hashmap.  
- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(n)`

---

## 📝 Notes  
- Brute force is **inefficient** for large inputs.  
- **HashMap** significantly improves performance by reducing lookups to `O(1)`.  
- If the array is **sorted**, a **two-pointer approach** (`O(n log n)`) can be used.  
