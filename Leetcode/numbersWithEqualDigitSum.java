// MS OTA- https://leetcode.com/discuss/interview-question/365872/
// Time: O(NlogK) - N size of array, K digit size
// Space: O(N)
    
public class Main {
    private int computeDigitSum(int a) {
        int sum = 0;
        while(a >0) {
            sum+= a%10;
            a=a/10;
        }
        return sum;
    }
    
    private int maxSum(int[] arr) {
        if(arr.length <=1) return -1;
        int n = arr.length;
        
        HashMap<Integer, Integer> map = new HashMap();
        int res = -1;
        
        for(int i = 0; i < n; ++i) {
            int digitSum = computeDigitSum(arr[i]);
            if(!map.containsKey(digitSum)) {
                map.put(digitSum, arr[i]);
            } else {
                res = Math.max(res, map.get(digitSum) + arr[i]);
                map.put(digitSum, Math.max(arr[i], map.get(digitSum)));
            }
        }
        return res;    
    }
    
    public static void main(String[] args) {
        Main main = new Main();
        int[][] testcases = {{51, 71, 17, 42, 33, 44, 24, 62}, 
                             {51, 71, 17, 42},
                             {42, 33, 60},
                             {51, 32, 43}};
        for(int[] testcase: testcases)
            System.out.println(main.maxSum(testcase));
    }
}
