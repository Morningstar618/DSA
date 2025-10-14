#include <iostream>
#include <vector>

using namespace std;

bool isPossible(const vector<int> &, int, int, int);
int allocateBooks(const vector<int> &, int, int);

int main() {
    const vector<int> vec {10, 20, 30, 40};
    const int n = static_cast<int>(vec.size());
    constexpr int m = 2;

    const int result = allocateBooks(vec, n, m);
    cout << result << endl;

    return 0;
}

bool isPossible(const vector<int> &vec, const int n, const int m, const int mid) {
    int studentCount {1};
    int pageSum {0};

    for (int i = 0; i < n; i++) {
        if (pageSum + vec[i] <= mid) {
            pageSum += vec[i];
        } else {
            studentCount++;
            if (studentCount > m || vec[i] > mid) {
                return false;
            }
            pageSum = vec[i];
        }
    }
    return true;
}

int allocateBooks(const vector<int> &arr, const int n, const int m) {
    int s {0};
    int sum {0};

    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    int e {sum};
    int mid {s + (e - s) / 2};
    int ans {-1};

    while (s <= e) {
        if (isPossible(arr, n, m, mid)) {
            ans = mid;
            e = mid - 1;
        } else {
            s = mid + 1;
        }

        mid = s + (e - s) / 2;
    }

    return ans;
}