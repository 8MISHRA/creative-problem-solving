import java.util.HashSet;

// Without using a data structure, how to do it?

public class IsUnique {
 public static void main(String[] args) {
   // Considering capital and small as different
    System.out.println(uniqueChar("abc"));
    System.out.println(uniqueChar("abcc"));
    System.out.println(uniqueChar(""));
    System.out.println(uniqueChar("aaacc"));
    System.out.println(uniqueChar("aabc"));
    System.out.println(uniqueChar("1111"));
 }
 public static boolean uniqueChar(String str){
   char[] arr = str.toCharArray();
   HashSet<Character> set = new HashSet<Character>();
   for (Character c : arr){
      if (set.contains(c)){
         return false;
      }
      else{
         set.add(c);
      }
   }
   return true;
    
 }
}