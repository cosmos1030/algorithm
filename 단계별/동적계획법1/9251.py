word1 = input()
word2 = input()
dp = [0 for _ in range(len(word2))]

for i in range(len(word1)):
    cnt = 0
    for j in range(len(word2)):
        if cnt<dp[j]:
            cnt = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = cnt+1

print(max(dp))
