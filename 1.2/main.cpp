#include <bits/stdc++.h>
using namespace std;
void addto(vector<int> &sums, vector<int> &outs) {
    for (int sum : sums) {
        outs.push_back(outs.back() + sum);
    }
}
bool hasDup(vector<int> &outs, int l) {
    vector<int> outSort = outs;
    sort(outSort.begin(), outSort.end());
    for (int i = l; i < outs.size(); i++) {
        auto occ = distance(outSort.begin(),find(outSort.begin(), outSort.end(), outs[i]));
        if (outSort[occ] == outSort[occ+1]) {
            cout << outSort[occ];
            return true;
        }
    }
    return false;
}
int main() {
    string file = "../in.txt";
    ifstream in(file.c_str());
    string str;
    vector<int> sums;
    int l = 1;
    while (getline(in, str)) {
        l++;
        sums.push_back(stoi(str));
    }
    in.close();
    vector<int> outs = {0};
    bool dup = false;
    int a = 0;
    while (!dup) {
        cout << a << endl;
        addto(sums, outs);
        dup = hasDup(outs, l*a);
        a++;
    }

}