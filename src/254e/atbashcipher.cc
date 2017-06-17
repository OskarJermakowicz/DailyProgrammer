#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string encode(string text) {
	for (int i = 0; i < text.length(); i++) {
		if (text[i] >= 'a' && text[i] <= 'z') {
			text[i] = 'z' - (text[i] - 'a');
		}
	}
	return text;
}

int main() {
	ifstream inputfile("input.txt");

	string line;
	while (getline(inputfile, line)) {
		cout << encode(line) << endl;
	}
}