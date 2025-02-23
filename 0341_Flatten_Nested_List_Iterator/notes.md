# 341. Flatten Nested List Iterator

## **Approach 1: Using Recursion and Queue (Python)**
- **Concept**: Recursively traverse the nested list and store integers in a queue.
- **Data Structure Used**: `deque` (double-ended queue) for efficient `pop(0)`.
- **Time Complexity**: \(O(N)\) - Each element is processed once.
- **Space Complexity**: \(O(N)\) - Stores all elements in a queue.

## **Approach 2: Stack-Based Iterative Approach (Python)**
- **Concept**: Use a stack to simulate recursion and process elements lazily.
- **Steps**:
  - Initialize stack with the nested list in **reverse order**.
  - `next()` retrieves and removes an integer.
  - `hasNext()` ensures only integers are processed.
- **Time Complexity**: \(O(1)\) for `next()` and `hasNext()` on average.
- **Space Complexity**: \(O(D)\) (where \(D\) is the depth of nesting).

## **Approach 3: Recursion with Queue (Java)**
- **Concept**: Recursively flatten nested lists into a queue.
- **Steps**:
  - Recursively extract all integers and store them in a queue.
  - `next()` dequeues and returns the next integer.
  - `hasNext()` checks if the queue is empty.
- **Time Complexity**: \(O(N)\) - Each element is processed once.
- **Space Complexity**: \(O(N)\) - Uses a queue to store all elements.
