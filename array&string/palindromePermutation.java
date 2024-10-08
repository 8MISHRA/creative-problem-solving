import java.util.HashMap;
import java.util.Map;


public class palindromePermutation {
    public static void main( String[] args){
        System.out.println(isPalindromePermutation("love"));
    }

    public static boolean isPalindromePermutation(String str){
        char[] arr = str.toCharArray();
        HashMap<Character, Integer> map = new HashMap();
        for (Character c : arr){
            if (map.containsKey(c)){
                map.put(c, map.get(c)+1);
            }else{
                map.put(c, 1);
            }
        }
        if (arr.length % 2 == 0){
            for(Map.Entry<Character, Integer> entry : map.entrySet()){
                int value = entry.getValue();
                if(value%2!=0) return false;
            }
            return true;
        }else{
            int oddCount = 0;
            for(Map.Entry<Character, Integer> entry : map.entrySet()){
                int value = entry.getValue();
                if (value%2 != 0 & oddCount == 0){
                    oddCount ++;
                }else if (value%2 != 0) return false;
            }
            return true;
        }
    }
}
