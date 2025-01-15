func findLUSlength(a string, b string) int {
    if a == b {
        return -1
    } else{
        return int(math.Max(float64(len(a)), float64(len(b))))
    }
}
