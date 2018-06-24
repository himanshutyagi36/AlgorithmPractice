## hackerrank common child problem solution
## Basically finding the Longest common subsequence
#!/usr/bin/py
 
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
     
    return lengths[-1][-1]
 
def main():
    s1 = raw_input()
    s2 = raw_input()
    print lcs(s1,s2)
     
if __name__ == '__main__':
    main()
