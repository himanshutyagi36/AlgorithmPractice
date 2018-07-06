## Question: https://practice.geeksforgeeks.org/problems/ease-the-array/0

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        res = []
        items = list(map(int,input().split()))
        for i in range(n-1):
            #print(items)
            if items[i] and i+1<=n:
                if items[i] == items[i+1]:
                    items[i+1]=0
                    value = items[i]*2
                    res.append(value)
                else:
                    res.append(items[i])
            else:
                continue
        if(items[n-1]):
            res.append(items[n-1])
        for i in range(abs(n-len(res))):
            res.append(0)
        
        print(*res)
        t-=1
            
            
        
