#include <stdio.h>
#include <openssl/md5.h>

int main(int argc, char *argv[])
{

    unsigned char c[MD5_DIGEST_LENGTH];
    char *filename = "file.c";
    int i;
    FILE *inFIle = fopen (filename, "rb");
    MD5_CTX mdContext;
    int bytes;
    unsigned char data[1024]

    if( inFile == NULL )
    {


}
