# Merge Intervals

## **Problem Statement**
Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals and return an array of non-overlapping intervals.

---

## **Approach 1: Sorting + Merging (Greedy)**
### **Key Steps**
1. **Sort the intervals** based on the starting time.
2. **Iterate through intervals**:
   - If an interval overlaps with the last merged interval, merge them.
   - Otherwise, add the interval as a new entry in the result.
3. **Return the merged intervals**.

### **Complexity Analysis**
- **Time Complexity:** `O(N log N)` due to sorting.
- **Space Complexity:** `O(N)` for storing merged intervals.

---

## **Observations**
- Sorting helps in quickly identifying overlapping intervals.
- Using a list/linked list efficiently stores merged intervals.

## **Approach 2: Using a Stack**
### **Key Steps**
1. **Sort intervals** by the start time.
2. **Use a stack**:
   - If the stack is empty or there is no overlap, push the interval.
   - If overlap exists, update the end of the top interval in the stack.
3. **Return the stack as the merged intervals.**

### **Complexity Analysis**
- **Time Complexity:** `O(N log N)` due to sorting.
- **Space Complexity:** `O(N)` for storing merged intervals.

## **Observations**
- The stack approach is useful when we want to process intervals dynamically.
- This approach is similar to the greedy method but explicitly tracks merged intervals using a stack.
