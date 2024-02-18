#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char c = get_char("Do you agree? (y/n)");
    // Logical or ||
    if (c == 'y' || c == 'Y')
    {
        printf("Agreed.\n");
    }
    // Logical or ||
    else if (c == 'n' || c == 'N')
    {
        printf("Not agreed.\n");
    }
}