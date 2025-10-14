#include <iostream>

using namespace std;

int pivot(const int[], int);
int search(const int[], int, int);

int main() {
    constexpr int arr[] {7, 9, 11, 12, 1, 2, 3, 5};
    const int ans = search(arr, 8, 3);

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

int search(const int arr[], const int size, const int key) {
    const int p = pivot(arr, size);
    int ans {-1};

    int s {0}, e = size - 1;

    if (arr[p] > key) {
        e = p - 1;
    } else if (arr[p] < key) {
        s = p;
    } else {
        return p;
    }

    int mid {s + (e - s) / 2};

    while (s <= e) {
        if (arr[mid] > key) {
            e = mid;
        } else if (arr[mid] < key) {
            s = mid;
        } else {
            ans = mid;
            break;
        }

        mid = s + (e - s) / 2;
    }

    return ans;
}