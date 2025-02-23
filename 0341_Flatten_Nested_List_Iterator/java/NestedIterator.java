import java.util.*;

interface NestedInteger {
    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    boolean isInteger();

    // return the single integer that this NestedInteger holds, if it holds a single integer.
    // Return null if this NestedInteger holds a nested list.
    Integer getInteger();

    // @return the nested list that this NestedInteger holds, if it holds a nested list.
    // Return empty list if this NestedInteger holds a single integer.
    List<NestedInteger> getList();
}

public class NestedIterator implements Iterator<Integer> {
    private Queue<Integer> queue = new LinkedList<>();

    public NestedIterator(List<NestedInteger> nestedList) {
        flatten(nestedList);
    }

    private void flatten(List<NestedInteger> nestedList) {
        for (NestedInteger item : nestedList) {
            if (item.isInteger()) {
                queue.offer(item.getInteger());  // Add to queue
            } else {
                flatten(item.getList());  // Recursively flatten nested lists
            }
        }
    }

    @Override
    public Integer next() {
        return queue.poll();  // Return and remove first element
    }

    @Override
    public boolean hasNext() {
        return !queue.isEmpty();  // Check if queue has elements
    }
}
