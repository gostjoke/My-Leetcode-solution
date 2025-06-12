/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    if (s == null || s[0]=="0"){
        return 0
    };
    n = s.length 
    dp = []
    for (var i=0; i<n+1; i++)
    {
        dp.push(0)
    }
    
    dp[0] = 1
    dp[1] = 1

    for (var i=2; i<n+1; i++)
    {
        var one_dig = parseInt(s[i-1]) 
        var two_dig = parseInt(s.slice(i-2, i))
        if (one_dig >=1 && one_dig <=9){
            dp[i] += dp[i - 1]
        }
        if (two_dig >=10 && two_dig <=26){
            dp[i] += dp[i - 2]
        }
    }
    
    return dp[n]
};
