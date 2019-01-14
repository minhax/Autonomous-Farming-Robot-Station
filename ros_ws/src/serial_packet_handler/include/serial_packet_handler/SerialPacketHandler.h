#include <iostream>
#include <ros/ros.h>
#include <serial_packet_handler/serial_request_codes.h>
#include "custom_msgs/SerialRequest.h"
#include "custom_msgs/PlantBox.h"


class SerialPacketHandler{
	
	custom_msgs::SerialRequest SerialRequestOut;
	custom_msgs::PlantBox PlantBoxIn;
	
	ros::Subscriber plant_sub;
	ros::Subscriber serial_sub;

	ros::Publisher plant_pub;
	ros::Publisher serial_pub;

	ros::NodeHandle N;

	uint8_t buffer[64];

public:

	SerialPacketHandler():N()
	{


	}

	void SerialRequestSender(const custom_msgs::PlantBox& msg){

	}


	// SerialRequest -> Whatever internal message
	void SerialRequestReceiver(const custom_msgs::SerialRequest& msg){

		uint16_t length = msg.Length;		
	
		switch(msg.Code){

		case SEND_PLANT_BOX:
			if (length > 0 && length <= 64){


				uint32_t* valPtr = (uint32_t*)&msg.Buffer[0];
				PlantBoxIn.x = valPtr[0];
				PlantBoxIn.y = valPtr[1];
				PlantBoxIn.length = valPtr[2];
				PlantBoxIn.width = valPtr[3];
				
				uint64_t t = *((uint64_t*)(valPtr+4));

				struct timeval tv;
				gettimeofday(&tv,NULL);
				uint64_t now = 1000000 * tv.tv_sec + tv.tv_usec;
				
				std::cout<<"then : "<<t<<std::endl<<"now : "<<now<<std::endl;
	
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


