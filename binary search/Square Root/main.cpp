#include <iostream>

using namespace std;

float root(float);

int main() {
    constexpr float x {189.0};
    cout << root(x) << endl;

    return 0;
}

float root(const float num) {
    if (num < 0.0f) {
        // Assuming non-negative input as per original; handle negative as error or NaN if needed
        return -1.0f;
    }
    if (num == 0.0f) {
        return 0.0f;
    }

    float x = num * 0.5f;
    float prev;
    constexpr float epsilon = 1e-6f;

    do {
        prev = x;
        x = (x + num / x) * 0.5f;
    } while ((prev - x > epsilon) || (x - prev > epsilon));

    return x;
}