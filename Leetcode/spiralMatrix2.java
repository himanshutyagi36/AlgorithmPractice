//Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
class Solution {
    public int[][] generateMatrix(int num) {
        int[][] result = new int[num][num];
        int i,k=0,l=0;
        int m=num;
        int n = num;
        /*  k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator 
        */
        int cval=1;
        while(k<n && l<n) {
            // create the first row from the remaining rows 
            for (i = l; i < n; ++i) 
            { 
                result[k][i]=cval++; 
            } 
            k++;
            // create last column from remaining columns
            for(i=k;i<m;i++) {
                result[i][n-1] = cval++;
            }
            n--;
            // create the last row from the remaining rows */ 
            if ( k < m) 
            { 
                for (i = n-1; i >= l; --i) 
                { 
                    result[m-1][i]=cval++; 
                } 
                m--; 
            }
            // create the first column from the remaining columns */ 
            if (l < n) 
            { 
                for (i = m-1; i >= k; --i) 
                { 
                    result[i][l]=cval++; 
                } 
                l++;     
            }  
        }
        return result;
    }
}
