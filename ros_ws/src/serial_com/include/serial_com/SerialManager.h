#pragma once

#include <serial_com/request.h>
#include <wiringSerial.h>
#include <iostream>
#include <string>
#include <termios.h>
#include <ros/ros.h>
#include "custom_msgs/SerialPacket.h"


class SerialManager{

	int fd; //file descriptor to the socket
	bool stopReading; //boolean used to stop reading because a write order has been received
	ros::NodeHandle N; //node handler
	ros::Rate rate;

	ros::Publisher recv_topic;
	ros::Subscriber send_topic;

	token_t tokenIn;
	token_t tokenOut;
	uint8_t bufferIn[MAX_BUFFER_LEN];
	uint8_t bufferOut[MAX_BUFFER_LEN];
	custom_msgs::SerialPacket serialPacketIn;

	

public:
	SerialManager(std::string filename, int baudrate):stopReading(false),N(),rate(1)
	{
		struct termios options;

		//open the file descriptor
		fd = serialOpen(filename.c_str(),baudrate);
		if(fd==-1)
			std::cout << "Error opening the serial file" << std::endl;

		//update the timeout to set it to 1 second
		tcgetattr (fd, &options);
		options.c_cc [VTIME] = 1 ; //100 milliseconds timeout
		tcsetattr (fd, TCSANOW, &options);

		//create publisher and subscriber
		// topic on which incoming data will be written
		recv_topic = N.advertise<custom_msgs::SerialPacket>("/com/serial/recv", 20);
		// topic on which data to send must be written
		send_topic = N.subscribe("/com/serial/send", 1, &SerialManager::callback,this);
		
	}


	void callback(const custom_msgs::SerialPacket& packet){
		tokenOut.reqCode = packet.Code;
		tokenOut.reqCode = packet.Length;

		if (packet.Length >0 && packet.Length<= MAX_BUFFER_LEN){
			int indice = 0;
			for(uint8_t i : packet.Buffer)
				bufferOut[indice++] = i;				
				//serialPacketIn.push_back(bufferIn[i]);
				//std::memcpy(bufferOut,packet.Buffer,packet.Length);
		}
		// Callback is called in the same thread, if a read operation is being done, we must wait
		stopReading = true;
	}



	void handleRequest(token_t* T, uint8_t* buffer){

		uint16_t Code = T->reqCode, Length = T->reqLength;
		box_payload_t bp;

		switch(Code){
	
		case SEND_COORDS:
			std::memcpy(bp.bytes,buffer,Length);
			printf("X = %d \nY = %d\nlength=%d\nwidth=%d\n",bp.box.x,bp.box.y,bp.box.length,bp.box.width);
			break;
		default:	
			break;

		}

	}

	
	
	

	// main function : continually reads the port and gets interrupted by a write request
	void run(){
		int code=0;
		
		while(ros::ok()) {

			
			if(stopReading==true){
				sendRequest(fd,&tokenOut,bufferOut);
				stopReading=false;
			}
		

			if(getRequest(fd,&tokenIn,bufferIn) == SUCCESS){
				parseToken(&tokenIn);
				serialPacketIn.Code = tokenIn.reqCode;
				serialPacketIn.Length = tokenIn.reqLength;
				//std::memcpy(serialPacketIn.Buffer,bufferIn,serialPacketIn.Length);
				if (tokenIn.reqLength >0 && tokenIn.reqLength<= MAX_BUFFER_LEN){
					for(uint8_t i = 0; i<tokenIn.reqLength; ++i)
						serialPacketIn.Buffer[i] = bufferIn[i];
				}
				
				
					
				//handleRequest(&tokenIn,bufferIn);
			}
			rate.sleep();
		}
	}

	

	
};
