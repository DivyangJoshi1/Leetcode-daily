# Find Peak Element

## **Understanding the Problem**
- Given an array of integers, we need to find a **peak element**, where an element is a peak if it is **strictly greater** than its adjacent elements.
- The array **does not have to be sorted**.
- The problem guarantees that at least **one peak** always exists.

## **Key Observations**
- **A peak element can be at the boundaries** (first or last element).
- **The problem constraints allow multiple correct answers**.
- **We don’t need to find all peaks, just one valid peak**.

---

## **Approach 1: Binary Search (Optimized)**
### **Why Binary Search?**
- Since we are only required to find one peak, we can take advantage of **binary search** to eliminate half of the search space at each step.
- If `nums[mid] > nums[mid + 1]`, it means there is a peak **towards the left**, so we move left.
- Otherwise, the peak must be **towards the right**, so we move right.
- Eventually, `left` and `right` will converge to a peak element.

### **Time Complexity Analysis**
- At each step, we eliminate half of the elements.
- This gives a complexity of **O(log N)**.

### **Why is this Efficient?**
- Instead of checking every element, we reach a solution **in logarithmic time**.
- Works efficiently even for large input sizes.

---

## **Approach 2: Linear Scan (Brute Force)**
### **Why Consider This?**
- This approach is **simple** and easy to implement.
- We iterate through the array and check for a peak by comparing each element with its neighbors.

### **Time Complexity Analysis**
- Since we scan the array once, the complexity is **O(N)**.

### **When to Use This?**
- This method is useful when `N` is small, and we don’t need an optimized solution.

---

## **Comparing Both Approaches**

| Approach        | Time Complexity | Space Complexity | Best Use Case |
|----------------|----------------|------------------|---------------|
| **Binary Search** | O(log N)       | O(1)             | Large inputs |
| **Linear Scan**  | O(N)           | O(1)             | Small inputs |

---

## **Key Takeaways**
1. **Binary search is the optimal approach** due to its `O(log N)` complexity.
2. **Linear scan is simpler** but slower for large arrays.
3. **A peak always exists**, so we are guaranteed a valid answer.
