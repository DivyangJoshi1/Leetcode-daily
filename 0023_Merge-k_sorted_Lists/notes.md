# Merge k Sorted Lists

## Problem Statement  
Given an array of `k` linked lists, where each linked list is sorted in ascending order, merge all `k` lists into one sorted linked list and return it.

## Observations  
- Each list is already sorted.
- The final merged list should also be sorted.
- We can use a **Min-Heap**, **Divide & Conquer**, or **Iterative Merging** to solve this efficiently.

## Approaches  

### Approach 1: Using Min-Heap (Priority Queue)  
**Intuition:**  
- A min-heap helps in efficiently fetching the smallest element among the heads of `k` lists.
- Extract the smallest element, move to the next node, and push it into the heap.
- Continue until all nodes are processed.

**Complexity Analysis:**  
- **Time Complexity:** \(O(N \log k)\), where \(N\) is the total number of nodes.  
- **Space Complexity:** \(O(k)\), as we store at most `k` elements in the heap at a time.

---

### Approach 2: Divide and Conquer  
**Intuition:**  
- Instead of merging all lists at once, merge them in pairs recursively.
- This reduces the number of merge operations.

**Complexity Analysis:**  
- **Time Complexity:** \(O(N \log k)\), since we divide the lists and merge step by step.
- **Space Complexity:** \(O(1)\), since merging happens in-place.

---

### Approach 3: Iterative Pairwise Merging  
**Intuition:**  
- Start with the first list and merge it with the second.
- Merge the resulting list with the third, and so on.

**Complexity Analysis:**  
- **Time Complexity:** \(O(N k)\), which is slower for large `k`.  
- **Space Complexity:** \(O(1)\), since merging is done in-place.

---

## Best Approach to Use  
✅ **Min-Heap (Priority Queue) or Divide & Conquer** are the most optimal choices.  
❌ **Iterative Pairwise Merging** is inefficient for large `k`.  

---

## Edge Cases to Consider  
- **Empty List:** If `lists = []`, return `None`.  
- **Single List:** If `lists = [[1,2,3]]`, return it as is.  
- **Different Lengths:** Some lists may have more elements than others.  
- **All Lists Empty:** If `lists = [[], [], []]`, return `None`.  
