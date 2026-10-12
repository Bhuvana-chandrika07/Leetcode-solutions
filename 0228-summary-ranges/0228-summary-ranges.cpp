class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
    vector<string> s;
    if(nums.size() == 0) return {};
    // long long prev = nums[0];
    
    // string temp = to_string(nums[0]);
    // temp += "->";
    long long n = nums.size();
    // long long next =  prev;
    int start = 0;
    int end = 1;
    int diff = 1;
    while(end<n){
        if( (abs(long(nums[start]) - long (nums[end]))) == diff){
            diff++;
            end++;
        }
        else{
            string temp;
            if(start == end-1){
               temp = to_string(nums[start]);
            }
            else  temp = to_string(nums[start]) + "->" + to_string(nums[end-1]);
            diff = 1;
            s.push_back(temp);
            start = end;
            end++;
        }

    }
       string temp;
    if(start == end-1) temp = to_string(nums[start]);
            
    else  temp = to_string(nums[start]) + "->" + to_string(nums[end-1]);
    //  temp = to_string(nums[start]) + "->" + to_string(nums[end-1]);
    s.push_back(temp);
    
    return s;
    }
};