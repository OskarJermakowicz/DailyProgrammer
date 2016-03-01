#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

pair<vector<vector<int>>, vector<vector<int>>> obl(vector<vector<int>> m) {
	vector<vector<int>> values(m.size() + m[0].size(), vector<int>(m.size()));
	vector<vector<int>> mapping(m.size() + m[0].size(), vector<int>(m.size()));

	// Add diagonals that start at row 0
	for (int i = 0; i < m[0].size(); i++) {
		int row = 0;

		for (int j = i; j > -1; j--) {
			values[i][row] = m[row][j];
			mapping[i][row] = 1;
			++row;
		}
	}

	// Add diagonals that do not start at row 0
	for (int i = 1; i < m.size(); i++) {
		int row = i;

		for (int j = m.size() - 1; j > m.size() - row - 1; j--) {
			values[i + m.size() - 1][row - 1] = m[row][j];
			mapping[i + m.size() - 1][row - 1] = 1;
			++row;
		}
	}

	pair<vector<vector<int>>, vector<vector<int>>> result(values, mapping);
	return result;
}

pair<vector<vector<int>>, vector<vector<int>>> deobl(pair<vector<vector<int>>, vector<vector<int>>> matrix) {
	vector<vector<int>> values = matrix.first;
	vector<vector<int>> mapping = matrix.second;
	
	return matrix;
}

void printMatrix(pair<vector<vector<int>>, vector<vector<int>>> matrix, bool diagonal) {
	vector<vector<int>> values = matrix.first;
	vector<vector<int>> mapping = matrix.second;
	for (int i = 0; i < values.size(); i++) {
		for (int j = 0; j < values[i].size(); j++) {
			if (mapping[i][j] == 1 || !diagonal) {
				cout << "\t" << values[i][j];
			}
		}
		cout << endl;
	}
}

int main() {
	vector<vector<int>> matrix(6, vector<int>(6));

	ifstream in("input.txt");
	if (!in) {
		cout << "File cannot be opened.\n";
		return 0;
	}
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			in >> matrix[i][j];
		}
	}
	in.close();
	
	pair<vector<vector<int>>, vector<vector<int>>> initialMatrix(matrix, matrix);
	printMatrix(initialMatrix, false);
	cout << endl;

	pair<vector<vector<int>>, vector<vector<int>>> oblMatrix = obl(matrix);
	printMatrix(oblMatrix, true);
	cout << endl;

	//pair<vector<vector<int>>, vector<vector<int>>> deoblMatrix = deobl(oblMatrix);
	//printMatrix(deoblMatrix, true);
}