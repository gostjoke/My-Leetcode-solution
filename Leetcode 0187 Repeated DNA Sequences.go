// 2026/08/17
func findRepeatedDnaSequences(s string) []string {
    seen := make(map[string]bool)
    repeated := make(map[string]bool)
    var ans []string
    if len(s) < 11{
        return ans
    }

    for i:=0; i+10<=len(s); i++{
        sub := s[i:i+10]
        if seen[sub]{
            repeated[sub] = true
        }
        seen[sub] = true
    }
    
    for i := range repeated{
        ans = append(ans, i)
    }

    return ans

}
