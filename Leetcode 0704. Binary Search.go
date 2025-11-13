func search(nums []int, t int) int {
    l := 0
    r := len(nums) - 1
    m := 0
    for l <= r {
        m = (l+r)//2
        if (nums[m] == t){
            return m
        } else if (nums[m]<t){
            l = m+1
        } else if (nums[m]>t){
            r = m-1
        }
    }
    return -1
}
