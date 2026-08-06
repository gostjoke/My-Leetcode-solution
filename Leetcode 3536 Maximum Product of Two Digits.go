// 2026/08/06

func maxProduct(n int) int {
    a := [10]int{}
    
    for _, i := range strconv.Itoa(n) {
        s := int(i - '0')
        a[s] += 1
    }
    slices.Reverse(a[:])
    ans := 1
    count := 0 
    for index, num := range(a){
        if num > 1 && count == 0 {
            return (9-index)*(9-index)
        } else if num > 0 {
            ans *= (9-index)
            count += 1
        }
        if count == 2 {
            break
        }
    }
    if count < 2 {
        return 0
    }

    return ans
}
