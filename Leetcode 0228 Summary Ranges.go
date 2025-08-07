// 20250806
func summaryRanges(nums []int) []string {
    var ans []string
    i := 0
    start := 0
    for i < len(nums){
        start = i
        for i + 1 < len(nums) && nums[i+1] == nums[i] + 1{
            i+=1
        }
        if i == start{
            ans = append(ans, strconv.Itoa(nums[start]))
        } else{
            ans = append(ans, strconv.Itoa(nums[start])+"->"+strconv.Itoa(nums[i]))
        }
        i+=1
    }
    return ans
}
