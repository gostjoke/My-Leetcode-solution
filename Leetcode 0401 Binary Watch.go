// 2025/12/15
func readBinaryWatch(turnedOn int) []string {
    ans := []string{}
    for h:=0; h < 12; h++ {
        for m:=0; m <60; m++{
        if bits.OnesCount(uint(h))+bits.OnesCount(uint(m)) == turnedOn{ 
                time := fmt.Sprintf("%d:%02d", h, m)
                ans = append(ans, time)
            }
        }
    }
    return ans
}
