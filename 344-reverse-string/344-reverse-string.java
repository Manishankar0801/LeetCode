class Solution {
    public void reverseString(char[] s) {
        int low = 0, high = s.length-1;
        while (low<high){
            char c = s[high];
            s[high] = s [low];
            s[low] = c;
            low++;
            high--;
        }
    }
}