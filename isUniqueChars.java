class Main {
  static boolean isUniqueChars(String str) {
    if(str.length() > 126) return false;
    // create a boolean array of all possible characters 
    boolean[] char_set = new boolean[128];
    // loop through the given string, store its index in val
   
    for(int i = 0; i < str.length(); i++) {
      int val = str.charAt(i);  
      System.out.println(val); // ASCII value a: 97
       // check if the character set exists in val, if yes: then there's NOT unique characters 
      if(char_set[val]) {
        return false;
      }
      // otherwise set it to true and return true by default
      char_set[val] = true; 
      System.out.println(char_set[val]);
    } return true;
  }






  public static void main(String[] args) {

    System.out.println(isUniqueChars("asjdfaksflk"));
  }

}

