#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int roll(int n){
    if (n <= 1)
        return n;
    return roll(n-1) + roll(n-2);
}
void main(){
        char key[32];
        printf("I can't just let anyone in, what's the password?\n");
        scanf("%s",key);
        //idek{n3v3R_r01l_uR_oWn_c1ph3r5}\0
        char keygen[32] = "+'(/@5]Ej6X-\"|'CRQyfF2PVSc[Wg,G_";
        for (int i=0; i<32; i++){
                int c = (int)(key[i]);
                int z = ((c+roll(i))%96+34);
                if ((int)(keygen[i]) != (int)(z)){
                        printf("Imposter!!");
                        exit(0);
                }

        }
        printf("https://www.youtube.com/watch?v=TeSRoEjevHI");
}