// 2026/08/10
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    const n = nums.length
    nums.sort((a,b)=>a-b)
    return Math.max(nums[n-1]*nums[n-2]*nums[n-3], nums[n-1]*nums[0]*nums[1])
};
