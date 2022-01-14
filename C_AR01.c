#include <stdio.h>
#include <string.h>

char buf[8192][8192];
int main() {
    char line[8192];
    
    for (; fgets(line, 8192, stdin);) {
        int n = 0;
        char *ptr = strtok(line, " \n");
        for (; ptr; n++) {
            strcpy(buf[n], ptr);
            ptr = strtok(NULL, " \n");
        }
        for (int i = n-1; i >=0; i--) {
            printf("%s%c", buf[i], " \n"[i == 0]);
        }
    }
    

    return 0;
}
