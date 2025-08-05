// 2025/08/05
func maxStrength(nums []int) int64 {
    if len(nums) == 1{
        return int64(nums[0])
    } 

    var positive []int
    var negative []int

    for _, i := range nums {
        if i > 0{
            positive = append(positive, i)
        } else if i < 0 {
            negative = append(negative, i)
        }
    }
    slices.Sort(negative)

    if len(negative) % 2 == 1{
        negative = negative[:len(negative)-1]
    }

    if len(negative) == 0 && len(positive) == 0 {
        return 0
    }
    positive = append(positive, negative...)
    ans := 1
    for _, i := range positive{
        ans *= i
    }
    
    return int64(ans)
}
