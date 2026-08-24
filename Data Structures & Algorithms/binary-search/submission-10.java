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
    int left = 0;
    int right = nums.length-1;

    while(left <= right){
        int mid = (left+right)/2;

        if(nums[mid] == target){
            return mid;
        }
        if(nums[mid] > target){
            right = mid - 1;
        }
        if(nums[mid]<target){
            left = mid + 1;
        }
    }
    return -1;
    }
}
