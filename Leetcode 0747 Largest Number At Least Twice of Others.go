// 2026/08/17
func dominantIndex(nums []int) int {
    max_n := 0
    s_max_n := 0
    max_index := 0
    for index, i := range nums {
        if i > max_n {
            s_max_n = max_n
            max_n = i
            max_index = index
        } else if i > s_max_n {
            s_max_n = i
        }
    }

    if s_max_n != 0 {
        if (max_n / s_max_n) >= 2.0  {
            return max_index
        } else {
            return -1
        }
    } else {
        if s_max_n == max_n {
            return -1
        } else {
            return max_index
        }
    }
}
