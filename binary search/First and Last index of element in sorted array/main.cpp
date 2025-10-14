#include <iostream>
#include <vector>

using namespace std;

int firstIndex(const vector<int>&, int);
int lastIndex(const vector<int>&, int);
pair<int, int> func(const vector<int>&, int);

int main() {
    const vector<int> vec {1, 8, 8, 8, 8, 8, 9, 12};
    auto [fst, snd] = func(vec, 8);

    cout << fst << ' ' << snd << endl;

    return 0;
}

int firstIndex(const vector<int>& vec, const int key) {
    int s {0}, e {static_cast<int>(vec.size() - 1)};
    int mid {(s + e) / 2};
    int ans {-1};

    while (s <= e) {
        if (vec[mid] == key) {
            ans = mid;
            e = mid - 1;
        } else if (vec[mid] < key) {
            s = mid + 1;
        } else {
            e = mid - 1;
        }

        mid = s + (e - s) / 2;
    }

    return ans;
}

int lastIndex(const vector<int>& vec, const int key) {
    int s {0}, e {static_cast<int>(vec.size() - 1)};
    int mid {(s + e) / 2};
    int ans {-1};

    while (s <= e) {
        if (vec[mid] == key) {
            ans = mid;
            s = mid + 1;
        } else if (vec[mid] < key) {
            s = mid + 1;
        } else {
            e = mid - 1;
        }

        mid = s + (e - s) / 2;
    }

    return ans;
}

pair<int, int> func(const vector<int>& vec, const int key) {
    pair<int, int> ans {-1, -1};
    ans.first = firstIndex(vec, key);
    ans.second = lastIndex(vec, key);

    return ans;
}