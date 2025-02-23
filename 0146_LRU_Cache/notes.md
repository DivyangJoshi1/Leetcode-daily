# 📌 LRU Cache  

## 🔍 Problem Statement  
Design and implement a **Least Recently Used (LRU) cache**.  
The cache should support two operations:  
1. `get(key)`: Retrieve the value of the `key` if it exists, otherwise return `-1`.  
2. `put(key, value)`: Insert or update the `key` with `value`. If the cache reaches its capacity, remove the **least recently used** item.  

### Example  
```plaintext
Input:
LRUCache cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);    // returns 1
cache.put(3, 3); // removes key 2
cache.get(2);    // returns -1 (not found)
cache.put(4, 4); // removes key 1
cache.get(1);    // returns -1 (not found)
cache.get(3);    // returns 3
cache.get(4);    // returns 4
```

---

## 🏷️ Solutions  

### 1️⃣ **Using `LinkedHashMap` (Java Built-in) - O(1)**
- **Use Java's `LinkedHashMap`** (with access-order enabled) to maintain LRU ordering.
- Override `removeEldestEntry()` to automatically evict the least recently used item.
- **Time Complexity:** `O(1)` for `get` and `put`.
- **Space Complexity:** `O(capacity)`, as we store at most `capacity` elements.

### 2️⃣ **Using Doubly Linked List + HashMap (Efficient) - O(1)**
- **Maintain a HashMap** (`key → node reference`) for `O(1)` lookups.
- **Use a Doubly Linked List**:
  - Store nodes in order of usage.
  - Most recently used node is at the **head**.
  - Least recently used node is at the **tail** (removed when capacity is exceeded).
- **Operations**:
  - `get(key)`: Move the node to the front (MRU position).
  - `put(key, value)`: Add or update the key, move it to the front.
  - If the cache exceeds capacity, remove the **tail** (LRU element).
- **Time Complexity:** `O(1)` for `get` and `put`.
- **Space Complexity:** `O(capacity)`, for storing nodes.

### 3️⃣ **Using OrderedDict (Python) - O(1)**
- Python’s `OrderedDict` maintains insertion order.
- **Operations**:
  - `get(key)`: Move key to the end to mark it as recently used.
  - `put(key, value)`: Insert or update and move it to the end.
  - If full, remove the first key (LRU).
- **Time Complexity:** `O(1)`.
- **Space Complexity:** `O(capacity)`.

---

## 📝 Notes  
- **LinkedHashMap** is the easiest way in Java (`O(1)`).  
- **Doubly Linked List + HashMap** provides full manual control (`O(1)`).  
- **Python `OrderedDict`** is the cleanest implementation.  
- **Eviction strategy** is key: always remove **Least Recently Used** when full.  