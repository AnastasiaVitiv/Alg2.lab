def longest_chain(words):
    word_set = set(words)
    dp = {}

    words.sort(key=len)

    max_length = 1

    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            shorter = word[:i] + word[i+1:]
            if shorter in word_set:
                dp[word] = max(dp[word], dp[shorter] + 1)
        max_length = max(max_length, dp[word])

    return max_length

with open("wchain.in", "r") as f:
    n = int(f.readline())
    words = [f.readline().strip() for _ in range(n)]

result = longest_chain(words)

with open("wchain.out", "w") as f:
    f.write(str(result) + "\n")
