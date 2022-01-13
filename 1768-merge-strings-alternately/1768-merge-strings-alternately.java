class Solution {
    public String mergeAlternately(String word1, String word2) {
        int low=0,high=0;
        String result = "";
        while(low<word1.length() && high<word2.length()){
            result = result + word1.charAt(low);
            result = result + word2.charAt(high);
            low++;
            high++;
        }
        if(word1.length()>word2.length()){
            result = result + word1.substring(word2.length(),word1.length());
        }else{
             result = result + word2.substring(word1.length(),word2.length());
        }
        return result;
    }
}