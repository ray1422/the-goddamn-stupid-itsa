#include <stdio.h>   
   
int main() {   
    int s = 0, b;   
    for (int i = 0; i < 6; i++) {   
         scanf("%d", &b);   
         s += b * b * b;   
    }   
    printf("%d\n", s);   
}  
