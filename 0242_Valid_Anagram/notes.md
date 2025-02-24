# 242. Valid Anagram  

## Approach 1: Sorting (Python & Java)  
### Idea  
- Sort both strings and compare them.  
- If they are equal, then one is an anagram of the other.  

### Complexity Analysis  
- **Time Complexity:** O(n log n) due to sorting.  
- **Space Complexity:** O(1) if sorting is done in-place, otherwise O(n).  

---

## Approach 2: HashMap (Python & Java)  
### Idea  
- Use a frequency count (hashmap/dictionary) to track occurrences of each character.  
- If both strings have the same frequency distribution, they are anagrams.  

### Complexity Analysis  
- **Time Complexity:** O(n) since we traverse the strings once.  
- **Space Complexity:** O(1) as we store at most 26 characters (constant space).  

---

## Approach 3: XOR Method (Python Only)  
### Idea  
- Compute the XOR sum of all characters in both strings.  
- If the XOR sum is 0, the strings are anagrams.  
- This works because XOR cancels out duplicate characters.  

### Issue  
- This approach fails for cases where the characters are different but the count is the same (e.g., "aa" vs. "bb").  

### Complexity Analysis  
- **Time Complexity:** O(n).  
- **Space Complexity:** O(1).  
