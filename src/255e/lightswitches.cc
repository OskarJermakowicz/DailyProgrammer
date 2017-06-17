#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>

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
	int starttime = clock();

	int switches;
	vector<int> from;
	vector<int> to;

	fstream inputfile("challengeinput.txt", ios_base::in);
	
	inputfile >> switches;

	int f, t;
	while (inputfile >> f >> t) {
		from.push_back(f);
		to.push_back(t);
	}

	solve(switches, from, to);

	cout << "\n*** Execution time: " << (clock() - starttime) / double(CLOCKS_PER_SEC) * 1000 << endl;
}