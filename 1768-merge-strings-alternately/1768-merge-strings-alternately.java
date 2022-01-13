class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int i=0;
        int len = Math.min(word1.length(),word2.length());
        for(i = 0 ; i < len ;i++){
            sb.append(word1.charAt(i));
            sb.append(word2.charAt(i));
        }
        sb.append(word1.substring(i,word1.length()));
        sb.append(word2.substring(i,word2.length()));
        return sb.toString();
    }
}