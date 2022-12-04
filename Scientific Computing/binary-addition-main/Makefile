CC = gcc

all: main.out

main.out: myutils.o 2602236685.o main.o
	${CC} -o main.out main.o myutils.o 2602236685.o -lm

2602236685.o: my_cra/2602236685.c
	${CC} -Wall -c my_cra/2602236685.c -o 2602236685.o -I.

main.o: main.c
	${CC} -Wall -c main.c -o main.o

myutils.o: utils/myutils.c
	${CC} -Wall -c utils/myutils.c -o myutils.o 

clean:
	rm *.o 
	rm *.out