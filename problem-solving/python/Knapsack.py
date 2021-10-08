for t in range(int(input())):
    n,w=map(int, input().split())
    arr=list(map(int, input().split()))
    dp=[[0 for i in range(w+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if j-arr[i-1]>=0:
                dp[i][j]=max(arr[i-1]+dp[i][j-arr[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]

    print(max(dp[-1]))
