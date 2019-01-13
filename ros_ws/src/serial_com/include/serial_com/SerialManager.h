#pragma once

#include <serial_com/request.h>
#include <wiringSerial.h>
#include <iostream>
#include <string>
#include <termios.h>
#include <ros/ros.h>
#include "custom_msgs/PlantBox.h"


class SerialManager{

	int fd; //file descriptor to the socket
	bool stopReading; //boolean used to stop reading because a write order has been received
	bool SC_write_access; //boolean used for acknoledgement 
	ros::NodeHandle N; //node handler
	ros::Rate rate;

	ros::Publisher reception;
	ros::Subscribe envoi;

	token_t tokenIn;
	token_t tokenOut;
	uint8_t bufferIn[MAX_BUFFER_LEN];
	uint8_t bufferOut[MAX_BUFFER_LEN];

	

public:
	SerialManager(std::string filename, int baudrate):stopReading(false),SC_write_access(false),N(),rate(1)
	{
		struct termios options;

		//open the file descriptor
		fd = serialOpen(filename.c_str(),baudrate);
		if(fd==-1)
			std::cout << "Error opening the serial file" << std::endl;

		//update the timeout to set it to 1 second
		tcgetattr (fd, &options);
		options.c_cc [VTIME] = 10 ; //1 second timeout
		tcsetattr (fd, TCSANOW, &options);

		//create publisher and listener
		reception = N.advertise<custom_msgs::PlantBox>("/recv", 20);
		envoi = N.subscribe("my_topic", 1, callback);
		
	}



	void handleRequest(token_t* T, uint8_t* buffer){

		uint16_t Code = T->reqCode, Length = T->reqLength;
		box_payload_t bp;

		switch(Code){
	
		case SEND_COORDS:
			memcpy(bp.bytes,buffer,Length);
			printf("X = %d \nY = %d\nlength=%d\nwidth=%d\n",bp.box.x,bp.box.y,bp.box.length,bp.box.width);
			break;
		default:	
			break;

		}

	}

	void writeData(){

		stopReading = true;
		while(stopReadingACK == false);

		/* insert sendRequest code */

		stopReading = false;
		

	}
	
	

	// main function : continually reads the port and gets interrupted by a write request
	void run(){
		int code=0;
		
		while(ros::ok()) {

			if(stopReading==true){
				while(SC_write_access==false);
				sendRequest(fd,&tokenOut,bufferOut);
			}
				//stopReadingACK = true;
			//while(stopReading==true);
			//stopReadingACK = false;

			if(getRequest(fd,&tokenIn,bufferIn) == SUCCESS){
				parseToken(&tokenIn);
				handleRequest(&tokenIn,bufferIn);
			}
			rate.sleep();
		}
	}

	

	
};
