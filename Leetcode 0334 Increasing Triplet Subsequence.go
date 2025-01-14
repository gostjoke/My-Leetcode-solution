// 2025/01/14

func increasingTriplet(nums []int) bool {
    min1 := math.MaxInt64 // 初始化為 Go 的最大整數
    min2 := math.MaxInt64

    for _, n := range nums{
        if (n <= min1){
            min1 = n
        }else if (n<=min2){
            min2 = n
        }else{
            return true
        }
    }
    return false
}
