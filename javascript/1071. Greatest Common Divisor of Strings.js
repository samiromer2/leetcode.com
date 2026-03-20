/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    if (str1+str2 != str2+str1)
        return "";

    let smaller = Math.min(str1.length, str2.length);
    let hcf = 1;

    for (let i = 1; i <= smaller; i++) {
        if (str1.length % i === 0 && str2.length % i === 0) {
            hcf = i;
        }
    }
    return str1.slice(0,hcf);
};