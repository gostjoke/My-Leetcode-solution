// 2025/01/03
func minElement(nums []int) int {
	ans := 10000
	for _, n := range nums {
		tmp := 0
		// 將 n 轉換為字符串
		for _, i := range strconv.Itoa(n) {
			// 將字符轉換為數字
			tmp += int(i - '0') // '0' 是字符 0 的 ASCII 值
		}
		if tmp < ans {
			ans = tmp
		}
	}
	return ans
}
