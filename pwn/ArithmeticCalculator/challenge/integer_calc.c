#include <stdio.h>
#include <stdlib.h>

unsigned long numbers[0x20] = {0};

__attribute__((constructor)) void ignore_me(){
    setbuf(stdout, NULL);
}

int get_index(){
    int idx;

    printf("index: ");
    scanf("%d", &idx);

    if(idx > 0x20){
        printf("Invalid index\n");
        exit(-1);
    }
    
    return idx;
}

void store(void){
    unsigned long num;
    int index = get_index();

    printf("value: ");
    scanf("%lu", &num);

    numbers[index] = num;
    printf("Number %lu stored at index %d successfully\n", num, index);
}

void rm(void){
    int index = get_index();
    numbers[index] = 0;
}

void add(void){
    printf("First number's ");
    int idx1 = get_index();

    printf("Second number's ");
    int idx2 = get_index();

    printf("Addition result: %lu\n", numbers[idx1] + numbers[idx2]);
}

void sub(void){
    printf("First number's ");
    int idx1 = get_index();

    printf("Second number's ");
    int idx2 = get_index();

    printf("Subtraction result: %lu\n", numbers[idx1] - numbers[idx2]);
}

void mul(void){
    printf("First number's ");
    int idx1 = get_index();

    printf("Second number's ");
    int idx2 = get_index();

    printf("Multiplication result: %lu\n", numbers[idx1] * numbers[idx2]);
}

void divi(void){
    printf("First number's ");
    int idx1 = get_index();

    printf("Second number's ");
    int idx2 = get_index();

    printf("Division result: %lu\n", numbers[idx1] / numbers[idx2]);
}

void (*operations[])(void) = {store, rm, add, sub, mul, divi, exit};

unsigned int menu(void){
    unsigned choice;

    while(1){
        puts(
            "0) store number\n"
            "1) remove number\n"
            "2) add two numbers\n"
            "3) subtract two numbers\n"
            "4) multiply two numbers\n"
            "5) divide two numbers\n"
            "6) exit");
        
        printf("> ");
        scanf("%u", &choice);

        if(choice > 6){
            puts(" Invalid option. try again");
            continue;
        }
        break;
    }

    return choice;
}

int main(void){
    puts("Welcome to my arithmetic calculator!");

    while(1){
        unsigned option = menu();
        operations[option]();
    }
}
