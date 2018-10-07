import sys
def matrixChain(arr, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1,n):
        m[i][i] = 0
    
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i+L-1
            m[i][j] = sys.maxsize
            for k in range(i,j):
                cost = m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j]
                if cost < m[i][j]:
                    m[i][j] = cost
    return m[1][n-1]
if __name__ == '__main__':
    t = input()
    for _ in range(int(t)):
        n = input()
        items = list(map(int,input().split()))
        print(matrixChain(items,int(n)))