#include <stdio.h>
#include <stdlib.h>
#define MAX_COMPLAINTS 10
#define DISCOUNT_PERCENTAGE 20/100

typedef unsigned uint;
typedef struct {
    uint total_orders;
    uint requests_handled;
    void (*offer_discount)(unsigned long);
} Manager;

Manager* manager;
char* complaints[MAX_COMPLAINTS];
uint sizes[MAX_COMPLAINTS];

__attribute__((constructor)) void ignore_me(void){
    setbuf(stdin,  NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void menu(void){
    puts(
        "1. Get a coffee - $2.50\n"
        "2. Get a chai latte - $3.25\n"
        "3. Get some water - $0.10\n"
        "4. File a complaint\n"
        "5. Revert a complaint\n"
        "6. Edit a complaint\n"
        "7. View a complaint\n"
        "8. I WANT TO SPEAK TO YOUR MANAGER\n"
        "9. Nahh. I'm fine\n"
    );
}

void order(char *item_name, double price){
    printf("Here's your %s.\nIt'll be %lf\n", item_name, price);
    if(manager) manager->total_orders++;
}

uint free_index(void){
    for(uint index = 0; index < MAX_COMPLAINTS; index++){
        if(complaints[index] == NULL)
            return index;
    }

    return -1;
}

uint get_index(void){
    uint index;

    printf("Please enter your complaint's ID: ");
    scanf("%u%*c", &index);

    if(index >= MAX_COMPLAINTS || complaints[index] == NULL){
        puts("Invalid ID");
        return -1;
    }

    return index;
}

void file_complaint(void){
    uint size;
    uint index = free_index();

    if(index == -1){
        puts("Our complaint box has been filled");
        return;
    }

    printf("How many characters does your complaint contain: ");
    scanf("%u%*c", &size);

    if(size >= 0x500){
        puts("I suggest writing a book instead.");
        return;
    }

    char *complaint = malloc(size);

    printf("Write your complaint: ");
    fgets(complaint, size, stdin);
    complaints[index] = complaint;
    sizes[index] = size;

    printf("Your complaint ID is %u\n", index);
}

void revert_complaint(void){
    uint index = get_index();

    if(index == -1)
        return;

    free(complaints[index]);
}

void edit_complaint(void){
    uint index = get_index();

    if(index == -1)
        return;

    printf("Write your complaint (again): ");
    fgets(complaints[index], sizes[index], stdin);
}

void view_complaint(void){
    uint index = get_index();

    if(index == -1)
        return;

    puts(complaints[index]);
}

void discount(unsigned long price){
    if(price < 1.0){
        puts("I can't give you discount on items that are under $1");
        return;
    }

    puts("Alright!");
    printf("Just pay $%ld to the cashier\n", price - (DISCOUNT_PERCENTAGE * price));
}

void get_manager(void){
    uint choice;
    unsigned long price;

    if(!manager)
        manager = (Manager *) malloc(sizeof(Manager));
    
    puts(
        "Hi! I'm manager of this coffee shop\n"
        "How can I help you?\n"
        "1. I need a discount\n"
        "2. My kid is younger than 10. I want free food for him\n"
        "3. I want to file a complaint"
    );

    printf("> ");
    scanf("%u", &choice);
    switch (choice)
    {
    case 1:
        printf("What's price of your item?: ");
        scanf("%lu", &price);
        manager->offer_discount(price);
        break;
    
    case 2:
        puts("Sure. Here's your voucher D15C0UN7-K1D5-3A7-FR33");
        break;

    case 3:
        file_complaint();
        break;

    default:
        break;
    }
}

int main(void){
    uint choice;

    puts("Welcome to my mini Coffee shop!\n");

    while(1){
        menu();
        printf("> ");
        scanf("%u%*c", &choice);

        switch (choice)
        {
        case 1:
            order("coffee", 2.50);
            break;
        
        case 2:
            order("chai latte", 3.25);
            break;

        case 3:
            order("water", 0.1);
            break;

        case 4:
            file_complaint();
            break;

        case 5:
            revert_complaint();
            break;

        case 6:
            edit_complaint();
            break;

        case 7:
            view_complaint();
            break;

        case 8:
            get_manager();
            break;

        case 9:
            return 0;
            break;

        default:
            puts("There's no such thing");
            break;
        }
    }

    return 0;
}