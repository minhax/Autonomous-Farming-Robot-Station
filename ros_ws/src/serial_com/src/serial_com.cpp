#include "serial_com/SerialManager.h"

int main(int argc, char **argv) {

     	ros::init(argc, argv, "serial_com");
	SerialManager M("/dev/ttyAMA0",115200);
	M.run();
}
