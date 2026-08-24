class Solution {
    public int search(int[] nums, int target) {
        /*
        left and right pointers
        mid ptr
        we use the left and right ptrs to create a mid ptr
            we can choose which partition that mid creates to traverse and 
            disregard the other part to optimize the search
        we know the target isnt there when left and right are in the same index
        */
        return helper(nums, target, 0, nums.length - 1);
    }
    public int helper(int nums[], int target, int left, int right){
        if(left > right){
            return -1;
        }
        int mid = (left + right) / 2;

        if(nums[mid] == target){
            return mid;
        }

        if(nums[mid] < target){
            return helper(nums, target, mid+1, right);
        } 

        return helper(nums,target, left, mid -1);
    }
    
}
