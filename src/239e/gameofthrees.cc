#include <iostream>

using namespace std;

void solve(int input) {
	while (input != 1) {
		if (input % 3 == 0) {
			cout << input << "\t0" << endl;
			input /= 3;
		}
		else if ((input + 1) % 3 == 0) {
			cout << input << "\t1" << endl;
			input++;
		}
		else if ((input - 1) % 3 == 0) {
			cout << input << "\t-1" << endl;
			input--;
		}
	}
	cout << input << endl;
}

int main() {
	int input = 31337357;
	solve(input);
}