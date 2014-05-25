all:
	g++ -c -fPIC BigInt.cpp
	g++ -shared -o libbigint.so bigInt.o
	LD_LIBRARY_PATH=./ g++ main.cpp -lbigint -I. -Wl,-rpath,. -L. -o BigInt
	
windows:
	g++ -c BigInt.cpp
	g++ -shared -o BigInt.dll BigInt.o
	g++ main.cpp BigInt.dll -I. -Wl,-rpath,. -L. -o BigInt.exe
#-------------------------------------------------------------->#
Python_Win64:
	swig -c++ -python BigInt.i
	C:\TDM-GCC-64\bin\g++ -c BigInt.cpp
	C:\TDM-GCC-64\bin\g++ -c bigInt_wrap.cxx -IC:\Python27\include
	C:\TDM-GCC-64\bin\g++ BigInt.o bigInt_wrap.o -Ic:\python27\include -Lc:\python27\libs -lpython27 -shared -o _BigInt.pyd
Python_U:	
	swig -c++ -python BigInt.i
	g++ -fPIC -c BigInt.cpp
	g++ -fPIC -c BigInt_wrap.cxx -I/usr/include/python2.7
	g++ -shared BigInt.o BigInt_wrap.o -o _BigInt.so
	
	