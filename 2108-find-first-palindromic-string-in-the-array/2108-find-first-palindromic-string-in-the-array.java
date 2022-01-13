class Solution {
    public String firstPalindrome(String[] words) {
        for(String word:words){
            if(palindrome(word)){
                return word;
            }
        }
        return "";
    }
    public static boolean palindrome(String words){
        int low =0, high=words.length()-1;
            while(low <= high){
                if(words.charAt(low)!=words.charAt(high)){
                    return false;
                }else{
                    low++;
                    high--;
                }
            }
        return true;
    }
}