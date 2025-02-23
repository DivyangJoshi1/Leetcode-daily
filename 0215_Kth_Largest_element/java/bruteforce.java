import java.util.Arrays;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];  // Kth largest is at (N-k)th index
    }
}
