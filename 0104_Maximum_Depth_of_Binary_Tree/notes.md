# LeetCode 104 - Maximum Depth of Binary Tree

## **Problem Statement**
Given the root of a binary tree, return its maximum depth.  
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## **Approach 1: Recursive DFS**
### **Explanation**
- If the tree is empty (`root == null`), return `0`.
- Otherwise, compute the depth of left and right subtrees.
- The maximum depth is `1 + max(left_depth, right_depth)`.

### **Complexity Analysis**
- **Time Complexity:** `O(n)`, where `n` is the number of nodes.
- **Space Complexity:** `O(h)`, where `h` is the height of the tree (worst case `O(n)`, best case `O(log n)`).

---

## **Approach 2: Iterative BFS (Level Order Traversal)**
### **Explanation**
- Use a queue to traverse the tree level by level.
- For each level, process all nodes and increment the depth counter.
- When all levels are processed, return the depth.

### **Complexity Analysis**
- **Time Complexity:** `O(n)`, since each node is processed once.
- **Space Complexity:** `O(n)`, as we store nodes in a queue.

---

## **Summary**
- **DFS (Recursive):** Simple and elegant, but may cause stack overflow for deep trees.
- **BFS (Iterative):** Uses a queue, better for iterative solutions.

---

## **Next Steps**
- Explore depth-first search with an explicit stack (iterative DFS).
- Solve related problems like "Balanced Binary Tree" and "Minimum Depth of Binary Tree".
