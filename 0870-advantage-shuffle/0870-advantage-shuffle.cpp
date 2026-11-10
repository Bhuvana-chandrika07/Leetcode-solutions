class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        sort(nums1.begin(), nums1.end());

        vector<pair<int, int>> dp;

        

        for(int i = 0; i < n; i++) {
            dp.push_back({nums2[i], i});
        }

        sort(dp.begin(), dp.end());


        int l = 0, r = n - 1;

        for(int i = n - 1; i >= 0; i--) {
            if(nums1[r] > dp[i].first) {
                nums2[dp[i].second] = nums1[r];
                r--;
            } else {
                nums2[dp[i].second] = nums1[l];
                l++;
            }
        }
        return nums2;
    }
};