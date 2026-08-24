class Solution {
    public boolean isValid(String s) {
        /*
        if we find an open character, add it to the stack
        if we find a closed one, pop and check it
        cannot pop from empty stack
        if stack is not fully empty, nono
        */
        Stack<Character> st = new Stack<>();
        String opened = "([{";

        for(int i = 0; i < s.length(); i++){
            char curr = s.charAt(i);

            // we have found an open paren, if closed proceed
            if(opened.indexOf(curr) != -1){
                st.push(curr);
            }

            // now try to find which closed one it is
            if(curr == ')'){
                if(st.size() == 0 || st.pop() != '('){
                    return false;
                }
            }
            if(curr == ']'){
                if(st.size() == 0 || st.pop() != '['){
                    return false;
                }
            }
            if(curr == '}'){
                if(st.size() == 0 || st.pop() != '{'){
                    return false;
                }
            }
        }
        return st.size() == 0;
    }
}
