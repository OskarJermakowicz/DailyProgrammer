#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <algorithm>

using namespace std;

vector<string> VOWELS = { "a", "o", "u", "e", "i", "u" };

void disemvowel(string text) {
	string result;
	string vowel;

	for (int i = 0; i < text.length(); i++) {
		if (std::find(VOWELS.begin(), VOWELS.end(), string(1, text[i])) != VOWELS.end()) {
			vowel += text[i];
		} else if (text[i] != ' ') {
			result += text[i];
		}
	}
	std::cout << result << "\n" << vowel << endl;
}

int main() {
	string text = "did you hear about the excellent farmer who was outstanding in his field";
	disemvowel(text);
}