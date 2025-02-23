# Construct Binary Tree from Preorder and Postorder Traversal

## Problem Statement
Given two integer arrays, `preorder` and `postorder`, representing the preorder and postorder traversal of a binary tree with distinct values, reconstruct and return the binary tree.

If multiple valid trees exist, return any of them.

---

## Approach Used:
1. **Recursive Tree Construction**:
   - Use the **first element** in `preorder` as the root.
   - The **second element** in `preorder` must be the root of the left subtree.
   - Find this node’s index in `postorder` to determine the size of the left subtree.
   - Recursively build the left and right subtrees.

2. **HashMap for Quick Lookup**:
   - Store the indices of `postorder` values in a hashmap.
   - This helps in **O(1)** lookup for subtree division.

3. **Base Cases**:
   - If `preStart > preEnd`, return `None` (invalid range).
   - If `preStart == preEnd`, return the single-node tree.

---

## Complexity Analysis:
- **Time Complexity**: `O(N)`, where `N` is the number of nodes.
  - Each node is processed once using recursive calls.
- **Space Complexity**: `O(N)`, due to recursive stack storage.

---

## Optimizations:
- **Avoid using extra lists** by using direct indexing.
- **Using HashMap for `postorder` lookups** reduces the search time from `O(N)` to `O(1)`.