# -*- coding: utf-8 -*-
import datetime

class Status():

    SUCCESS             =       ('SUCCESS')
    CRITICAL            =       ('CRITICAL')
    PENDING             =       ('PENDING')
    PAUSED              =       ('PAUSED')
    ERROR               =       ('ERROR')

    def __init__(self, message):
        self.message = message
        # Creation Time
        self.beginTimeStamp = datetime.datetime.now().isoformat()
        # End of execution time
        # Default value is set to creation time
        self.endTimeStamp = datetime.datetime.now().isoformat()

    @property
    def timeStamp(self):
        return self.__timeStamp

    @property
    def endTimeStamp(self):
        return self.__endTimeStamp

    @endTimeStamp.setter
    def endTimeStamp(self, value):
        self.__endTimeStamp = value

    def computeTimes(self):
        try:
            tdelta = self.endTimeStamp - self.beginTimeStamp
        except: #TODO Faire mieux
            print("timeStamp error")
        return tdelta




