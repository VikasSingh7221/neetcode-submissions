class Solution {
public:
    bool isPalindrome(string data) {
        int n = data.size();

        string s = "";
        string t = "";

        for (int i = 0; i < n; i++) {

            
            if(isalnum(data[i])){
                if (data[i] != ' ') {
                    s += tolower(data[i]);
                }
            }

            if(isalnum(data[n-1-i])){
                if (data[n - 1 - i] != ' ') {
                    t += tolower(data[n - 1 - i]);
                }
        }
            }

            
        cout<<s<<endl;
        cout<<t<<endl;
        if (s == t) {
            return true;
        }

        return false;
    }
};