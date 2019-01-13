#include "serial_com/request.h"


// ------------------------------------//
// 		Request		       //
// ------------------------------------//


int sendToken(int fd, token_t* T){
	return write(fd, T, sizeof(token_t));
}

int getToken(int fd, token_t* T){
	return read(fd, T, sizeof(token_t));
}

int sendPayload(int fd, uint8_t* buffer, uint16_t Length){
	return write(fd, buffer, Length);
}

int getPayload(int fd, uint8_t* buffer, uint16_t Length){
	return read(fd, buffer, Length);
}

int sendRequest(int fd, token_t* T, uint8_t* buffer){
	


	if(T->reqLength < 0 || T->reqLength > MAX_BUFFER_LEN)
		return SENDPAYLOAD_FAILED;

	sendToken(fd,T);

	if(T->reqLength == 0)
		return SUCCESS;

	sendPayload(fd, buffer, T->reqLength);
	return SUCCESS;
}

int getRequest(int fd, token_t* T, uint8_t* buffer){

	if (getToken(fd,T) ==-1)
		return GETTOKEN_FAILED;

	if(T->reqLength < 0 || T->reqLength > MAX_BUFFER_LEN)
		return GETTOKEN_FAILED;
	else if (T->reqLength == 0 )
		return SUCCESS;
	
	int availableBytes = 0;	
	time_t t1 =time(NULL),t2=time(NULL);
	while( (availableBytes < T->reqLength) && (t2-t1 < 2)){
		ioctl (fd, FIONREAD, &availableBytes );
		t2=time(NULL);
	}

	if(availableBytes == T->reqLength){
		getPayload(fd, buffer, T->reqLength);
		return SUCCESS;
	}

	return GETPAYLOAD_FAILED;
	
}

void parseToken(token_t* T){
	printf("Request parsing\nRequest code : %u\nRequest data length : %u\n",T->reqCode, T->reqLength);
}

void hexdumpRequest(token_t* T){
	uint8_t *ptr = (uint8_t*)T;
	for(int i = 0; i<sizeof(token_t); ++i)
		printf("%x\n",ptr[i]);
}


