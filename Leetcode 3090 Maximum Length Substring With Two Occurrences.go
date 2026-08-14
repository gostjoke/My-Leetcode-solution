func maximumLengthSubstring(s string) int {
    left := 0
    ans := 0
    var fq [26]int
    for right := 0; right < len(s); right++{
        index := s[right] - 'a'
        fq[index] += 1
        for fq[index] > 2 {
            fq[s[left]-'a'] -= 1
            left += 1
        }
        ans = max(ans, right-left+1)
    }
    return ans
}
