s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

dp = [False] * (len(s) + 1)
dp[0] = True

# dp[i] : 앞에서 i길이 까지 봤을때, i글자까지 사전단어들로 나눌 수 있는가에 대한 bool값

for i in range(len(s) + 1):
    if dp[i]:
        for j in range(i, len(s) + 1):
            if s[i:j] in wordDict:
                print(s[i:j])
                dp[j] = True

print(dp[-1])
