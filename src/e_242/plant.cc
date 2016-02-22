#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void solve(vector<int> people, vector<int> fruits) {
	for (int i = 0; i < people.size(); i++) {
		int weeks = 1;
		int totalfruits = 0;
		int temp_fruits = fruits[i];
		while (totalfruits < people[i]) {
			++weeks;
			totalfruits += temp_fruits;
			temp_fruits += totalfruits;
		}
		cout << weeks << endl;
	}
}

int main() {
	vector<int> people;
	vector<int> fruits;

	fstream inputfile("input.txt", ios_base::in);

	int p, f;
	while (inputfile >> p >> f) {
		people.push_back(p);
		fruits.push_back(f);
	}

	solve(people, fruits);
}