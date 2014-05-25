import sys
import BigInt 

def PrintStart():
	print"Program TCHMK.\n"
	print"Enter the input parameters:\n"
	print"\n<name of program> <filename A> <operation>\n<filename B> <result filename C> [b] [filename with module]\n\n"
	print"Parametr: \n"
	print"\"-b\" - binfile\n"
	print"Operations: \n"
	print"\"+\" - addition\n"
	print"\"-\" - subtraction\n"
	print"\"*\" - multiplication\n"
	print"\"/\" - division\n"
	print"\"%%\" - taking the remainder\n"		 
	print"\"^\" - involution (pow)\n"
	sys.exit(-1)

print"Program TCHMK.\n"

fileA = sys.argv[1]
operation = sys.argv[2]
fileB =sys.argv[3]
fileC = sys.argv[4]
bin = False

if len(sys.argv) < 5 or len(sys.argv) > 6:
	PrintStart();

elif len(sys.argv) == 6:

	 if sys.argv[5] == "-b":
		 bin  = True;

print"fileA :",fileA;
print"operation :",operation;
print"fileB :",fileB;
print"fileC :",fileC;
print"bin :",bin;

a = BigInt.BigInt()
b = BigInt.BigInt()
c = BigInt.BigInt()

if bin == True:
	a.getFrom_bin(fileA)
	b.getFrom_bin(fileB)
else:
	a.getFrom_txt(fileA)
	b.getFrom_txt(fileB)

if operation == "+":
	c = a + b;
elif operation == "-":
	c = a - b;
elif operation == "*":
	c = a * b;
elif operation == "/":
	c = a / b;
elif operation == "%":
	c = a % b;
elif operation == "^":
	c = a ^ b;
else:
	PrintStart()
	
print"a = ",a
print"b = ",b
print"c = ",c

if bin == False:
	c.saveTo_txt(fileC)
else:
	c.saveTo_bin(fileC)




