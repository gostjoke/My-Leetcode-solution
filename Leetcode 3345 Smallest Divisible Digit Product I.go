// 2026/08/06

func smallestNumber(n int, t int) int {
    var tp int
    for i:=n; i < 101; i++ {
        tp = 1
        for _, j := range strconv.Itoa(i) {
            tp *= int(j - '0')
        }
        if tp % t == 0{
            return i
        }
    }
    return 0
}
