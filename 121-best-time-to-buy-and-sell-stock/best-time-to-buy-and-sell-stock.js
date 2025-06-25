/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minValue = prices[0]
    let maxProfit = 0
    for (let i=1;i<prices.length;i++) {
        if (prices[i]-minValue > maxProfit) {
            maxProfit = prices[i] - minValue
        }
        if(prices[i]<minValue) {
            minValue = prices[i]
        }
    }
    return maxProfit
};


// Brute force: Two for loops -> calculate profits for each and every index ie.. all possible combinations. But this will make time complexity O(n2)

//Alternate approach
// 1. we need to keep track of the min price of buying
// to get maxProfit we need to get the min price
// 2. loop through each element and keep track of minValue and calcuate maxProfit