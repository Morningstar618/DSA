#include <iostream>

using namespace std;

int pivot(const int[], int);

int main() {
    constexpr int arr[] {7, 9, 11, 12, 1, 2, 3};
    const int ans = pivot(arr, 7);

    cout << ans << endl;

    return 0;
}

int pivot(const int arr[], const int size) {
    int s {0}, e = size - 1;
    int mid {s + (e - s) / 2};

    while (s < e) {
        if (arr[mid] >= arr[0]) {
            s = mid + 1;
        } else {
            e = mid;
        }

        mid = s + (e - s) / 2;
    }

    return s;
}