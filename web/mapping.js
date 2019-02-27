
var deviceManager = {
  number = 0,
  robotList = {},
  droneList = {},
  robot : function={
    for (robot in this.robotList){
      this.number++;
    }
    return this.number;
  }
}

function retrieveRobot(id)={
  return deviceManager.robotList[id];
}
