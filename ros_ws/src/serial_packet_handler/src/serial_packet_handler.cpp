#include <serial_packet_handler/SerialPacketHandler.h>




int main(int argc, char **argv)
{
	ros::init(argc, argv, "SerialPacketHandler");
  	SerialPacketHandler SPH;
	SPH.run();
}
