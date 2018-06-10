## https://practice.geeksforgeeks.org/problems/find-the-fine/0/?ref=self
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        inp = input().split()
        n = int(inp[0])
        date = int(inp[1])
        carNumbers = list(map(int, input().split()))
        penaltyArray = list(map(int, input().split()))
        fine = 0
        isEven = False
        if (date % 2 == 0):
            isEven = True
        for i in range(n):
            if (isEven and (carNumbers[i] % 2 !=0)):
                fine += penaltyArray[i]
            elif ((not isEven) and (carNumbers[i] % 2 == 0)):
                fine += penaltyArray[i]
        print(fine)