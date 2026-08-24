class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numbs = new HashSet<>();

        for(int i = 0; i < nums.length; i++){
            int prevLen = numbs.size();
            numbs.add(nums[i]);
            if(prevLen == numbs.size())
                return true;
        }
        return false;
    }
}