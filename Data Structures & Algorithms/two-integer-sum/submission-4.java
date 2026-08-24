class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
        find the complement of the target and see if that has been in the seen list yet
        hm of {number : index}
        */

        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
          int compl = target - nums[i];

          if(hm.containsKey(compl)){
            return new int[] {hm.get(compl), i};
          }  
          hm.put(nums[i], i);
        }
        return null;
    }

}
