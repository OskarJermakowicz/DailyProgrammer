#include <iostream>
#include <fstream>

using namespace std;

int main() {
	fstream inputfile("input.txt", ios_base::in);

	int a, b, c, temp;
	while (inputfile >> a) {
		inputfile.get();
		inputfile >> b;
		inputfile.get();
		inputfile >> c;

		if (a <= 12) {
			temp = a;
			a = c;
			c = b;
			b = temp;
		}
		cout << (a < 100 ? "20" : "") << a << '-' << (b < 10 ? "0" : "") << b << '-'
			<< (c < 10 ? "0" : "") << c << endl;
	}
	inputfile.close();
}