//2026/03/12
func repeatedCharacter(s string) byte {
    seen := make([]int, 26) 

    for _, i := range(s){
        seen[int(i - 'a')]++
        if seen[int(i - 'a')]==2{
            return byte(i)
        }
    }
    return 0
}
