// 2025/01/02
func romanToInt(s string) int {
    if len(s) == 0 {
        return 0
        }

    dic := map[string]int{
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "T": 90,
        "G": 900,
        "B": 9,
        "Y": 400,
        "U": 40,
    }

    s = strings.ReplaceAll(s, "IV","IIII")
    s = strings.ReplaceAll(s, "XC","T")
    s = strings.ReplaceAll(s, "CM","G")
    s = strings.ReplaceAll(s, "IX","B")
    s = strings.ReplaceAll(s, "CD","Y")
    s = strings.ReplaceAll(s, "XL","U")

    result := 0
    for _, char := range s {
        result += dic[string(char)]
    }
    return result
}
