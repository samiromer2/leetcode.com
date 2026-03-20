/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    if (1 < word1.length > 100 || 1 < word2.length > 100)
        return -1;
    let i = 0 , j = 0;
    const result = [];
    while (word1.length > i && word2.length > j)
        {
            result.push(word1[i]);
            result.push(word2[j]);
            i++;
            j++;    
        }
        result.push(word1.slice(i));
        result.push(word2.slice(j));
    return result.join("");
};