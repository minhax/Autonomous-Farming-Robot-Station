#include "serial_com/request.h"
#include <ros/ros.h>
#include <wiringSerial.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include "serial_com/SerialManager.h"

int main(int argc, char **argv) {

     	ros::init(argc, argv, "serial_com");
	SerialManager M("/dev/ttyAMA0",115200);
	M.run();
}
