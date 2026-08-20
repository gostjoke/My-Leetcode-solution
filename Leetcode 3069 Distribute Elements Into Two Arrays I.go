// 2026/08/20

func resultArray(nums []int) []int {
    var arr1 []int
    var arr2 []int
    arr1 = append(arr1, nums[0])
    arr2 = append(arr2, nums[1])
    
    for _, i := range nums[2:len(nums)]{
        if arr1[len(arr1)-1] > arr2[len(arr2)-1] {
            arr1 = append(arr1, i)
        } else{
            arr2 = append(arr2, i)
        }
    }

    return append(arr1, arr2...)
}
