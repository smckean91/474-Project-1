#modules
import sys
import os


class Process:

    #Private variables
    __message = None
    __time = None

    # Setup constructors
    def __init__(self, message, time_Stamp):
        self.__message = message
        self.__time_Stamp = time_Stamp

    # Set functions
    def set_Message(self, message):
        self.__message = message

    def set_Time(self,time_Stamp):
        self.__time_Stamp = time_Stamp

    # Get functions
    def get_Message(self):
        return str(self.__message)

    def get_Time(self):
        return int(self.__time_Stamp)


# This function will help us increment the clock counter in a
# a process locally before each event and send its payload to reciever.


# In this function, will deal with processing the message and
# update the counter


def main():
    # Create 3 processes
    P1 = Process(" ", 0)
    P2 = Process(" ", 0)
    P3 = Process(" ", 0)


if __name__ == '__main__':
    main()
