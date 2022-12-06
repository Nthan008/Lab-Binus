all: mylib.o
	gcc -o main.exe main_test.c mylib.o

mylib.o:
	gcc -o mylib.o -c mylib/mylib.c
clear:
	rm -rf *.out
	rm -rf *.o

time-recursive: mylib.o 
	gcc -o main_b_time_recursive.exe main_b_time_recursive.c mylib.o

time-iterative: mylib.o
	gcc -o main_b_time_iterative.exe main_b_time_iterative.c mylib.o

space-recursive: mylib.o 
	gcc -o main_b_space_recursive.exe main_b_space_recursive.c mylib.o 

space-iterative: mylib.o
	gcc -o 	 main_b_space_iterative.c mylib.o	