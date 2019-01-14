#pragma once

#include <serial_com/serial_utils.h>
#include <wiringSerial.h>
#include <iostream>
#include <string>
#include <termios.h>
#include <ros/ros.h>
#include "custom_msgs/SerialRequest.h"


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
	custom_msgs::SerialRequest serialRequestIn;


public:


	SerialManager(std::string filename, int baudrate);

	int openSerial(std::string filename, int baudrate);

	void callback(const custom_msgs::SerialRequest& packet);

	// main function : continually reads the port and gets interrupted by a write request
	void run();

	

	
};
