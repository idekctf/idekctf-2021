#include <stdio.h> 
#include <stdlib.h>
#include "md5.h"
#include <openssl/md5.h>
#include <string.h>

long long int benzene(long long int product);
long long int NBS(long long int product); 
long long int diels(long long int product); 
long long int SOCl2(long long int product);
long long int decarb(long long int product);
long long int aldol(long long int product);
long long int favorsky(long long int product);

void compute_md5(char *str, unsigned char digest[16]);
int va(char *str1, char *str2); 
void pf(void); 

void compute_md5(char *str, unsigned char digest[16]) {
    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, str, strlen(str));
    MD5_Final(digest, &ctx);
}

int va(char *str1, char *str2) {
	int diff;
	for (int i = 0; i < 16; i++) {
		diff = str1[i] - str2[i];
		if (diff != 0) {
			return 0;
		}
	}
	return 1;
}

void pf(void) {
	int num[] = {765, 731, 746, 771, 873, 884, 405, 671, 719, 494, 319, 920, 870, 309, 562, 661, 649, 508, 995, 671, 1010, 555, 156, 65, 926, 186, 816, 908, 222, 146, 205, 885, 366, 318};
	int tri[] = {3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666};
	char fl[35];
	for (int i = 0; i < 34; i++) {
	num[i] = ((num[i] - 33) ^ tri[i]) / 7 ; 
	printf("%c", num[i]);
	}
	printf("\n");
}

long long int benzene(long long int product) {
	product = product + 28550354772583778;
	return product;
}

long long int NBS(long long int product) {
	product = product + 5456462;
	return product;
}

long long int diels(long long int product) {
	product = product ^ 495739824484;
	return product;
}

long long int SOCl2(long long int product) {
	product = product + 216564715347;
	return product;
}

long long int decarb(long long int product) {
	product = product - 310568239917;
	return product;
}

long long int aldol(long long int product) {
	product = product + 465725320289;
	return product;
}

long long int favorsky(long long int product) {
	product = product ^ 8749213636430815590;
	return product;
}

int main(void) {
	// Variable declarations
	long long int result = 8749110455712246664;
	int do_benzene = 0;
	int do_nbs = 0;
	int do_diels = 0;
	int do_SOCl2 = 0;
	int do_decarb = 0;
	int do_aldol = 0;
	int do_favorsky = 0; 
	
	// Banner
	printf("%s\n", "    ____       __                              __  __              _     ");
	printf("%s\n", "   / __ \\___  / /__________  _______  ______  / /_/ /_  ___  _____(_)____");
	printf("%s\n", "  / /_/ / _ \\/ __/ ___/ __ \\/ ___/ / / / __ \\/ __/ __ \\/ _ \\/ ___/ / ___/");
	printf("%s\n", " / _, _/  __/ /_/ /  / /_/ (__  ) /_/ / / / / /_/ / / /  __(__  ) (__  ) ");
	printf("%s\n", "/_/ |_|\\___/\\__/_/   \\____/____/\\__, /_/ /_/\\__/_/ /_/\\___/____/_/____/  ");
	printf("%s\n", "                               /____/                                    ");
	printf("%s\n", "-------------------------------------------------------------------------");
	printf("%s\n", "Note: You do not need to know Chemistry to do this challenge, though it will help :)");
	printf("%s\n", "---------------------------------STATUS----------------------------------");
	
	// Synthesis and functions and print statements
	if (do_benzene == 1) {
		result = benzene(result);
		printf("%s\n", "Math: 28550354772583778 [Done] | Chem: Benzene [Added]");
	} else {
		printf("%s\n", "Math: 28550354772583778 [Not done] | Chem: Benzene [Not added]");
	}
	
	if (do_nbs == 1) {
		result = NBS(result);
		printf("%s\n", "Math: 5456462 [Done] | Chem: NBS [Added]");
	} else {
		printf("%s\n", "Math: 5456462 [Not done] | Chem: NBS [Not added]");
	}
	
	if (do_diels == 1) {
		result = diels(result);
		printf("%s\n", "Math: 495739824484 [Done] | Chem: Diels-Alder Reaction [Done]");
	} else {
		printf("%s\n", "Math: 495739824484 [Not done] | Chem: Diels-Alder Reaction [Not done]");
	}
	
	if (do_SOCl2 == 1) {
		result = SOCl2(result);
		printf("%s\n", "Math: 216564715347 [Done] | Chem: SOCl2 [Added]");
	} else {
		printf("%s\n", "Math: 216564715347 [Not done] | Chem: SOCl2 [Not added]");
	}
	
	if (do_decarb == 1) {
		result = decarb(result);
		printf("%s\n", "Math: 310568239917 [Done] | Chem: Decarboxylation [Done]");
	} else {
		printf("%s\n", "Math: 310568239917 [Not done] | Chem: Decarboxylation [Not done]");
	}
	
	if (do_aldol == 1) {
		result = aldol(result);
		printf("%s\n", "Math: 465725320289 [Done] | Chem: Aldol Reaction [Done]");
	} else {
		printf("%s\n", "Math: 465725320289 [Not done] | Chem: Aldol Reaction [Not done]");
	}
	
	if (do_favorsky == 1) {
		result = favorsky(result);
		printf("%s\n", "Math: 8749213636430815590 [Done] | Chem: Favorskii Reaction [Done]");
	} else {
		printf("%s\n", "Math: 87492136360x0000172e430815590 [Not done] | Chem: Favorskii Reaction [Not done]");
	}
	
	// More banner
	printf("%s\n", "---------------------------------RESULTS---------------------------------");
	printf("%s: %lld\n", "Starting material", 8749110455712246664);
	printf("%s: %lld %s\n", "Desired product", 111524754650467, "Cubane");
	printf("%s: %lld\n", "Obtained product", result);
	
	// Processing
	char sresult[40];
	char sdesired[16] = "111524754650467";
	sprintf(sresult, "%lld", result);
	char part_result[16];
	memcpy(part_result, sresult, 16*sizeof(char));
	// Hashing result
	unsigned char hresult[16];
	char bufresult[sizeof(hresult) * 2 + 1];
	compute_md5(part_result, hresult);
	for (int i = 0, j = 0; i < 16; i++, j+=2) {
		sprintf(bufresult+j, "%02x", hresult[i]);
	}
	bufresult[sizeof(hresult) * 2] = 0;
	// Hashing desired
	unsigned char hdesired[16];
	char bufdesired[sizeof(hdesired) * 2 + 1];
	compute_md5(sdesired, hdesired);
	for (int i = 0, j = 0; i < 16; i++, j+=2) {
		sprintf(bufdesired+j, "%02x", hdesired[i]);
	}
	bufdesired[sizeof(hdesired) * 2] = 0;
	
	printf("%s\n", "-------------------------------------------------------------------------");
	
	// Validation and flag
	int vaf = va(bufresult, bufdesired);
	if (vaf == 1) {
		printf("%s\n", "You synthesized cubane! :D");
		pf(); 
		printf("\n");
		printf("%s\n", "                                                       .:");
		printf("%s\n", "                                                      / )");
		printf("%s\n", "                                                     ( ("); 
		printf("%s\n", "                                                      \\ )");
		printf("%s\n", "      o                                             ._(/_.");
		printf("%s\n", "       o                                            |___%|");
		printf("%s\n", "     ___              ___  ___  ___  ___             | %|");
		printf("%s\n", "     | |        ._____|_|__|_|__|_|__|_|_____.       | %|");
		printf("%s\n", "     | |        |__________________________|%|       | %|");
		printf("%s\n", "     |o|          | | |%|  | |  | |  |~| | |        .|_%|.");
		printf("%s\n", "    .' '.         | | |%|  | |  |~|  |#| | |        | ()%|");
		printf("%s\n", "   /  o  \\        | | :%:  :~:  : :  :#: | |     .__|___%|__.");
		printf("%s\n", "  :____o__:     ._|_|_."    "    "    "._|_|_.   |      ___%|_");
		printf("%s\n", "  '._____.'     |___|%|                |___|%|   |_____(____  )");
		printf("%s\n", "                                                           ( (");
		printf("%s\n", "                                                            \\ '._____.-");
		printf("%s\n", "                                                             '._______.-");
		printf("\n");
		
	} else {
		printf("%s\n", "You did not synthesize the final product! Synthesis failed. :(");
	}

	printf("%s\n", "-------------------------------------------------------------------------");
	
}
