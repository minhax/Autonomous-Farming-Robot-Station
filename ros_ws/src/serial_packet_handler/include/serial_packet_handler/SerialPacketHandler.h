#include <iostream>
#include <ros/ros.h>
#include <serial_packet_handler/serial_request_codes.h>
#include "custom_msgs/SerialRequest.h"
#include "custom_msgs/PlantBox.h" 
#include <ros/console.h>


class SerialPacketHandler{
	
	custom_msgs::SerialRequest SerialRequestOut;
	custom_msgs::PlantBox PlantBoxIn;
	
	ros::Subscriber plant_sub;
	ros::Subscriber serial_sub;

	ros::Publisher plant_pub;
	ros::Publisher serial_pub;

	ros::NodeHandle N;


public:

	SerialPacketHandler():N()
	{


	}

	void SerialRequestSender(const custom_msgs::PlantBox& msg){
		uint16_t code = SEND_PLANT_BOX;
		uint16_t length = 4*sizeof(uint32_t);	
		uint32_t buffer[4];
		uint8_t* bytes;

		buffer[0] = msg.x;
		buffer[1] = msg.y;
		buffer[2] = msg.length;
		buffer[3] = msg.width;
		
		bytes = (uint8_t*)buffer;

		for(int i=0; i<length; ++i)
			SerialRequestOut.Buffer[i] = bytes[i];
		
		
		SerialRequestOut.Code = code;
		SerialRequestOut.Length = length;

		
		//std::memcpy(&SerialRequestOut.Buffer[0], (uint8_t*)buffer, length);
		serial_pub.publish(SerialRequestOut);
	}


	// SerialRequest -> Whatever internal message
	void SerialRequestReceiver(const custom_msgs::SerialRequest& msg){

		uint16_t length = msg.Length;		
	
		switch(msg.Code){

		case SEND_PLANT_BOX:
			// Here replace 64 by the MAX_BUFFER_LEN macro
			if (length > 0 && length <= 64){


				uint32_t* valPtr = (uint32_t*)&msg.Buffer[0];
				PlantBoxIn.x = valPtr[0];
				PlantBoxIn.y = valPtr[1];
				PlantBoxIn.length = valPtr[2];
				PlantBoxIn.width = valPtr[3];
				
	
				plant_pub.publish(PlantBoxIn);

			}
		
		default:
			break;



		}
		
	}

	void run(){

			// subscriber to the plantbox topic (to be sent)
		plant_sub = N.subscribe("/image/plantbox_send", 10, &SerialPacketHandler::SerialRequestSender,this);

		// subscriber to the serialrequest topic (message has been received)
		serial_sub = N.subscribe("/com/serial/recv", 10, &SerialPacketHandler::SerialRequestReceiver,this);

		plant_pub = N.advertise<custom_msgs::PlantBox>("/image/plantbox_recv", 10);

		serial_pub = N.advertise<custom_msgs::SerialRequest>("/com/serial/send", 10);

		ros::spin();
	}



};


