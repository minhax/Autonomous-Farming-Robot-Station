# -*- coding: utf-8 -*-
import datetime


class Status():

    SUCCESS             =       ('SUCCESS')
    ERROR               =       ('ERROR')
    INACTIVE            =       ('INACTIVE')

    def __init__(self, message="Default message"):
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





