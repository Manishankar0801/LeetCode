class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int low = 0,high = nums.length-1;
        while(low<high){
            if(nums[low]%2 !=0){
                int a = nums[high];
                nums[high] = nums[low];
                nums[low] = a;
                high--;
            }else{
                low++;
            }
        }
        return nums;
    }
}