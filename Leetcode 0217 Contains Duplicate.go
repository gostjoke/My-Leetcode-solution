// 2026/03/12

func containsDuplicate(nums []int) bool {
    seen := make(map[int]struct{})
    for _, i := range(nums) {
        if _, exists := seen[i]; exists {
            return true
        } else {
            seen[i] = struct{}{}
        }
    }
    return false
}
