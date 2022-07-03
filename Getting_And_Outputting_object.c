/* putting characters B, y, and e together on the screen. */ 

#include <stdio.h>

main()
{
    int ch1, ch2, ch3;
    
    printf("Write three letters on the field: \n");
    
    ch1 = getchar();
    ch2 = getchar();
    ch3 = getchar();
    
    printf("The letters you wrote are:\n");
    
    putchar(ch1);
    putchar(ch2);
    putchar(ch3);
    
    return 0;
}