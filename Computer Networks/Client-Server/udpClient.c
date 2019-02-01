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
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(21000);
    servaddr.sin_addr.s_addr = INADDR_ANY;

    char messageToSend[100];
    printf("Enter the message that you want to send\n");
    scanf("%s",messageToSend);

    sendto(sockfd, (char *)messageToSend, strlen(messageToSend), 0, (struct sockaddr*)&servaddr, sizeof(servaddr));

    int len;
    char messageReceived[100];
    int bytesReceived = recvfrom(sockfd, (char *)messageReceived, 100, 0, (struct sockaddr*)&servaddr, &len);
    printf("%s\n",messageReceived);
    close(sockfd);
}