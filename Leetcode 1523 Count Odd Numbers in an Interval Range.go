// 2025/12/15
func countOdds(low int, high int) int {
    var ans int = 0
    if low % 2== 1{
        ans+=1
        low+=1
    }
    if high % 2 == 1{
        ans+=1
        high-=1
    }
    ans += (high-low)/2
    return ans
}

