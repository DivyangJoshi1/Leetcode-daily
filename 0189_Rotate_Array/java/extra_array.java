class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;

        int[] temp = new int[n];
        
        for (int i = 0; i < n; i++) {
            temp[(i + k) % n] = nums[i]; // Shift element to new position
        }
        
        System.arraycopy(temp, 0, nums, 0, n); // Copy back to original array
    }
}
