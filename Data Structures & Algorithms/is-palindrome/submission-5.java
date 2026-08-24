class Solution {
    public boolean isPalindrome(String s) {
        /*
        left and right pointer
            iterate left and right ptr until it is a valid char to check
                check for alphabetic and digit
        */
        int left = 0;
        int right = s.length() - 1;

        while(left < right){

            char leftC = s.charAt(left);
            char rightC = s.charAt(right);

            while(left < right && !(Character.isAlphabetic(s.charAt(left)) || Character.isDigit(s.charAt(left)))){
                left++;
            }

            while(left < right && !(Character.isAlphabetic(s.charAt(right)) || Character.isDigit(s.charAt(right)))){
                right--;
            }

            if(Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
