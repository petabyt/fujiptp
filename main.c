// Decode PTP packets from Canon software

#include <stdio.h>
#include "ptp.h"

#define HEXDATA

unsigned short code = 0;
unsigned short type = 0;
unsigned int transid = 0;
unsigned int nparam = 0;

int print = 1;

void decodeBulkContainer(FILE *f) {
	PTPUSBBulkContainer a;

	// Get 12 bytes before payload data
	fread(&a, 1, sizeof(a), f);

	if (print) {
		printf("Length: %u\n", a.length);
		printf("Type: %hu\n", a.type);
		printf("Code: %hu (0x%x)\n", a.code, a.code);
		printf("Transfer ID: %u\n", a.trans_id);
		printf("Param: 0x%x\n", a.payload.params.param1);
		printf("Param: 0x%x\n", a.payload.params.param2);
		printf("Param: 0x%x\n", a.payload.params.param3);
		printf("Param: 0x%x\n", a.payload.params.param4);
		printf("Param: 0x%x\n", a.payload.params.param5);
		printf("Payload Data in hex: '");
		for (int i = 0; i < (int)(a.length); i++) {
			printf("%x ", a.payload.data[i]);
		}

		printf("'\n");

		printf("Payload Data: '%s'\n", a.payload.data);
		putchar('\n');
	}

	code = a.code;
	type = a.type;
	transid = a.trans_id;
}

void decodeEventContainer(FILE *f) {
	PTPUSBEventContainer a;

	fread(&a, 1, sizeof(a), f);

	if (print) {
		printf("Length: %u\n", a.length);
		printf("Type: %hu\n", a.type);
		printf("Code: %hu (0x%x)\n", a.code, a.code);
		printf("Transfer ID: %u\n", a.trans_id);
		printf("Param: 0x%x\n", a.param1);
		printf("Param: 0x%x\n", a.param2);
		printf("Param: 0x%x\n", a.param3);
		putchar('\n');
	}

	code = a.code;
	type = a.type;
	transid = a.trans_id;
}

void decodeContainer(FILE *f) {
	PTPContainer a;

	fread(&a, 1, sizeof(a), f);

	if (print) {
		printf("Code: %hu (0x%x)\n", a.Code, a.Code);
		printf("Session ID: %u\n", a.SessionID);
		printf("Transaction ID: %u\n", a.Transaction_ID);
		printf("Param: 0x%x\n", a.Param1);
		printf("Param: 0x%x\n", a.Param2);
		printf("Param: 0x%x\n", a.Param3);
		printf("Param: 0x%x\n", a.Param4);
		printf("Param: 0x%x\n", a.Param5);
		printf("NParam: %d\n", (char)a.Nparam);
		putchar('\n');
	}

	code = a.Code;
	type = 0;
	transid = a.Transaction_ID;
	nparam = a.Nparam;
}

// Current search packet target
#define CURTEST decodeBulkContainer

int main(int argc, char *argv[]) {
	if (argc != 2) {
		return 1;
	}

	// Don't print
	print = 0;

	// Where to store matched addresses
	int addrs[100000];
	int addrlen = 0;

	FILE *f = fopen(argv[1], "r");

	// Read through file, find matches
	int i = 0;
	while (!feof(f)) {
		fseek(f, i, SEEK_SET);
		CURTEST(f);

		int filter = 1;

		// Look for Canon calls
		filter &= code >> 8 == 0x90 || code >> 8 == 0x91;

		// Avoid too high transaction IDs (Typically 0-300)
		filter &= transid < 300;

		if (filter) {
			addrs[addrlen] = i;
			addrlen++;
		}
		
		i++;
	}

	print = 1;

	if (addrlen == 0) {
		puts("!!!!! No matches found");
	}

	for (int i = 0; i < addrlen; i++) {
		printf("\n!!!!! Offset: %d\n", addrs[i]);
		fseek(f, addrs[i], SEEK_SET);
		CURTEST(f);
	}

	fclose(f);
}
