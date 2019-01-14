#include <serial_com/SerialManager.h>


SerialManager::SerialManager(std::string filename, int baudrate):stopReading(false),N(),rate(10)
{
	
	fd = openSerial(filename,baudrate);
	if(fd==-1){
		std::cout << "Error opening the serial file" << std::endl;
	}
	//create publisher and subscriber
	// topic on which incoming data will be written
	recv_topic = N.advertise<custom_msgs::SerialRequest>("/com/serial/recv", 10);
	// topic on which data to send must be written
	send_topic = N.subscribe("/com/serial/send", 10, &SerialManager::callback,this);
	
}


int SerialManager::openSerial(std::string filename, int baudrate){


	struct termios options;

	//open the file descriptor
	int f = serialOpen(filename.c_str(),baudrate);
	if(f==-1)
		return f;

	//update the timeout to set it to 1 second
	tcgetattr (f, &options);
	options.c_cc [VTIME] = 1 ; //100 milliseconds timeout
	tcsetattr (f, TCSANOW, &options);

	return f;

}


void SerialManager::callback(const custom_msgs::SerialRequest& request){
	tokenOut.reqCode = request.Code;
	tokenOut.reqCode = request.Length;

	if (request.Length >0 && request.Length<= MAX_BUFFER_LEN){
		//return
		int indice = 0;
		for(uint8_t i : request.Buffer)
			bufferOut[indice++] = i;				
			//serialRequestIn.push_back(bufferIn[i]);
			//std::memcpy(bufferOut,request.Buffer,request.Length);
	}
	// Callback is called in the same thread, if a read operation is being done, we must wait
	stopReading = true;
}





// main function : continually reads the port and gets interrupted by a write request
void SerialManager::run(){
	int code=0;
	
	while(ros::ok()) {

		
		if(stopReading==true){
			sendRequest(fd,&tokenOut,bufferOut);
			stopReading=false;
		}
	
		//serialFlush(fd);
		if(getRequest(fd,&tokenIn,bufferIn) == SUCCESS){
			parseToken(&tokenIn);
			serialRequestIn.Code = tokenIn.reqCode;
			serialRequestIn.Length = tokenIn.reqLength;
			//std::memcpy(serialRequestIn.Buffer,bufferIn,serialRequestIn.Length);
			if (tokenIn.reqLength >0 && tokenIn.reqLength<= MAX_BUFFER_LEN){
				for(uint8_t i = 0; i<tokenIn.reqLength; ++i)
					serialRequestIn.Buffer[i] = bufferIn[i];
			}

			recv_topic.publish(serialRequestIn);
			serialFlush(fd);
			//handleRequest(&tokenIn,bufferIn);
		}
		rate.sleep();
	}
}

