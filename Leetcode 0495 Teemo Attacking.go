// 20250807
func findPoisonedDuration(timeSeries []int, duration int) int {
    if len(timeSeries) == 0{
        return 0
    } else if len(timeSeries)==1{
        return duration
    }
    // last attack
    ans := duration
    for i:=0; i<len(timeSeries)-1; i++{
        if timeSeries[i+1] - timeSeries[i] < duration{
            ans += (timeSeries[i+1] - timeSeries[i])
        } else{
            ans += duration
        }
    }
    return ans
}
