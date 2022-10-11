class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> resultMap = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int result = target-nums[i];
            if(resultMap.containsKey(result)){
                return new int[] {i, resultMap.get(result)};
            }
            resultMap.put(nums[i],i);
        }
        return new int[] {-1,-1};
    }
}