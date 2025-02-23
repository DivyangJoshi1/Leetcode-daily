# 215 - Kth Largest Element in an Array  

## **Approach 1: Sorting**
- **Concept:** Sort the array in descending order and return the `k`th element.
- **Time Complexity:** `O(N log N)` due to sorting.
- **Space Complexity:** `O(1)` if sorting in place, otherwise `O(N)` if using an extra array.

## **Approach 2: Min-Heap (Priority Queue)**
- **Concept:** Maintain a min-heap of size `k`. The top element of the heap will be the `k`th largest element.
- **Steps:**
  - Add elements to the heap one by one.
  - If the heap size exceeds `k`, remove the smallest element.
  - The root of the heap at the end will be the `k`th largest element.
- **Time Complexity:** `O(N log k)` (heap operations).
- **Space Complexity:** `O(k)` for storing elements in the heap.

## **Approach 3: QuickSelect (Hoare’s Selection Algorithm)**
- **Concept:** Similar to QuickSort, but only processes the relevant part of the array.
- **Steps:**
  - Select a pivot and partition the array.
  - Recursively search for the `k`th largest element in the required half.
- **Time Complexity:** Average case `O(N)`, worst case `O(N^2)` (if pivot selection is bad).
- **Space Complexity:** `O(1)` (in-place).

## **Comparison of Approaches**

| Approach  | Time Complexity | Space Complexity | Best For        |
|-----------|---------------|-----------------|----------------|
| Sorting   | `O(N log N)`  | `O(1)`          | Small datasets |
| Min-Heap  | `O(N log k)`  | `O(k)`          | Medium datasets |
| QuickSelect | `O(N)` avg, `O(N^2)` worst | `O(1)` | Large datasets |
