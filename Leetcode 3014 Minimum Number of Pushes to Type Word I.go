// 2026/08/11
func minimumPushes(word string) int {
    n := len(word)
    ans :=0
    for i := range(n){
        ans += (i/8) +1
    }
    return ans
}
