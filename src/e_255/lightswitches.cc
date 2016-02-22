#include <iostream>
#include <vector>

using namespace std;

void solve(int switches, vector<int> from, vector<int> to) {
	vector<int> bulbstate;

	for (int i = 0; i < switches; i++) {
		bulbstate.push_back(-1);
	}

	for (int i = 0; i < from.size(); i++ ) {
		if (from[i] < to[i]) {
			for (int j = from[i]; j < (to[i] + 1); j++) {
				bulbstate[j] *= -1;
			}
		} else if (from[i] == to[i]) {
			bulbstate[from[i]] *= -1;
		} else {
			for (int j = to[i]; j < (from[i] + 1); j++) {
				bulbstate[j] *= -1;
			}
		}
	}

	int count = 0;
	for (int i = 0; i < bulbstate.size(); i++) {
		if (bulbstate[i] == 1) {
			++count;
		}
	}
	cout << count << endl;
}

int main() {
	int switches = 10;
	vector<int> from;
	vector<int> to;
	
	from.push_back(3);
	from.push_back(0);
	from.push_back(7);
	from.push_back(9);

	to.push_back(6);
	to.push_back(4);
	to.push_back(3);
	to.push_back(9);

	solve(switches, from, to);
}