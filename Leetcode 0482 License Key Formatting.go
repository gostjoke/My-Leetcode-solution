// 20250804
func licenseKeyFormatting(s string, k int) string {
    s_r := strings.ReplaceAll(strings.ToUpper(s), "-","")
    if len(s_r) <= k {
        return s_r
    }

    left := len(s_r) % k
    var ans []string
    if left != 0 {
        ans = append(ans, s_r[:left]+"-")
    }
    count := 0
    for _, ch := range s_r[left:] {
        if count == k{
            ans = append(ans, "-")
            count = 0
        }
        ans = append(ans, string(ch))
        count += 1
    }

    return strings.Join(ans, "")
}
