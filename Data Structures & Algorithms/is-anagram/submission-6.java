class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hm = new HashMap<>();


        for(int i = 0; i < s.length(); i++){
            hm.put(s.charAt(i), hm.getOrDefault(s.charAt(i),0) + 1);
        }

        for(int i = 0; i < t.length(); i++){
            if(!hm.containsKey(t.charAt(i))){
                return false;
            }
            else{
                hm.put(t.charAt(i), hm.get(t.charAt(i))-1);
            }
        }

        for(int count : hm.values()){
            if(count != 0){
                return false;
            }
        }
        return true;

    }
}
