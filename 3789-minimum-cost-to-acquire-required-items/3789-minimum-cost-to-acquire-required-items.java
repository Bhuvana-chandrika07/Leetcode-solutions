class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long ans = 0;
        if(costBoth >= cost1 + cost2) {
            return (((long)cost1*need1) + ((long)cost2*need2));
        }else{
            int min = Math.min(need1, need2);

            ans += (min*(long)costBoth);

            need1-=min; need2-=min;
            if(need1 > 0){
                if(cost1 > costBoth) ans += ((long)costBoth*need1);
                else ans += ((long)cost1*need1); 
            }else if(need2 > 0){
                if(cost2 > costBoth) ans += ((long)costBoth*need2);
                else ans += ((long)cost2*need2); 
            }
        }

        return ans;
    }
}