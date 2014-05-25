#pragma once
#define BASE 10
#define DEV_BY_ZERO 1
#include <iostream>
#include <vector>
using namespace std;

class BigInt
{
public:
	BigInt();
	BigInt(char* str);
	BigInt(int i);
	~BigInt();

	char* getString();

	bool getFrom_txt(const char* filename);
	bool saveTo_txt(const char* filename);
	bool saveTo_bin(const char* filename);
	bool getFrom_bin(const char* filename);

	bool operator > (const BigInt& B);
	bool operator < (const BigInt& B);
	bool operator <= (const BigInt& B);
	bool operator >= (const BigInt& B);
	bool operator == (const BigInt& B);
	bool operator != (const BigInt& B);

	BigInt operator +(const BigInt& B) const;	
	BigInt operator -(const BigInt& B) const;	
	BigInt operator -()const;					  
	BigInt operator *(const BigInt& B) const;
	BigInt operator /(const BigInt& B) const;
	BigInt operator %(const BigInt& B) const;
	BigInt operator ^(const BigInt& B) const;

	BigInt operator +=(const BigInt& B); 	   
	BigInt operator -=(const BigInt& B);	   
	BigInt operator *=(const BigInt& B);	   
	BigInt operator /=(const BigInt& B);		
	BigInt operator %=(const BigInt& B);		
	BigInt operator ^=(const BigInt& B);	   

	BigInt operator ++();	  
	BigInt operator --();	  
	BigInt operator ++(int);   
	BigInt operator --(int); 

	char* __str__();		//for Python //output
	char* __repr__();
	

private:
	vector<int> elements;
	int sign;

	void DelZeros();	
	void ShiftRight();	

	friend int cmp(BigInt A, BigInt B);	

};

