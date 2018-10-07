/**
 *  Implement an algorithm to determine if a string hasall unique characters.What
if you cannot use additional data structures?
 */

import java.util.*;

public class AllUniqueChars {
	public static void main(String[] args) {
		//the string to test
		String strTest1 = "adsfsdf";
		String strTest2 = "adsfeb";
		judgeUnique(strTest1);
		judgeUnique(strTest2);
		
	}
	public static boolean judgeUnique(String tempStr){
		boolean flag = false;
		//convert the string into the characters array
		char [] strArray = tempStr.toCharArray();
		//sort the characters array
		Arrays.sort(strArray);
		//compare the characters array
		for (int i = 0; i < strArray.length - 1; i++) {
			if(strArray[i] == strArray[i + 1]){
				flag = true;
				System.out.println("the string is not unique");
				return flag;
			}	
		}
		System.out.println("the string is unique");
		return flag;
	}
}