/* Program that shows the return values (in hex)
of the 0xFFFF^0x8888, 0xABCD & 0x4567,
and 0xDCBA | 0x1234 expressions */

#include <stdio.h>

main()
{
    int x, y, z;
    
    x = 0xFFFF^0x8888;
    y = 0xABCD & 0x4567;
    z = 0xDCBA | 0x1234;
    
    printf("The hex values of 0xFFFF^0x8888 is %X \n", x);
    printf("The hex values of 0xABCD & 0x4567 is %X \n", y);
    printf("The hex values of 0xDCBA | 0x1234 is %X", z);
    
    return 0;
}