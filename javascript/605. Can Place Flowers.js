/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {

    let i = 0;
    while (i < flowerbed.length) {
        if (flowerbed[i] == 0) {
            let leftcheck = false;
            let rightcheck = false;

            if (i == 0)
                leftcheck = true;
            else {
                if (flowerbed[i - 1] == 0)
                    leftcheck = true
            }
            if (i == flowerbed.length - 1)
                rightcheck = true;
            else {
                if (flowerbed[i + 1] == 0)
                    rightcheck = true
            }
            if (rightcheck && leftcheck) {
                flowerbed[i] = 1;
                n = n - 1;
            }

        }
        i += 1;
    }
   
        return n <= 0;

};