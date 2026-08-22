// 2026/08/22
func checkDivisibility(n int) bool {
    dig_sum := 0
    dig_pro := 1
    for _, ch := range strconv.Itoa(n) {
        a := int(ch - '0')
        dig_sum += a
        dig_pro *= a
    }
    return n % (dig_sum+dig_pro) == 0
}
