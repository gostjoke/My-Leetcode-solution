// 20250716
func isAnagram(s string, t string) bool {
    s1 := strings.Split(s, "")
    t1 := strings.Split(t, "")
    sort.Strings(s1)
    sort.Strings(t1)

    s2 := strings.Join(s1, "")
    t2 := strings.Join(t1, "")
    if s2 == t2 {
        return true
    } else {
        return false
    }

}
