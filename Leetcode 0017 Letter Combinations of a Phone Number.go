// 2025/07/03

func letterCombinations(digits string) []string {
    ans := make([]string,0)
    l := len(digits)
    if l == 0{
        return ans
    }
    dic := make(map[string][]string)
    dic["2"] = append(dic["2"], []string{"a","b","c"}...)
    dic["3"] = append(dic["3"], []string{"d","e","f"}...)
    dic["4"] = append(dic["4"], []string{"g","h","i"}...)
    dic["5"] = append(dic["5"], []string{"j","k","l"}...)
    dic["6"] = append(dic["6"], []string{"m","n","o"}...)
    dic["7"] = append(dic["7"], []string{"p","q","r","s"}...)
    dic["8"] = append(dic["8"], []string{"t","u","v"}...)
    dic["9"] = append(dic["9"], []string{"w","x","y","z"}...)
    if l == 1{
        for _, a := range dic[string(digits[0])]{
            ans = append(ans, a)
        }
    }   else if l == 2 {
            for _, b := range dic[string(digits[1])]{
                for _, a := range dic[string(digits[0])]{
                    ans = append(ans, a+b)
            }
        }
    }   else if l == 3 {
            for _, c := range dic[string(digits[2])]{
                for _, b := range dic[string(digits[1])]{
                    for _, a := range dic[string(digits[0])]{
                        ans = append(ans, a+b+c)
                    }
                }
            }
        } else if l == 4 {
            for _, d := range dic[string(digits[3])]{
                for _, c := range dic[string(digits[2])]{
                    for _, b := range dic[string(digits[1])]{
                        for _, a := range dic[string(digits[0])]{
                            ans = append(ans, a+b+c+d)
                        }
                    }
                }
            }
        }


    return ans // 暫時 return nil，避免編譯錯誤
}
