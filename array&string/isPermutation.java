import java.util.HashMap;

public class isPermutation {
    public static void main(String[] args) {
        System.out.println(isPermute("ssstr", "ssrts"));
        System.out.println(isPermute("abc", "def"));
        System.out.println(isPermute("eee", "e"));
        System.out.println(isPermute("  ", ""));
        System.out.println(isPermute("e", "eee"));
        System.out.println(isPermute("ppq", "pqp"));
    }

    public static boolean isPermute(String s1, String s2){
        if (s1.length() != s2.length()){ return false; }
        HashMap<Character, Integer> map = new HashMap<>();
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        for(Character c:arr1){
            if (map.containsKey(c)){
                map.put(c, map.get(c)+1);
            }
            else{
                map.put(c, 1);
            }
        }
        for(Character c:arr2){
            if (map.containsKey(c)){
                if (map.get(c)<0){return false;}
                map.put(c, map.get(c)-1);
            }
            else{
                return false;
            }
        }
        return true;
    }
}
