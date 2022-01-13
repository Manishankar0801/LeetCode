class Solution {
    public String mergeAlternately(String word1, String word2) {
        String result = "";
        int i=0;
        for(i = 0 ; i < Math.min(word1.length(),word2.length());i++){
           result = result + word1.charAt(i);
           result = result + word2.charAt(i);
        }
        result = result + word1.substring(i,word1.length());
        result = result + word2.substring(i,word2.length());
        return result;
    }
}