#include <stdio.h>
#include <stdlib.h>

#define ll long long

ll matrix[1000][1000], total_weight;
int inp[100], vis[1000], arr[1000], flag[63];

void __attribute__((constructor)) fix()
{
    flag[0] = 105;
    flag[1] = 23;
    flag[2] = 113;
    flag[3] = 211;
    flag[4] = 12;
    flag[5] = 5;
    flag[6] = 39;
    flag[7] = 42;
    flag[8] = 66;
    flag[9] = 160;
    flag[10] = 71;
    flag[11] = 33;
    flag[12] = 18;
    flag[13] = 117;
    flag[14] = 104;
    flag[15] = 240;
    flag[16] = 24;
    flag[17] = 4;
    flag[18] = 166;
    flag[19] = 64;
    flag[20] = 91;
    flag[21] = 219;
    flag[22] = 133;
    flag[23] = 141;
    flag[24] = 169;
    flag[25] = 161;
    flag[26] = 191;
    flag[27] = 141;
    flag[28] = 171;
    flag[29] = 124;
    flag[30] = 171;
    flag[31] = 110;
    flag[32] = 178;
    flag[33] = 249;
    flag[34] = 114;
    flag[35] = 6;
    flag[36] = 103;
    flag[37] = 204;
    flag[38] = 5;
    flag[39] = 51;
    flag[40] = 50;
    flag[41] = 47;
    flag[42] = 71;
    flag[43] = 174;
    flag[44] = 9;
    flag[45] = 39;
    flag[46] = 70;
    flag[47] = 60;
    flag[48] = 111;
    flag[49] = 184;
    flag[50] = 14;
    flag[51] = 75;
    flag[52] = 245;
    flag[53] = 71;
    flag[54] = 67;
    flag[55] = 208;
    flag[56] = 137;
    flag[57] = 217;
    flag[58] = 162;
    flag[59] = 185;
    flag[60] = 174;
    flag[61] = 140;
    flag[62] = 183;
}

void read_file_and_init() {
    FILE *fp;
    fp = fopen("./abc_original.txt", "r");

    int x, y, weight, m = 100000;

    for (int i=0; i<m; i++) {
        fscanf(fp, "%d %d %d", &x, &y, &weight);
        matrix[x][y] = weight;
        matrix[y][x] = weight;
    }

    arr[82] = 1;    //1
    arr[134] = 2;   //2
    arr[208] = 3;   //3
    arr[671] = 4;   //4
    arr[724] = 5;   //5
    arr[969] = 6;   //6

    fclose(fp);
}

void input_and_check() {
    int n = 34, state = 0;

    printf("Hello, let's walk with me:\n");
    for (int i=0; i<n; i++)
        scanf("%d", &inp[i]);

    if (inp[0] != 0) {
        printf("Illegal move my dude :(");
        exit(0);
    }

    int num = 0;
    for (int i=0; i<n - 1; i++) {
        if (matrix[inp[i]][inp[i + 1]] == 0) {
            printf("Illegal move my dude :(");
            exit(0);
        }
        total_weight += matrix[inp[i]][inp[i + 1]];
        if (arr[inp[i + 1]] != 0) {
            state |= (1 << (arr[inp[i + 1]] - 1));
        }
    }
    
    if (total_weight <= 18951 && state == 63) {
        printf("Correct, here's your flag:\n");
        for (int i=0; i<63; i++)
            printf("%c", flag[i] ^ (inp[i % 34] & 0xff));
    }
    else {
        printf("Fail, walking must be very frustrating right? :p");
        exit(0);
    }
}

int main() {
    read_file_and_init();
    input_and_check();
    return 0;
}

//0 371 276 952 119 82 838 582 553 969 553 582 562 540 283 208 619 107 134 38 814 181 937 685 203 724 203 685 970 16 216 769 658 671
