/******************************************
Names: Dave Taveras, Marjan Chowdhury, Nick Guo
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Assignment: Hw2: Substring Divisibility
Date: February 16th, 2021
Course: CS370: Creative Problem Solving
*******************************************/
import java.util.Arrays;

public class SubstringDivisibility{


	static boolean isNextPermute(char[] str){
		// A function to find next lexicographic permutation of a string
		// Based on Lexicographic permute algorithm from CS-385
		int size = str.length;
		int k = 0;
		for(k = size-2; k >=0; k--){
			if(str[k]-'0' < str[k+1]-'0'){
				break;
			}
		}
		if(k == -1){
			return false;
		}
		int j = size-1;
		while(str[k]-'0' > str[j]-'0'){
			j--;
		}
		char temp = str[j];
		str[j] = str[k];
		str[k] = temp;	

		for(int q = size-1, p = k+1; q>p; q--, p++){
			temp = str[q];
			str[q] = str[p];
			str[p] = temp;
		}
		return true;
	}


	static void substringDivisibility(String str){
		long start = System.nanoTime();

		//Convert input string to char array and sort it
		char[] input = str.toCharArray();
		Arrays.sort(input);

		//initialize variables 
		long sum = 0;
		int size = str.length();
		//A while loop to generate all permutations
		// check initial input
		for(int i = 0; i < 1; i++){
			if(((input[3]-'0') % 2) != 0){
				continue;
			}
			//if size 5, digits 3,4,5 are divisible by 3
			//Follows mathematical property that digits 3+4+5 
			//should be divisible by 3
			if(size >= 5){
				if((((input[2]-'0') + (input[3]-'0') + (input[4]-'0')) % 3) != 0){
					continue;
				}
			}
			//if size 6, digits 4,5,6 are divisible by 5
			if(size >= 6){
				//only need to check 6th digit 
				if(((input[5]-'0') % 5) != 0){
					continue;
				}
			}
			//if size 7, digits 5,6,7 are divisible by 7
			if(size >= 7){
				if((((input[4]-'0')*100 + (input[5]-'0')*10 + (input[6]-'0')) % 7) != 0){
					continue;
				}
			}
			//if size 8, digits 6,7,8 are divisible by 11
			if(size >= 8){
				if((((input[5]-'0')*100 + (input[6]-'0')*10 + (input[7]-'0')) % 11) != 0){
					continue;
				}
			}
			//if size 9, digits 7,8,9 are divisible by 13
			if(size >= 9){
				if((((input[6]-'0')*100 + (input[7]-'0')*10 + (input[8]-'0')) % 13) != 0){
					continue;
				}
			}
			//if size 10, digits 8,9,10 are divisible by 17
			if(size == 10){
				if((((input[7]-'0')*100 + (input[8]-'0')*10 + (input[9]-'0')) % 17) != 0){
					continue;
				}
			}
			//If we get this far, that means all properties were satisfied
			System.out.println(input);
			sum += Long.parseLong(new String(input));
		}
		while(isNextPermute(input)){
			//For all inputs, the property, digits 2,3,4 is divisible by 2 will be checked
			//Only need to check 4th digit anyways
			if(((input[3]-'0') % 2) != 0){
				continue;
			}
			//if size 5, digits 3,4,5 are divisible by 3
			//Follows mathematical property that digits 3+4+5 
			//should be divisible by 3
			if(size >= 5){
				if((((input[2]-'0') + (input[3]-'0') + (input[4]-'0')) % 3) != 0){
					continue;
				}
			}
			//if size 6, digits 4,5,6 are divisible by 5
			if(size >= 6){
				//only need to check 6th digit 
				if(((input[5]-'0') % 5) != 0){
					continue;
				}
			}
			//if size 7, digits 5,6,7 are divisible by 7
			if(size >= 7){
				if((((input[4]-'0')*100 + (input[5]-'0')*10 + (input[6]-'0')) % 7) != 0){
					continue;
				}
			}
			//if size 8, digits 6,7,8 are divisible by 11
			if(size >= 8){
				if((((input[5]-'0')*100 + (input[6]-'0')*10 + (input[7]-'0')) % 11) != 0){
					continue;
				}
			}
			//if size 9, digits 7,8,9 are divisible by 13
			if(size >= 9){
				if((((input[6]-'0')*100 + (input[7]-'0')*10 + (input[8]-'0')) % 13) != 0){
					continue;
				}
			}
			//if size 10, digits 8,9,10 are divisible by 17
			if(size == 10){
				if((((input[7]-'0')*100 + (input[8]-'0')*10 + (input[9]-'0')) % 17) != 0){
					continue;
				}
			}
			//If we get this far, that means all properties were satisfied
			System.out.println(input);
			sum += Long.parseLong(new String(input));
		}
		//Print results
		System.out.println("Sum: " + sum);
		System.out.printf("Elapsed time: %.6f ms\n" , (System.nanoTime() - start) / 1e6);
	}

	public static void main(String[] args){
		//We can assume all inputs are valid
		substringDivisibility(args[0]);
	}
}


