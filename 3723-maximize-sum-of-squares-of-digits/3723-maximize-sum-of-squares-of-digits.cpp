
class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        // edge cases
        // A num-digit number can have a maximum digit sum of 9 * num.
        if (sum == 0 || sum > 9 * num) {
            return "";
        }

        string res;

        // greedily construct the maximum res string
        while (num > 0) {
            int digit = min(9, sum);

            res.push_back(char('0' + digit));
            sum -= digit;
            num--;
        }

        // If sum remains, no valid number exists.
        if (sum > 0) {
            return "";
        }

        // The number must have exactly the requested digit sum.
        return res;
    }
};