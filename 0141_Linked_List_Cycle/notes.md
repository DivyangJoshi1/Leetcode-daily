# **Linked List Cycle - Solution Approaches**

## **Problem Statement**
Given a linked list, determine if it contains a cycle. A cycle occurs when a node in the list points back to a previous node, forming a loop.

---

## **Approach 1: Hashing (Using a Set)**
### **Idea**
- Use a **HashSet** to store visited nodes.
- Traverse the linked list and check if a node has been seen before.
- If a node appears again, there is a cycle; otherwise, the list terminates normally.

### **Complexity Analysis**
- **Time Complexity:** `O(N)`, since each node is visited once.
- **Space Complexity:** `O(N)`, as we store each node in the set.

---

## **Approach 2: Floyd’s Cycle Detection Algorithm (Two Pointers)**
### **Idea**
- Use **two pointers** (`slow` and `fast`).
- `slow` moves **one step** at a time, while `fast` moves **two steps**.
- If there is a cycle, `fast` will eventually meet `slow`.
- If `fast` reaches `None`, the list has no cycle.

### **Complexity Analysis**
- **Time Complexity:** `O(N)`, since the `fast` pointer moves through the list in linear time.
- **Space Complexity:** `O(1)`, as no extra data structures are used.

---

## **Approach 3: Modifying Node Values (Not Recommended)**
### **Idea**
- Modify the node values (e.g., set them to a special marker).
- If a node with the special value is found again, a cycle exists.
- This approach **modifies the list** and is **not recommended**.

### **Complexity Analysis**
- **Time Complexity:** `O(N)`, as each node is visited once.
- **Space Complexity:** `O(1)`, since no extra storage is used.

---

## **Comparison of Approaches**
| Approach | Time Complexity | Space Complexity | Notes |
|----------|---------------|----------------|------------|
| **Hashing (Set)** | `O(N)` | `O(N)` | Simple but uses extra memory |
| **Floyd’s Cycle Detection** | `O(N)` | `O(1)` | Most efficient and widely used |
| **Modifying Node Values** | `O(N)` | `O(1)` | Alters input, not recommended |

---

## **Final Thoughts**
- **Floyd’s Cycle Detection Algorithm (Two Pointers)** is the most efficient and widely used approach.
- **Hashing** is simple but requires extra memory.
- **Modifying node values** should be avoided in real-world applications.

---

## **References**
- Floyd’s Cycle Detection Algorithm
- LeetCode Problem: Linked List Cycle (LC #141)