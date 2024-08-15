def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a DP table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Length of LCS is dp[m][n]
    lcs_length = dp[m][n]

    # Backtrack to find the LCS
    i, j = m, n
    lcs = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the lcs list since we collected it backwards
    lcs.reverse()

    return lcs_length, ''.join(lcs)


# Example usage
X = "ABCDGH"
Y = "AEDFHR"
length, subsequence = lcs(X, Y)
print(f"LCS length: {length}")
print(f"LCS: {subsequence}")
