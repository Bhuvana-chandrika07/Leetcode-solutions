class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<string> ans(m, "." + string(n - 1, '#'));
        ans.back() = string(n, '.');
        return ans;
    }
};