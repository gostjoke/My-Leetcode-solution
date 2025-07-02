// 2025/07/02

func countPrimes(n int) int {
    if n <= 1{
        return 0
    }
    
    dp := make([]bool, n)
    for i:= 0; i < n; i++{
        dp[i] = true
    }
    dp[0], dp[1] = false, false
    for i:=2; i*i < n; i++{
        if dp[i] == true{
            for j:=i*i; j < n; j+=i{
                dp[j] = false
            }  
        }
    }
    count := 0;
    for _, prime := range dp{
        if prime{
            count += 1
        }
    }
    return count

}
