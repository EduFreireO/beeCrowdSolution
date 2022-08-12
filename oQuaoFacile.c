#include <stdio.h>
#include <stdlib.h>
int main()
{
    int i = 0;
    int letra = 0;
    int palavra = 0;
    char string[51];
    printf(" ");
    scanf0("%[^\n]s",string);
    
    while (i != 49)
    {
        if((string[i] >= 65 && string[i] <= 90) || (string[i] >= 97 && string[i] <= 122) || (string[i] >= 48 && string[i] <= 57))
        {
            letra += 1;
            i += 1;
        }
        while(string[i] == ' ' || string[i] == '.')
        {    
            i += 1;
        }
    }
   
    int media = letra / palavra;
    if(media <= 3)
        printf("250");
    else if(media <= 5)
        printf("500");
    else
        printf("1000");        



}