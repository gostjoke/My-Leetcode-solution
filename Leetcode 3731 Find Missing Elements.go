// 2026/08/17

func findMissingElements(nums []int) []int {
    var ans []int
    sliceMin := slices.Min(nums)
    sliceMax := slices.Max(nums) 
    seen := make([]int, (sliceMax-sliceMin)+1)
    if len(nums) == (sliceMax-sliceMin+1){
        return ans
    }

    for _, n := range nums {
        seen[n-sliceMin] = 1
    }
    for i:=0; i<len(seen);i++{
        if seen[i] == 0{
            ans = append(ans, i+sliceMin)
        }
    }
    return ans
}
