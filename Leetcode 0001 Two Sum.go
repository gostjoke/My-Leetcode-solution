// 2025/07/02

func twoSum(nums []int, target int) []int {
    dict := make(map[string]int)
    for index, no := range nums{
        comp := target - no
        key := strconv.Itoa(comp)
        if idx, ok := dict[key]; ok{
            return []int{idx, index} // 找到了
        } else{
            dict[strconv.Itoa(no)] = index
        }
    };
    return nil;
}
