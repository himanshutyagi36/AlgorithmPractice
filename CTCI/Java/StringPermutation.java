// Given two strings, write a method to decide if one is a permutation of the other.
import java.util.*;

public class StringPermutation {
    // public static boolean areAnagram(String str1, String str2) {
    //     int n1 = str1.length();
    //     int n2 = str2.length();
    //     if(n1 != n2)
    //         return false;
    //     char [] strArr1 = str1.toCharArray();
    //     char[] strArr2 = str2.toCharArray();
    //     Arrays.sort(strArr1);
    //     Arrays.sort(strArr2);
    //     System.out.println(strArr1);
    //     System.out.println(strArr2);
    //     for(int i=0;i<strArr1.length;i++){
    //         if (strArr1[i] != strArr2[i])
    //             return false;
    //     }
    //     return true;
    // }


    // more optimized solution
    public static boolean areAnagramOpt(String str1, String str2) {
        int n1 = str1.length();
        int n2 = str2.length();
        if(n1 != n2)
            return false;
        int[] letters = new int[256];
        char[] strArr1 = str1.toCharArray();
        for(char x : strArr1){
            letters[x]++;
        }
        for(int i=0;i<str2.length();i++) {
            int temp = (int)str2.charAt(i);
            if(--letters[temp] < 0) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
		//the string to test
		String strTest1 = "abc";
        String strTest2 = "bac";
        if (areAnagramOpt(strTest1,strTest2))
            System.out.println("anagrams");
		else {
            System.out.println("Not anagrams");
        }
		
	}
}