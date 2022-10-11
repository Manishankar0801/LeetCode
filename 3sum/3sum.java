class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<List<Integer>> resultSet = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            HashMap<Integer,Integer> hashMap = new HashMap<>();
            for(int j=i+1;j<nums.length;j++){
                int sum=-(nums[i]+nums[j]);
                if(hashMap.containsKey(sum)){
                    ArrayList<Integer> arrayList = new ArrayList<>();
                    arrayList.addAll(Arrays.asList(sum,nums[i],nums[j]));
                    Collections.sort(arrayList);
                    resultSet.add(arrayList);
                }
                hashMap.put(nums[j],j);
            }
        }
         return new ArrayList<>(resultSet);
    }
}