// 2025/07/09

func countSegments(s string) int {
    a := strings.Split(s, " ")
    count := 0
    for _, i := range a{
        if i != ""{
            count++
        }
    }

    return count
}
