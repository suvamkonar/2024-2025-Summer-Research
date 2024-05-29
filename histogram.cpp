#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

// FILE OPENING
ifstream fin;
ofstream fout;
string InputFileName;
string OutputFileName;
void setIOOpen(string name) {

	InputFileName = name + ".txt";
	OutputFileName = "cpp_histogram.txt";

	fout.open(OutputFileName, ios::out | ios::trunc);

	if (!fout) {
		fout << "Unable to open file \n";
		exit(1); // terminate with error
	}

	fin.open(InputFileName, ios::in);

	if (!fin) {
		fout << "Unable to open file \n";
		exit(1); // terminate with error
	}
}
//FILE CLOSING
void setIOClose()
{ 
	fin.close();
	fout.close();
}


int numInterval;
int amountData;

vector<pair<int,int>> intervals;
vector<int> dataHolder;

void read()
{
    int a; //reads in the number of intervals
	fin >> a;
	numInterval = a;

	int b; //reads in the number of data values
	fin >> b;
	amountData = b;
    
    for(int i = 0; i < numInterval; i++) { // reads in the intervals in form of pairs
		int start;
		int end;
		fin >> start >> end;
		intervals.push_back( make_pair(start, end) );
	}

	for(int i = 0; i < amountData; i++) { //reads in the raw data itself
		int value;
		fin >> value;
		dataHolder.push_back(value);
	}

	sort(dataHolder.begin(), dataHolder.end()); //sort the data
}

void build() 
{
	cout << "Test";
	vector<int> intervalFreqs;

    for (int i = 0; i < intervals.size(); i++) { //goes through the intervals
		int start = intervals[i].first; // start of interval
		int end = intervals[i].second; //end of interval

		int frequency = 0; //how many data values are in current interval

		for (int value: dataHolder) {
			if(start <= value && value <= end) {
				frequency++;
			}
		}

		intervalFreqs.push_back(frequency); // enters frequency for the interval
	}

	// MAKING HISTOGRAM
	cout << "DATA HISTOGRAM";
    for (int i = 0; i < intervals.size(); i++) { //goes through the intervals
		int start = intervals[i].first; // start of interval
		int end = intervals[i].second; //end of interval
		fout << start << "-" << end;

		fout.width(2); 
        fout << " | "; 
		
		int freq = intervalFreqs[i];
		for(int j = 0; j < freq; j++) {
			fout << " x "; 
		}

		fout << endl;

	}
    fout << "---------------------------------------" << endl; 
    fout << "    "; 
  
  
}

int main()
{
	setIOOpen("data");
	read();
    build();
    setIOClose();
    return 0;
}