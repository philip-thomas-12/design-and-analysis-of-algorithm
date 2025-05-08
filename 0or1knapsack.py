# Problem: 0/1 Knapsack
# Time: O(n * W), Space: O(n * W)

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]

# Example
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7
print("Maximum value:", knapsack(weights, values, W))  # Output: 9
