#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int intlog(int base, int x) {
    return (int)(log(x) / log(base));
}

int tracezero(int n) {
    int result = n / 5;
    int maxpow = intlog(5, n);
    for (int i = 2; i <= maxpow; i++) {
        result += n / pow(5,i);
    }
    return result;
}

int main() {
    int lines;
    cin >> lines;
    vector<int> arr;
    for (int i = 0; i < lines; i++) {
        int inputnumber;
        cin >> inputnumber;
        arr.push_back(inputnumber);
    }
    for (int i = 0; i<lines; i++){
        cout << tracezero(arr[i])<<endl;
    }
    return 0;
}