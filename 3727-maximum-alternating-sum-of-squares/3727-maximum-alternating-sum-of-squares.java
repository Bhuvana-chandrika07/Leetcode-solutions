class Solution {
    public long maxAlternatingSum(int[] nums) {
        long arr[]=new long[nums.length];
        for(int i=0;i<nums.length;i++){
            arr[i]=nums[i]*nums[i];
        }
        Arrays.sort(arr);
        long ans=0;
        int l=0;
        int r=nums.length-1;
        if(nums.length%2!=0){
            ans+=arr[nums.length/2];
        }
        while(l<r){
            ans+=(arr[r]-arr[l]);
            l++;
            r--;
        }
        return ans;
    }
}