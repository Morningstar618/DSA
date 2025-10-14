/****************************** PROBLEM STATEMENT *******************************
* Given a rope of length `n`, and 3 separate length options i.e. `a`, `b` and `c`
* we need to find the maximum combination from the 3 lengths such that they will 
* sum up to the length of the rope `n`.
*
* Example 1: n = 5, a = 2, b = 3, c = 1
* Correct output in this case is 5, i.e. 5 pieces of length `c`.
*
* Time complexity -> Big O(3^n)
*********************************************************************************/
#include <algorithm>
#include <iostream>
using namespace std;

int maxPieces(int n, int a, int b, int c) {
    if (n == 0) return 0;
    if (n < 0) return -1;

    int res = max({maxPieces(n-a,a,b,c), maxPieces(n-b,a,b,c), maxPieces(n-c,a,b,c)});

    if (res == -1) return -1;
    return res + 1;
}

int main() {
    int n {23};
    int a {11};
    int b {9};
    int c {12};

    int ans {0};

    ans = maxPieces(n, a, b, c);
    cout << "Ans: " << ans << endl;

    return 0;
}