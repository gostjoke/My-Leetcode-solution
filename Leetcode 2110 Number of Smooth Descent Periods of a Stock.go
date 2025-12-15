// 2025/12/15

func getDescentPeriods(prices []int) int64 {
    if len(prices) < 2{
        return 1
    }
    var ans int64 = 1
    var curr int64 = 1
    
    for i:=1; i < len(prices); i++{
        if prices[i-1] - prices[i]==1{
            curr += 1
        } else {
            curr = 1
        }
        ans += curr
    }
    return ans
}
