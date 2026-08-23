class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        int i = 0;
        int n = nums.size();
        vector<int> ans(2*n,0);
        for(i=0;i<n;i++){
            ans[i] = nums[i];
        }
        int j;
        for(i=n,j=0;i<2*n,j<n;i++,j++){
            ans[i] = nums[j];
        }
        return ans;
    }
};