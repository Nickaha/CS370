/******************************************
Names: Dave Taveras, Marjan Chowdry, Nick Guo
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Assignment: Hw1: Large Sums
Date: February 9th, 2021
Course: CS370: Creative Problem Solving
*******************************************/

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

string reverse(string str){
	//Function to reverse string numbers to imitate right to left addition
	if(str.size() == 0){
		return "";
	}
	int front = 0;
	int back = str.size() - 1;
	while(front < back){
		int temp = str[front];
		str[front] = str[back];
		str[back] = temp;
		front++;
		back--;
	}
	return str;
}

void largeSum(){
	ifstream input;
	//open the file we wish to read from (assume it always works)
	input.open("input.txt");
	string total = "";
	string line = "";
	string rnum = "";
	//Start reading numbers line by line
	while(getline(input, line)){

		//istringstream used to remove newline char from lines read
		istringstream snum(line);
		snum >> rnum;

		//reverse strings we wish to add since adding is done right to left
		string num = reverse(rnum);
		string curr_total = reverse(total);

		//carry variable for carry over addition
		int carry = 0;
		string temp_sum = "";
		if(num.size() > curr_total.size()){
			/*if the size of the number we are adding to 
			the total is greater than the size of the total*/
			temp_sum = num;
			for(int i = 0; i < num.size(); i++){
				if(i < curr_total.size()){
					/*if the total number can still be indexed use it*/
					int sum = carry + (curr_total[i]-'0') + (num[i]-'0');
					int remander = sum % 10;
					carry = sum/10;
					temp_sum[i] = remander + '0';
				}else{
					/*if the total number is out of bounds don't use it*/
					int sum = carry + (num[i]-'0');
					int remander = sum % 10;
					carry = sum/10;
					temp_sum[i] = remander + '0';
				}
			}
		}else{
			/*if the size of the total number is greater than 
			  or equal to the size of the number 
			  we wish to add to the total*/
			temp_sum = curr_total;
			for(int i = 0; i < curr_total.size(); i++){
				if(i < num.size()){
					/*If the number we wish to add to total can still be indexed use it*/
					int sum = carry + (curr_total[i]-'0') + (num[i]-'0'); 			
					int remander = sum % 10;
					carry = sum/10;
					temp_sum[i] = remander + '0';
				}else{
					/*If the number we wish to add to the total is out of bounds
					  don't use it*/
					int sum = carry + (curr_total[i]-'0');
					int remander = sum % 10;
					carry = sum/10;
					temp_sum[i] = (remander + '0');
				}
			}
		}
		//add remaining carry value to the end of the number 
		if(carry > 0){
			temp_sum += (carry + '0');
			carry = 0;
		}
		total = reverse(temp_sum);
	}
	//close file we read from
	input.close();

	//Remove leading zeros from final result
	bool seen_non_zero = false;
	string no_leading_zeros = "";
	for(int i = 0; i < total.size(); i++){
		if(seen_non_zero == true){
			no_leading_zeros += total[i];
		}
		if(total[i]-'0' > 0 && seen_non_zero == false){
			seen_non_zero = true;
			no_leading_zeros += total[i];
		}
	}
	// if the input file was empty result should be 0
	if(no_leading_zeros.size() == 0){
		no_leading_zeros += '0';
	}
	//output the results in the desired format
	cout << "Full sum: " << no_leading_zeros << endl;
	int i = 0;
	string ten_total = "";
	while(i < no_leading_zeros.size() && i < 10 ){
		ten_total += no_leading_zeros[i];
		i++;
	}
	cout << "First 10 digits: " << ten_total;
}


int main(){
	largeSum();
}