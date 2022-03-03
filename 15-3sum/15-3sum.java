class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<List<Integer>> result = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            HashMap<Integer, Integer> hashmap = new HashMap<>();
            for(int j=i+1;j<nums.length;j++){
                int sum = -(nums[i]+nums[j]);
                if(hashmap.containsKey(sum)){
                    List<Integer> w = new ArrayList<Integer>();
                    w.addAll(Arrays.asList(sum,nums[i],nums[j]));
                    Collections.sort(w);
                    result.add(w);
                }
                hashmap.put(nums[j],j);
            }
        }
        return new ArrayList<>(result);
    }
}