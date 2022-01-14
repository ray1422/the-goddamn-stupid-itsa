int arr[8192]; 
#include <stdio.h> 
int main() { 
    int n; scanf("%d", &n); 
    for (int i = 0; i < n; i++) { 
        int a, b; 
        scanf("%d %d", &a, &b); 
        for (int i = a; i < b; i++) { 
            arr[i]++; 
        } 
    } 
    int u=  0; 
    for (int i = 0; i < 8192; i++) { 
        if (arr[i] > u) u = arr[i]; 
    } 
 
    printf("%d\n", u); 
}  
