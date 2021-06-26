f ?= ~/Documents/1300d/1300ddump

run:
	@python3 bootdisk.py

build:
	@pip3 install .

ptp:
	@${CC} main.c -o main.o
	@./main.o ${f}
	@rm -rf *.o *.out
