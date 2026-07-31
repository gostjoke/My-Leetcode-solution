// 2026/07/30
func minimumPushes(word string) int {
    freq := make(map[rune]int)

    for _, c := range word {
        freq[c] ++
    }

    counts := make([]int, 0, len(freq))
    for _, v := range freq{
        counts = append(counts, v)
    }

    slices.SortFunc(counts, func(a, b int) int { return b - a })
    ans := 0
    for index, value := range counts{
        ans += value * (index/8+1) 
    }

    return ans
}
