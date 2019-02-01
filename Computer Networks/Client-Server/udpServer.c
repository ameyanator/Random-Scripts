#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main()
{
    int sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    struct sockaddr_in servaddr;
    __bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(21000);
    bind(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr));

    struct sockaddr_in cliaddr;
    __bzero(&cliaddr, sizeof(cliaddr));

    char buffer[100];
    socklen_t clilen;
    while(1)
    {
        __bzero(buffer,100);
        int bytesReceived = recvfrom(sockfd, (char *)buffer, 100, 0, (struct sockaddr*)&cliaddr, &clilen);
        printf("message received is -> %s\n",buffer);
        // printf("%d\n", cliaddr.sin_port);
        // printf("%d\n", cliaddr.sin_addr.s_addr);
        buffer[bytesReceived] = '\0';
        sendto(sockfd, (char *)buffer, strlen(buffer), 0, (struct sockaddr*)&cliaddr, clilen);
        printf("Message sent back\n");
    }
}