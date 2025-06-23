// 20250623
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_num = prices[0];
        int max_diff = 0;
        for (int i=0; i < prices.size(); i++){
            if (prices[i] < min_num){
                min_num = prices[i];
            } 
            else
            {
                max_diff = max(max_diff, prices[i]-min_num);
            }

        }
        return max_diff;
    }
};
