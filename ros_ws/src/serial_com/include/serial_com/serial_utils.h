#pragma once
#include <stdio.h>
#include <stdint.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/ioctl.h>

#define MAX_BUFFER_LEN 		64

//errors 
#define SUCCESS 		0
#define LEN_TOO_HIGH 		1
#define SENDTOKEN_FAILED 	2
#define SENDPAYLOAD_FAILED	3
#define GETTOKEN_FAILED 	2
#define GETPAYLOAD_FAILED	3

#define TIMEOUT_GET 		 1 //2 seconds timeout on get payload to avoid being stuck



//Peut être remplacé par __attribute__((__packed__))
#pragma pack(1)
typedef 
struct token{
	uint16_t reqCode;	// In case of future requests
	uint16_t reqLength;	// Number of bytes in the payload
} token_t;
#pragma pack(0)

#pragma pack(1)
typedef 
struct request{
	token_t Token;
	uint8_t Buffer[MAX_BUFFER_LEN];
} request_t;
#pragma pack(0)

// Functions to handle IO operations
int sendToken(int fd, token_t* T);
int getToken(int fd, token_t* T);
int sendPayload(int fd, uint8_t* buffer, uint16_t Length);
int getPayload(int fd, uint8_t* buffer, uint16_t Length);

// A request is a token_t and a data buffer
// Function to handle high level request sending
int sendRequest(int fd, token_t* T, uint8_t* buffer); 
int getRequest(int fd, token_t* T, uint8_t* buffer);

//int sendRequest(int fd, request_t* T); 
//int getRequest(int fd, request_t* T); 

void parseToken(token_t* T);
void hexdumpRequest(token_t* T);

