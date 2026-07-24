// 2026/07/23
func judgeCircle(moves string) bool {
    x := 0
    y := 0
    for i:=0; i<len(moves);i++ {
        switch s := string(moves[i]); s {
            case "U":
                x += 1
            case "D":
                x -= 1
            case "L":
                y -= 1
            case "R":
                y += 1
        }
    }
    if x ==0 && y == 0 {
        return true
    } else {
        return false
    }
}
