## https://www.geeksforgeeks.org/find-smallest-number-whose-digits-multiply-given-number-n/
## Given a number ‘n’, find the smallest number ‘p’ such that if we multiply all digits of ‘p’, we get ‘n’. 
## The result ‘p’ should have minimum two digits.
def findDigit(n):
    # Case 1 - if number is smaller than 10
    if n<10:
        print(str(n+10)) 
    factors = []
    # Case 2 - Start with 9 and try every possible digit
    for i in range(9,1,-1):
        ## while current digit divides n, store all occurances
        while n%i==0:
            n=n/i
            factors.append(i)
    # If n could not be broken in form of digits
    # prime factors of  n are greater than 9
    if n >10:
        print("Not Posible")
    print(factors)
    n = factors[len(factors)-1]
    for i in range(len(factors)-2,-1,-1):
        n = 10*n + factors[i]
    print(str(n))
    
if __name__ == '__main__':
    n = int(input())
    findDigit(n)