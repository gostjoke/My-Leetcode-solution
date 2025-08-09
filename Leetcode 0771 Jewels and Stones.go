// 20250809
func numJewelsInStones(jewels string, stones string) int {
    dic := make(map[string]bool, len(jewels))
    for _, ch := range jewels{
        dic[string(ch)] = true
    }
    count := 0
    for _, ch := range stones{
        if dic[string(ch)]{
            count += 1
        }
    }
    return count
}

//GPT5 improve to avoid string() convert so many times
func numJewelsInStones(jewels string, stones string) int {
    dic := make(map[rune]struct{}, len(jewels))
    for _, ch := range jewels {
        dic[ch] = struct{}{}
    }

    count := 0
    for _, ch := range stones {
        if _, exists := dic[ch]; exists {
            count++
        }
    }
    return count
}
