/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let max = candies[0];
    let i = 0;
    while (i < candies.length)
    {
        if (candies[i] > max)
            max = candies[i];
        i++;
    }
    const output = [];
    i=0;
    while (i< candies.length)
    {
        if ((candies[i]+extraCandies) >= max)
             output.push(true);
        else 
            output.push(false);
        i++;
    }
    return output;
};