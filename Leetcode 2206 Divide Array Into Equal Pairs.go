// 2026/08/20

func divideArray(nums []int) bool {
    n_map := make(map[int]int)
    for _, num := range nums{
        n_map[num] ++
    }
    // fmt.Println(n_map)
    for _, c := range n_map {
        if c % 2 == 1 {
            return false
        }
    }

    return true
}
