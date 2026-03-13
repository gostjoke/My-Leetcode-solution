// 2026/03/12

func containsDuplicate(nums []int) bool {
    seen := make(map[int]struct{})
    for _, i := range(nums) {
        _, exists := seen[i]
        if exists {
            return true
        } else {
            seen[i] = struct{}{}
        }
    }
    return false
}
