# Reorganize String

## Problem Statement  
Given a string `s`, rearrange its characters so that no two adjacent characters are the same. If it is not possible, return an empty string `""`.

## Observations  
- The most frequent character should not appear consecutively.
- If a character appears more than `(n+1)/2` times, it is impossible to rearrange.
- A **Max-Heap** can help place the most frequent characters first while ensuring separation.

## Approaches  

### Approach 1: Using Max-Heap (Priority Queue)  
**Intuition:**  
- Store character frequencies in a max-heap (priority queue).
- Extract the highest frequency character and place it in the result string.
- Ensure characters are spaced out by re-inserting them after use.

**Steps:**  
1. Build a frequency map of characters.  
2. Insert characters into a max-heap based on frequency.  
3. Repeatedly pop the top character, place it, and store it for the next turn.  
4. If the heap is empty before placing all characters, return `""`.  

**Complexity Analysis:**  
- **Time Complexity:** \(O(N \log 26)\) ≈ \(O(N)\) (since heap operations are limited to 26 characters).  
- **Space Complexity:** \(O(26)\) ≈ \(O(1)\), storing at most 26 characters in a heap.

---

### Approach 2: Greedy Array Placement  
**Intuition:**  
- Sort characters by frequency and distribute them in even-indexed positions first.
- If the frequency of a character exceeds half the string length, return `""`.

**Steps:**  
1. Count character frequencies.  
2. Sort characters by frequency.  
3. Place the most frequent characters first in even indexes, then fill odd indexes.  
4. If any character count exceeds `(n+1)/2`, return `""`.  

**Complexity Analysis:**  
- **Time Complexity:** \(O(N + 26 \log 26)\) ≈ \(O(N)\).  
- **Space Complexity:** \(O(26)\) ≈ \(O(1)\).

---

## Best Approach to Use  
✅ **Max-Heap (Priority Queue)** is intuitive and works efficiently.  
✅ **Greedy Array Placement** is also effective and runs in linear time.  

---

## Edge Cases to Consider  
- **Single Character:** `"a"` → `"a"` (already valid).  
- **Impossible Cases:** `"aaaabb"` → `""` (too many `a`s).  
- **Already Valid Strings:** `"abab"` → `"abab"` (no need to modify).  
- **Multiple Valid Outputs:** `"aabbc"` → `"abcab"`, `"bacba"`, etc.  