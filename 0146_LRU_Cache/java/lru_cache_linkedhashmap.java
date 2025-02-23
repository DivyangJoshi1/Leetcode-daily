import java.util.*;

class LRUCache {
    private final int capacity;
    private final LinkedHashMap<Integer, Integer> cache;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new LinkedHashMap<>(capacity, 0.75f, true);
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        return cache.get(key);
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            cache.remove(key);
        } else if (cache.size() >= capacity) {
            Iterator<Integer> it = cache.keySet().iterator();
            it.next();
            it.remove();
        }
        cache.put(key, value);
    }
}
