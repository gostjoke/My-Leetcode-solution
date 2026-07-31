// 2026/07/31

func rotateString(s string, goal string) bool {
    return strings.Contains(goal+goal, s)
}
