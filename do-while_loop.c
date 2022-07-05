/* Using a do-while loop */

#include <stdio.h>

main()
{
    int i;
    
    i = 65;
    
    do 
    {
        printf("The numeric value of %c is %d.\n", i, i);
        i++;
    }
    while(i < 72);
    
    return 0;
}