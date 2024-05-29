// 5282024
func singleNumber(nums []int) int {
    mymap := make(map[int]int)
    for _, i := range nums{
        if _, exists := mymap[i]; exists{
            mymap[i] += 1
        }else{
            mymap[i] = 1
        }
    }
    for key, value := range mymap{
        if value == 1{
            return key
        }
    }
    return -1
}
