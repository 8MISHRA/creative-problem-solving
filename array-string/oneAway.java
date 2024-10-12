public class oneAway {
    public static void main(String[] args) {
        System.out.println(isOneAway("bcbc", "bhbc"));
        System.out.println(isOneAway("test", "test"));   // true (Same strings)
        System.out.println(isOneAway("test", "best"));   // true (One character replaced)
        // System.out.println(isOneAway("test", "tests"));  // true (One character inserted)
        // System.out.println(isOneAway("tests", "test"));  // true (One character deleted)
        System.out.println(isOneAway("test", "tast"));   // true (One character replaced)
        System.out.println(isOneAway("test", "tent"));   // true (One character replaced)
        System.out.println(isOneAway("test", "toast"));  // false (Two characters replaced)
        System.out.println(isOneAway("test", "tst"));    // true (One character deleted)
        System.out.println(isOneAway("test", "te"));     // false (More than one character removed)
        System.out.println(isOneAway("tesst", "test"));  // false (More than one character inserted)
    }
    public static boolean isOneAway(String str1, String str2){
        char[] c1 = str1.toCharArray();
        char[] c2 = str2.toCharArray();
        int count = 0;

        if (c2.length>c1.length){
            char[] temp;
            temp = c1;
            c1 = c2;
            c2 = temp;
        }

        if (c1.length > c2.length+1){
            return false;
        } else if (c1.length==c2.length+1){
            int i = 0, j = 0;
            boolean oneAway = true;
            while (i<c1.length){
                if (c1[i] != c2[j]){
                    count ++;
                    i ++;
                }else{
                    i++; j++;
                }
                oneAway = (c1[i-1] == c2[j-1] | count <= 1);
                if (!oneAway){return false;};
            }
            return oneAway;         
        }
        else{
            int i = 0;
            boolean oneAway = true;
            while (i<c1.length){
                if (c1[i] != c2[i]){
                    count ++;
                    i ++;
                }else{
                    i++;
                }
                oneAway = count <= 1;
                if (!oneAway){return false;};
            }
            return oneAway;
        }
    }

}

